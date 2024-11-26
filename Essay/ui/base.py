import reflex as rx
from .nav import navbar

def base_page(child: rx.Component)-> rx.Component:
    
    return rx.fragment(
        navbar(),
        child,
        rx.color_mode.button(position="down-left",
                             id='darkmode_btn_id'),
        id = 'base_page_id'
    )