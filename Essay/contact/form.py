import reflex as rx 


from .state import ContactState
from..auth.state import  SessionState

def contact_form() -> rx.Component:
    username = SessionState.authenticated_username
    valid_user = SessionState.is_authenticated
    return rx.form(
                rx.cond(
                    valid_user,
                    rx.box(
                        rx.box(
                            rx.text_area(
                                name='first_name',
                                value= username,
                                required=True,
                                type='hidden',
                            ),
                            display='none'
                        ),
                        rx.text_area(
                            name='message',
                            placeholder="Your message",
                            required=True,
                            height='50vh',
                            width='100%',
                        ),
                        padding='1em'
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.input(
                                name="first_name",
                                placeholder="First Name",
                                required=True,
                                type='text',
                                width='100%',
                            ),
                            rx.input(
                                name="last_name",
                                placeholder="Last Name",
                                type='text',
                                width='100%',
                            ),
                            width='100%'
                        ),
                        rx.input(
                            name='email',
                            placeholder='Your email',
                            type='email',
                            width='100%',
                        ),
                        rx.text_area(
                            name='message',
                            placeholder="Your message",
                            required=True,
                            height='50vh',
                            width='100%',
                        ),
                    ),
                ),
                rx.button("Submit", type="submit"),
                on_submit=ContactState.handle_submit,
                reset_on_submit=True,
            )