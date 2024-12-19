import reflex as rx

from ..auth.state import SessionState
from .nav import navbar
from .dashboard import base_dashboard_page

def base_layout_component(child) -> rx.Component:
    return rx.fragment( # renders nada
        navbar(),
        rx.box(
            child,
            # bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
            id="my-content-area-el"
        ),
        rx.color_mode.button(position="bottom-left"),
        # padding='10em',
        # id="my-base-container"
    )

def base_page(child: rx.Component) -> rx.Component:
    return rx.cond(
        SessionState.is_authenticated,
        base_dashboard_page(child),
        base_layout_component(child),
    )