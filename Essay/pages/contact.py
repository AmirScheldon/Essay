import reflex as rx
from ..ui.base import base_page
from .. import navigations


class ContactState(rx.State):
    form_data: dict = {}
    
    @rx.event
    def submit_handler(self, form_data: dict):
        print(form_data)
        self.form_data = form_data


@rx.page(route= navigations.routes.CONTACT_ROUTE)
def contact() -> rx.Component:
    my_form = rx.vstack(
                rx.form(
                    rx.vstack(
                        rx.input(
                            type='text',
                            name="first_name",
                            placeholder="First Name",
                            required= True
                        ),
                        rx.input(
                            type='text',
                            name="last_name",
                            placeholder="Last Name"
                        ),
                        rx.input(
                            type='email',
                            name='email',
                            placeholder='email'
                        ),
                        rx.text_area(
                            type='text',
                            name= 'text',
                            placeholder= 'enter a text',
                            required= True
                        ),
                        rx.button("Submit", type="submit"),
                        align='center',
                    ),
                    on_submit=ContactState.submit_handler,
                    reset_on_submit=True,
                ),
            )
    
    child = rx.vstack(
            # vertical stack
            rx.heading('Contact Us', size= '9', align= 'center'),
            my_form,
            spacing="5",
            justify="center",
            align = 'center',
            min_height="85vh",
            id = 'contact'
        )
    
    return base_page(      
            child)
    
