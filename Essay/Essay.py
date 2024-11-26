import reflex as rx

from rxconfig import config
from .ui.base import base_page


from . import navigations
from .pages import about, contact
class State(rx.State):
    label = 'Label one'
    
    def on_change_function(self, val):
        self.label = val
        
    def on_click_function(self):
        print('clicked!')


@rx.page(route= navigations.routes.HOME_ROUTE)
def index() -> rx.Component:
    
    child = rx.vstack(
            # vertical stack
            rx.heading(State.label, size= '9', align= 'center'),
            rx.link(rx.button('About US'), href= navigations.routes.ABOUT_US_ROUTE),
            spacing="5",
            justify="center",
            align = 'center',
            min_height="85vh",
            id = 'child_id'
        )
    
    return base_page(      
            child)
    
app = rx.App()
app.add_page(contact.contact)


