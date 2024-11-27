import reflex as rx
from .state import ContactState

def contact_form() -> rx.Component:
    return rx.vstack(
                rx.form(
                    rx.vstack(
                        rx.hstack(
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
                            width = '100%'
                        ),
                        rx.input(
                            type='email',
                            name='email',
                            placeholder='Email',
                            width = '100%'
                        ),
                        rx.text_area(
                            type='text',
                            name= 'text',
                            placeholder= 'Enter a text',
                            required= True,
                            width = '100%'
                        ),
                        rx.button("Submit", type="submit"),
                        align='center',
                    ),
                    on_submit=ContactState.submit_handler,
                    reset_on_submit=True,
                ),
            )