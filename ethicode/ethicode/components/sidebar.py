"""Sidebar component for the app."""

from ethicode import styles

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.chakra.hstack(
        rx.chakra.image(
            src="/blob.svg",
            height="8em",
        ),
        rx.chakra.spacer(),
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return rx.chakra.hstack(
        rx.chakra.spacer(),
        rx.chakra.link(
            rx.chakra.text("Open Design Duke"),
            href="https://opendesignstudio.duke.edu/",
        ),
        width="100%",
        border_top=styles.border,
        padding="1em",
    )


def sidebar_item(text: str, url: str) -> rx.Component:
    active = (rx.State.router.page.path == f"/{text.lower()}") | (
        (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.chakra.link(
        
        rx.chakra.hstack(
    rx.chakra.text(text, font_size="1.25em"),
    bg=rx.cond(
        active,
        styles.accent_color,
        "transparent",
    ),
    color=rx.cond(
        active,
        styles.accent_text_color,
        styles.text_color,
    ),
    border_radius=styles.border_radius,
    width="100%",
    padding_x="2em",  # Increased horizontal padding
    padding_y="1em",  # Added vertical padding for larger button appearance
    _hover={
        "box_shadow": "0 4px 14px 0 rgba(0, 0, 0, 0.25)",  # Shadow appears only on hover
    },
),
        href=url,
        width="100%",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    from reflex.page import get_decorated_pages

    return rx.chakra.box(
        rx.chakra.vstack(
            sidebar_header(),
            rx.chakra.vstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        # icon=page.get("image", "/github.svg"),
                        url=page["route"],
                    )
                    for page in get_decorated_pages()
                ],
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            rx.chakra.spacer(),
            sidebar_footer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
