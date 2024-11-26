import reflex as rx
from ..ui.base import base_page
from .. import navigations

@rx.page(route= navigations.routes.ABOUT_US_ROUTE)
def about() -> rx.Component:
    
    child = rx.vstack(
            # vertical stack
            rx.heading('About Us', size= '9', align= 'center'),
            spacing="5",
            justify="center",
            align = 'center',
            min_height="85vh",
            id = 'about'
        )
    
    return base_page(      
            child)
    
app = rx.App()
app.add_page(about)