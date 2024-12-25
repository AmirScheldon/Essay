import reflex as rx
import reflex_local_auth
from .. import navigation
from ..ui.base import base_page
from ..models import BlogPostModel
from . import state
from . import forms
from .state import BlogEditFormState, BlogPostState

def blog_post_not_found() -> rx.Component:
    return rx.hstack(
        rx.heading('Blog Post Not found!'),
        spacing='5',
        align='center',
        min_height='85vh'
    )
    


def blog_post_detail_link(child: rx.Component, post: BlogPostModel):
    if post is None:
        return rx.fragment(child)
    post_id = post.id
    if post_id is None:
        return rx.fragment(child)
    root_path = navigation.routes.BLOG_POSTS_ROUTE
    post_detail_url = f"{root_path}/{post_id}"

    return rx.link(
        child,
        rx.heading(f"by  {post.userinfo.user.username}"),
        href=post_detail_url
    )

def blog_post_list_item(post: BlogPostModel):

    return rx.box(
        blog_post_detail_link(
            rx.heading(post.title),
            post
        ),
        padding='1em'
    )

@reflex_local_auth.require_login
def blog_post_list_page() ->rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Blog Posts",  size="5"),
            rx.link(
                rx.button("New Post"),
                href=navigation.routes.BLOG_POST_ADD_ROUTE
            ),
            rx.foreach(state.BlogPostState.posts, blog_post_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
        ),
    ) 

@reflex_local_auth.require_login
def blog_post_edit_page() -> rx.Component:
    my_form = forms.blog_post_edit_form()
    post = BlogEditFormState.post
    my_child = rx.cond(post, 
            rx.vstack(
                rx.heading("Editing ", post.title, size="9"),
                rx.desktop_only(
                    rx.box(
                        my_form,
                        width='50vw'
                    )
                ),
                rx.tablet_only(
                    rx.box(
                        my_form,
                        width='75vw'
                    )
                ),
                rx.mobile_only(
                    rx.box(
                        my_form,
                        width='95vw'
                    )
                ),
                spacing="5",
                align="center",
                min_height="95vh",
            ),
            blog_post_not_found()  
        )
    return base_page(my_child)

def blog_post_detail_page() -> rx.Component:
    can_edit = True
    can_delete = True
    edit_link = rx.link("Edit", href=state.BlogPostState.blog_post_edit_url)
    delete_link = rx.link("Delete", href=state.BlogPostState.blog_post_delete_url)
    edit_link_el = rx.cond(
        can_edit,
        edit_link,
        rx.fragment("")
    )
    delete_link_el = rx.cond(
        can_delete,
        delete_link,
        rx.fragment("")
    )
    
    my_child = rx.cond(
        state.BlogPostState.post, 
            rx.vstack(
                rx.hstack(
                    rx.card(
                            rx.flex(
                                rx.box(
                                    rx.heading(state.BlogPostState.post.title, size="9"),
                                ),
                                spacing="2",
                        ),
                        as_child=True,
                    ),
                    rx.text(state.BlogPostState.post.publish_date),

                    align='end'
                ),
                    rx.card(
                        rx.flex(
                            rx.box(
                                rx.text(
                                    state.BlogPostState.post.content,
                                    white_space='pre-wrap'
                                ),
                                size='25vh',
                            ),
                        ),
                    as_child=True,
                    ),
                    rx.button(
                    edit_link_el,
                    color_scheme= 'gray'
                    ),
                    rx.button(
                        delete_link_el,
                        color_scheme= 'red'
                    ),
            spacing="5",
            align="center",
            min_height="85vh"
            ),
        blog_post_not_found()
        ), 
        
    return base_page(my_child)

def my_delete_page() -> rx.Component: 
    child = rx.vstack(
            rx.heading('Do you want to delete?', size= '9', align= 'center'),
            rx.link(
                rx.button(
                    'Yes, Delete',
                    on_click=BlogPostState.delete_blog,
                    size='4'
                ),
            ),
            rx.link(
                rx.button(
                    'No',
                    color_scheme= 'gray',
                    size='4'
                ),
                href=navigation.routes.HOME_ROUTE
            ),
            spacing="5",
            justify="center",
            align = 'center',
            min_height="85vh",
            id = 'child_id'
        )
    
    return base_page(      
            child)
    
@reflex_local_auth.require_login
def blog_post_add_page() -> rx.Component:
    my_form = forms.blog_post_add_form()
    my_child = rx.vstack(
            rx.heading("New Blog Post", size="9"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width='50vw'
                )
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    width='75vw'
                )
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    width='95vw'
                )
            ),
            spacing="5",
            align="center",
            min_height="95vh",
        )
    return base_page(my_child)