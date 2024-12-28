import reflex as rx 

def dashboard_component() -> rx.Component:
    return rx.center(
        rx.heading('Welcome back', size='9'),
        min_height='85vh',
        align='center'
    )