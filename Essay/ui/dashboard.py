import reflex as rx

from .sidebar import sidebar

def base_dashboard_page(child: rx.Component) -> rx.Component:
    return rx.fragment( 
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                # bg=rx.color("accent", 3),
                padding="1em",
                width="100%",
                id="my-content-area-el"
            ),
            
        ),
    )