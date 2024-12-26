import reflex as rx 
import reflex_local_auth
from .. import navigation
from ..ui.base import base_page
from ..models import BlogPostModel
from . import state
from .state import SessionState
from ..blog.pages import blog_post_not_found

def article_card_link(post: BlogPostModel):
    post_id = post.id
    if post_id is None:
        return rx.fragment('Not Found!')
    root_path = navigation.routes.ARTICLE_LIST_ROUTE
    post_detail_url = f"{root_path}/{post_id}"

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
    return rx.grid(
        rx.foreach(state.ArticlePublicState.posts, article_card_link),
        columns= f'{columns}',
        spacing= f'{spacing}',
        on_mount=lambda: state.ArticlePublicState.set_limit_and_reload(limit)
    )
@reflex_local_auth.require_login
def article_public_list_page() ->rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Pulished Articles",  size="5"),
            article_public_lsit_component(),
            min_height="85vh",
        ),
    ) 
    

def article_detail_page() -> rx.Component:
    usrername = SessionState.authenticated_username
    my_child = rx.cond(state.ArticlePublicState.post, 
            rx.vstack(
                rx.hstack(
                    rx.flex(
                    rx.heading(state.ArticlePublicState.post.title, size="9"),
                    rx.text('by: ', usrername),
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
        ), 
        blog_post_not_found()
        )
    return base_page(my_child)
