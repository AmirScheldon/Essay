import reflex as rx
from ..ui.base import base_page
from .state import ContactState
from .form import contact_form



def contact_page() -> rx.Component:
    my_form =contact_form()
    child = rx.vstack(
            # vertical stack
            rx.heading('Contact Us', size= '9', align= 'center'),
            rx.cond(ContactState.submitted, ContactState.thank_you, ''),
            rx.desktop_only(my_form),
            rx.mobile_and_tablet(my_form),
            spacing="5",
            justify="center",
            align = 'center',
            min_height="85vh",
            id = 'contact'
        )
    
    return base_page(      
            child)