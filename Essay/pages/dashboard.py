import reflex as rx 
from ..auth.state import SessionState

def dashboard_component() -> rx.Component:
    username = SessionState.authenticated_username
    return rx.center(
        rx.heading(f'Welcome back {username}', size='9'),
        min_height='85vh',
        align='center'
    )