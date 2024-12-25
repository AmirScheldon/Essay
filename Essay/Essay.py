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
from .articles.list import article_public_list_page, article_public_lsit_component
from .articles.state import ArticlePublicState
from .articles.detail import article_detail_page
from .auth.state import SessionState 

@rx.page(route= navigation.routes.HOME_ROUTE)
def index() -> rx.Component:
    return base_page( 
            rx.cond(
                SessionState.is_authenticated,  
                pages.dashboard_component(),
                pages.landing_component()
            ),
        )
    
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
    index, 
    on_load=ArticlePublicState.load_posts
)

app.add_page(
    my_logout_page,
    route=navigation.routes.LOGOUT_ROUTE,
    title="Logout",
)

app.add_page(pages.about_page, 
             route=navigation.routes.ABOUT_US_ROUTE)

app.add_page(
    article_public_list_page, 
    route=navigation.routes.ARTICLE_LIST_ROUTE,
    on_load=ArticlePublicState.load_posts
 )  

app.add_page(
    article_detail_page, 
    route=f"{navigation.routes.ARTICLE_LIST_ROUTE}/[post_id]",
    on_load=ArticlePublicState.get_post_detail
)

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

