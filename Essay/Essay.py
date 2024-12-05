import reflex as rx
from .ui.base import base_page


from . import navigations
from .contact import state as state_contact
from .contact import page as page_contact
from .blog import list as blog_list
from .blog import state as blog_state
from .blog import add_page

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
app.add_page(page_contact.contact_page, route=navigations.routes.CONTACT_ROUTE)
app.add_page(page_contact.contact_list_page, 
             route=navigations.routes.CONTACT_ENTERIES_ROUTE,
             on_load=state_contact.ContactState.contact_list_entries)
app.add_page(add_page.blog_add_post_page, route=navigations.routes.BLOG_ADD_ROUTE)
app.add_page(blog_list.blog_post_list_page, 
             route= navigations.routes.BLOG_POSTS_ROUTE,
             on_load= blog_state.BLogPostState.load_posts)


