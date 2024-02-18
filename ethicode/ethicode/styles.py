"""Styles for the app."""

import reflex as rx

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
border = "1px solid #F4F3F6"
text_color = "black"
accent_text_color = "#1A1060"
# accent_color = "#F5EFFE"
accent_color = "##6495ED"
hover_accent_color = {"_hover": {"color": accent_color}}
hover_accent_bg = {"_hover": {"bg": accent_color}}
content_width_vw = "90vw"
sidebar_width = "20em"

template_page_style = {"padding_top": "5em", "padding_x": ["auto", "2em"], "flex": "1"}

template_content_style = {
    "align_items": "flex-start",
    "box_shadow": box_shadow,
    "border_radius": border_radius,
    "padding": "1em",
    "margin_bottom": "2em",
}

link_style = {
    "color": text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": "white",
    "border": border,
    "border_radius": border_radius,
}

base_style = {
    rx.chakra.MenuButton: {
        "width": "3em",
        "height": "3em",
        **overlapping_button_style,
    },
    rx.chakra.MenuItem: hover_accent_bg,
}

markdown_style = {
    "code": lambda text: rx.chakra.code(text, color="#1F1944", bg="#EAE4FD"),
    "a": lambda text, **props: rx.chakra.link(
        text,
        **props,
        font_weight="bold",
        color="#03030B",
        text_decoration="underline",
        text_decoration_color="#AD9BF8",
        _hover={
            "color": "#AD9BF8",
            "text_decoration": "underline",
            "text_decoration_color": "#03030B",
        },
    ),
}

sidebar_button_padding_x = "2em"
sidebar_button_padding_y = "1em"

sidebar_button_hover_box_shadow = "0 4px 14px 0 rgba(0, 0, 0, 0.25)"


hover_accent_bg = {
    "_hover": {
        "bg": accent_color,
        "box_shadow": sidebar_button_hover_box_shadow, 
    }
}


base_style = {
    rx.chakra.MenuButton: {
        "width": "3em",
        "height": "3em",
        "padding_x": sidebar_button_padding_x,  
        "padding_y": sidebar_button_padding_y, 
        **overlapping_button_style,
    },
    rx.chakra.MenuItem: hover_accent_bg,
}




# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin
)
answer_style = message_style | dict(
    margin_right=chat_margin,
    bg = "rgb(107,99,246)",
    color="white",
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1.25em", box_shadow=shadow
)
button_style = dict(
    background_color="#6495ED", box_shadow=shadow
)

card_style = {
    "_hover": {
        "box_shadow": "0 10px 15px rgba(0, 0, 0, 0.2)",
        "transform": "translateY(-10px)",
        "transition": "transform 0.2s ease-in-out"
    }
}