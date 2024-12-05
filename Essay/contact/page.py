import reflex as rx
from ..ui.base import base_page
from .state import ContactState
from .form import contact_form
from . import model

def contact_list_item(contact: model.ContactDataModel):
    return rx.box(
        rx.heading(contact.first_name),
        rx.text(contact.text),
        padding='1em'
        )

def contact_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            # vertical stack
            rx.heading('Contact List', size= '5'),
            rx.foreach(ContactState.enteries, contact_list_item),
            spacing="5",
            align = 'center',
            min_height="85vh"
        )
    )
    

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