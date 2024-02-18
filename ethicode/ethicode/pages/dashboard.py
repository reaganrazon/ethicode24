"""The Create page."""
from ethicode.templates import template

import reflex as rx
import fitz 
from sqlmodel import Field

color = "rgb(107,99,246)"
color2 = "rgb(55, 184, 238)"

def process_file(upload_data):
    text = ""
    try:
        doc = fitz.open(stream=upload_data, filetype="pdf")
        
        for page in doc:
            text += page.get_text()
        
        doc.close()
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return text


class lessonplan(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    filename: str
    content: str


class PDFUpload(rx.State):
    upload_status: str = ""
    text: str = ""
    
    def on_load(self):
        self.reset()

    async def handle_upload(self, files: list[rx.UploadFile]):

        with rx.session() as session:
            for file in files:
                file_data = await file.read()
                result = process_file(file_data)
                file_record = lessonplan(filename=file.filename, content=result)    
                self.upload_status = "File processed successfully" if result else "Processing failed"
                self.text = result
                session.add(file_record)

            session.commit()

@template(route="/create", title="Create",on_load=PDFUpload.on_load)


def dashboard() -> rx.Component:
    """The Create page.

    Returns:
        The UI for the Create page.
    """

    return rx.chakra.vstack(
    rx.chakra.heading("Curriculum Generator", font_size="3em", align="center"),
    rx.chakra.text("Ideate to create an ethics-centered computer science curriculum.", align="center"),
    rx.chakra.center(
        rx.upload(
            rx.chakra.vstack(
                rx.chakra.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                rx.chakra.text("Drag and drop relevant files here or click to select files."),
                        rx.text("Examples include: your favorite lesson plan, your county CS standards, etc." ),
            ),
            border="1px dotted rgb(107,99,246)",
            padding="4em",
        )
    ),
    rx.chakra.center(
                rx.foreach(rx.selected_files, lambda file: rx.text(file)),
    ),
    rx.chakra.center(
        rx.chakra.button(
            "Upload",color=color2, bg="white", border=f"1px solid {color2}",
            on_click=lambda: PDFUpload.handle_upload(rx.upload_files()),
        )
    ),
    rx.chakra.text(PDFUpload.upload_status, align="center"),
    rx.chakra.text(PDFUpload.text, align="center"),
    justify="center",
    align_items="center",
    spacing="24px",
)