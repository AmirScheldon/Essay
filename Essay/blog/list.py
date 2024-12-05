import reflex as rx
from ..ui.base import base_page
from .state import BLogPostState
from . import model
from .. import navigations


def blog_post_detail_list(child: rx.Component, post: model.BlogPostModel):
    post_id: int = post.id
    if post is None:
        return rx.fragment(child)
    if post_id is None:
        return rx.fragment(child)
    root_path = navigations.routes.BLOG_POSTS_ROUTE
    post_detail_url = f'{root_path}/{post_id}'
    return rx.link(
        child,
        href=post_detail_url
    )
    
    
def blog_list_item(post: model.BlogPostModel):
    return rx.box(
        blog_post_detail_list(
            rx.heading(post.title),
            post
        ),
    padding='1em'
    )

def blog_post_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            # vertical stack
            rx.heading('Blogs List', size= '5'),
            rx.link(rx.button('New Blog'),
                    href=navigations.routes.BLOG_ADD_ROUTE
                    ),
            rx.foreach(BLogPostState.posts, blog_list_item),
            spacing="5",
            align = 'center',
            min_height="85vh"
        )
    )
    
