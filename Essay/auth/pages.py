import reflex as rx

from reflex_local_auth.pages.login import LoginState, login_form
from reflex_local_auth.pages.registration import RegistrationState

from .. import navigation
from ..ui.base import base_page

from .forms import my_register_form
from .state import SessionState

def my_login_page()->rx.Component:
    return base_page(
        rx.center(
            rx.cond(
                LoginState.is_hydrated,  # type: ignore
                rx.card(login_form()),
            ),
             min_height="85vh",
        ),
       
    )

def my_register_page()->rx.Component:
    return base_page(
        rx.center(
            rx.cond(
                RegistrationState.success, # If the registration is successfully done
                rx.vstack(
                    rx.text("Registration successful!"),
                ),# do this
                rx.card(my_register_form()), # else user refill registration form
                
            ),
             min_height="85vh",
        )
       
    )


def my_logout_page() -> rx.Component: 
    child = rx.box(
            rx.vstack(
                    rx.heading('Do you want to logout?', size= '9', align= 'center'),
                    rx.hstack(
                        rx.box(
                            rx.link(
                                rx.button(
                                    'Yes',
                                    on_click=SessionState.my_logout, # logouts the user
                                    size='4'
                                )
                            ),
                        border_radius="15px",
                        width="100%",
                        margin="16px",
                        padding="16px"
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    'No',
                                    color_scheme= 'gray',
                                    size='4'
                                ),
                                href=navigation.routes.HOME_ROUTE # returns the use to the home page
                            ),
                            border_radius="15px",
                            width="100%",
                            margin="16px",
                            padding="16px"
                            ),
                    ),
                    spacing="5",
                    justify="center",
                    align = 'center',
                    min_height="85vh",
                    id = 'child_id'
                ),
            radius="full",
            width="100%",
            margin="24px",
            padding="25px",
        )
    return base_page(      
            child)

