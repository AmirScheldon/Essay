import reflex as rx
from .ui.base import base_page
import reflex_local_auth

from .auth.pages import (
    my_login_page,
    my_register_page,
    my_logout_page
)

from . import navigation
from . import blog, contact, navigation, pages

class State(rx.State):
    label = 'Label one'
    
    def on_change_function(self, val):
        self.label = val
        
    def on_click_function(self):
        print('clicked!')


@rx.page(route= navigation.routes.HOME_ROUTE)
def index() -> rx.Component:
    
    child = rx.vstack(
            # vertical stack
            rx.heading(State.label, size= '9', align= 'center'),
            rx.link(rx.button('About Me'), href= navigation.routes.ABOUT_US_ROUTE),
            spacing="5",
            justify="center",
            align = 'center',
            min_height="85vh",
            id = 'child_id'
        )
    
    return base_page(      
            child)
    
app = rx.App()

# reflex_local_auth pages
app.add_page(
    my_login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    my_register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)

# my pages
app.add_page(
    my_logout_page,
    route=navigation.routes.LOGOUT_ROUTE,
    title="Logout",
)

app.add_page(pages.about_page, 
             route=navigation.routes.ABOUT_US_ROUTE)

app.add_page(
    blog.blog_post_list_page, 
    route=navigation.routes.BLOG_POSTS_ROUTE,
    on_load=blog.BlogPostState.load_posts
    
)

app.add_page(
    blog.blog_post_add_page, 
    route=navigation.routes.BLOG_POST_ADD_ROUTE
)

app.add_page(
    blog.blog_post_detail_page, 
    route="/blog/[blog_id]",
    on_load=blog.BlogPostState.get_post_detail
)

app.add_page(
    blog.blog_post_edit_page, 
    route="/blog/[blog_id]/edit",
    on_load=blog.BlogPostState.get_post_detail
)

app.add_page(contact.contact_page, 
             route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(
    contact.contact_entries_list_page, 
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries
)

