import reflex as rx 

from ..articles.list import article_public_lsit_component
from .. import navigation

def landing_component() -> rx.Component:
    return  rx.vstack(
            rx.heading('Welcome to Essay', size= '9', align= 'center'),
            rx.link(rx.button('About Me'), href= navigation.routes.ABOUT_US_ROUTE),
            rx.heading('Recent Articles', size= '4', align= 'center'),
            rx.divider(),
            article_public_lsit_component(columns=1, limit=1),
            spacing="5",
            justify="center",
            align = 'center',
            min_height="85vh",
            id = 'child_id'
        )