"""The evaluate page."""

from ethicode.templates import template

import reflex as rx

# class ItemState(rx.State):
#     item: str = ''

#     def fetch_item(self):
#         with rx.session() as session:
#             self.item = session.exec(rx.select(MyModel).first())


@template(route="/evaluate", title="Evaluate")
def settings() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.chakra.vstack(
        rx.chakra.heading("Evaluate", font_size="3em"),
        rx.chakra.text("Test and iterate your lesson plan."),

    #     rx.vstack(
    #     rx.button("Fetch Item", on_click=ItemState.fetch_item),
    #     rx.text(ItemState.item)
    # )
    )
