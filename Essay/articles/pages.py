import reflex as rx 
import reflex_local_auth
from .. import navigation
from ..ui.base import base_page
from ..models import BlogPostModel
from . import state
from ..blog.pages import blog_post_not_found

def article_card_link(post: BlogPostModel):
    """_summary_
        create link for each card in artcle page
    Args:
        post (BlogPostModel): takes an instance of model

    Returns:
        link: returns a link for each article
    """    
    post_id = post.id
    if post_id is None:
        return rx.fragment('Not Found!') # if there is not post to route to, returns a fragment
    root_path = navigation.routes.ARTICLE_LIST_ROUTE
    post_detail_url = f"{root_path}/{post_id}" # declare an url path to detail of a post

    return rx.card(
    rx.link(
        rx.flex(
            rx.box(
                rx.heading(post.title),
            ),
            spacing="2",
        ),
        href=post_detail_url
    ),
    as_child=True,
)

def article_public_lsit_component(columns:int=3, spacing:int=5, limit:int=10)-> rx.Component:
    """_summary_
        create  grids component for each articles and then use them on dashboard and landing pages. 
    Args:
        columns (int, optional): Defaults to 3.
        spacing (int, optional): Defaults to 5.
        limit (int, optional): Sets a limitation to show components per page. Defaults to 10.

    Returns:
        rx.Component: retruns Grids
    """    
    return rx.grid(
        rx.foreach(state.ArticlePublicState.posts, article_card_link),
        columns= f'{columns}',
        spacing= f'{spacing}',
        on_mount=lambda: state.ArticlePublicState.set_limit_and_reload(limit)
    )
@reflex_local_auth.require_login
def article_public_list_page() ->rx.Component:
    """_summary_
        published articles page
    """  
    return base_page(
        rx.vstack(
            rx.heading("Pulished Articles",  size="5"),
            article_public_lsit_component(),
            min_height="85vh",
        ),
    ) 
    

def article_detail_page() -> rx.Component:
    """_summary_
        shows published articles details
    """  
    my_child = rx.cond(state.ArticlePublicState.post, # if post does exist
            rx.vstack(
                rx.hstack(
                    rx.flex(
                    rx.heading(state.ArticlePublicState.post.title, size="9"),
                    align='end'
                    ),
                ),
            rx.text('Published at: ',state.ArticlePublicState.post.publish_date),
                rx.flex(
                    rx.box(
                        rx.text(
                            state.ArticlePublicState.post.content,
                            white_space='pre-wrap'
                        ),
                    ),
                ),
            spacing="5",
            align="start",
            min_height="85vh"
        ), # do this
        blog_post_not_found() # else show 'Not found' page
        )
    return base_page(my_child)
