import reflex as rx
from ..ui.base import base_page
from .form import blog_create_post_form


def blog_add_post_page() -> rx.Component:
    my_form =blog_create_post_form()
    child = rx.vstack(
            # vertical stack
            rx.heading('Add Post', size='9', align= 'center'),
            rx.desktop_only(my_form),
            rx.mobile_and_tablet(my_form),
            spacing="5",
            justify="center",
            align = 'center',
            min_height="95vh",
        )
    
    return base_page(      
            child)