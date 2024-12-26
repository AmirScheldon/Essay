import reflex as rx 
from ..ui.base import base_page
from ..models import ContactEntryModel
from . import form, state

def contact_entry_list_item(contact: ContactEntryModel):
    return rx.box(
            rx.flex(
                rx.card(
                    rx.vstack(
                        rx.heading('User',contact.first_name),
                        rx.text(f"Message: {contact.message}"),
                        padding='1em',
                        align='start'
                        ),
                    ),
            direction='column'
                ),
            size='5',
            flex_wrap="wrap",
            width="100%",
            )

def contact_entries_list_page() ->rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size="5"),
            rx.foreach(state.ContactState.entries, contact_entry_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    ) 

def contact_page() -> rx.Component:
    
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.cond(state.ContactState.did_submit, state.ContactState.thank_you, ""),
            rx.desktop_only(
                rx.box(
                    form.contact_form(),
                    width='50vw'
                )
            ),
            rx.tablet_only(
                rx.box(
                    form.contact_form(),
                    width='75vw'
                )
            ),
            rx.mobile_only(
                rx.box(
                    form.contact_form(),
                    width='95vw'
                )
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)