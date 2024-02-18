"""The home page of the app."""

from ethicode import styles
from ethicode.templates import template
from ethicode.qstate import QState

import reflex as rx
color = "rgb(107,99,246)"


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=styles.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=styles.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            QState.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.chakra.input(
            value=QState.question,
            placeholder="Ask a question",
            on_change=QState.set_question,
            style=styles.input_style),
            rx.chakra.button("Ask", color="white", bg=color, border=f"0.5px solid {color}", on_click=QState.answer)
    )



@template(route="/", title="Understand")
def index() -> rx.Component:
    
    return rx.chakra.vstack(
        rx.chakra.heading("EthiCode", font_size="3em"),
        rx.hover_card.root(
            rx.hover_card.trigger(
                rx.chakra.text("An open-design approach to ethical computer science curriculum building and lesson plan development.")
            ),
            rx.hover_card.content(
                rx.callout(
                    "Understanding both your goals as an educator and the interests and backgrounds of your students is very important in curriculum design.",
                    icon="info"
                )
            )),
    rx.stack(
   rx.flex(
    rx.card(
        # rx.icon(name="icon2"),
        rx.heading("Active Inclusivity", font_size="1.5em", color = "#2E86C1"),
            rx.text("Co-creation and collaboration are at the heart of open-design methodologies. This means we must be intentional about actively including people who are historically underrepresented in all parts of the design process."),
            width="100%",style = styles.card_style
            ),
            rx.card(
                # rx.icon(name="icon2"),
                rx.heading("Transparency", font_size="1.5em", color = "#1E8449"),
                rx.text("Sharing our knowledge and information at every step of the development process is important because that is how we build trust and learn as a collective. Transparency applies to community interactions as well as our data gathering, wrangling, and training processes."),
                width="100%", style = styles.card_style
            ),
            rx.card(
                # rx.icon(name="icon3"),
                rx.heading("Collaboration", font_size="1.5em", color = color),
                rx.text("A collaborative approach to computer science curriculum development allows for an incorporation of diverse perspectives and expertise. Teachers, technology experts, and students all have something to contribute. Valuable approaches will address student feedback and provide an avenue for learning that is not just one size fits all."),
                width="100%",style = styles.card_style
            ),
            spacing="4",  
            direction="row", 
            width="100%",  
        ),
        rx.spacer(),
),      rx.chakra.heading("Learn More!", font_size="2em"),
 rx.chakra.text("Chat with our model trained with Retrieval-Augmented Generation on academic texts in the fields of computer science, ethics, and policy."),
        rx.container(chat(), action_bar())
    )
