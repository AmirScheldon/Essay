import reflex as rx 
from..auth.state import  SessionState

from .state import (
    BlogAddPostFormState,
    BlogEditFormState
)


def blog_post_add_form() -> rx.Component:
    username = SessionState.authenticated_username
    return rx.form(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.text_area(
                            name='author',
                            value= username, # takes(autofill) and sends the username
                            required=True,
                            type='hidden',
                        ),
                        display='none'
                    ),
                    rx.input(
                        name="title",
                        placeholder="Title",
                        required=True,
                        type='text',
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.text_area(
                    name='content',
                    placeholder="Your message",
                    required=True,
                    height='50vh',
                    width='100%',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=BlogAddPostFormState.handle_submit,
            reset_on_submit=True,
    )




def blog_post_edit_form() -> rx.Component:
    post = BlogEditFormState.post
    title = post.title
    post_content = BlogEditFormState.post_content
    return rx.form(
            rx.box(
                rx.input(
                    type='hidden',
                    name='blog_post_id',
                    value=post.id
                ),
                display='none'
            ), 
            rx.vstack(
                rx.hstack(
                    rx.input(
                        default_value=title,
                        name="title",
                        placeholder="Title",
                        required=True,
                        type='text',
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.text_area(
                    value = post_content,
                    on_change = BlogEditFormState.set_post_content,
                    name='content',
                    placeholder="Your message",
                    required=True,
                    height='50vh',
                    width='100%',
                ),
                rx.flex(
                    rx.switch(
                        default_checked=BlogEditFormState.post_publish_active,
                        on_change=BlogEditFormState.set_post_publish_active,
                        name='publish_active',          
                    ),
                    rx.text("Publish Active"),
                    spacing="2",
                ),
                rx.cond(
                    BlogEditFormState.post_publish_active, # if rx.switch is post_publish_active(=True)
                    rx.box(
                        rx.hstack(
                            rx.input(
                                default_value=BlogEditFormState.publish_display_date,
                                type='date',
                                name='publish_date',
                                width='100%'
                            ),
                            rx.input(
                                default_value=BlogEditFormState.publish_display_time,
                                type='time',
                                 name='publish_time',
                                width='100%'
                            ),
                        width='100%'
                        ),
                        width='100%'
                    )
                ),# The user can set a time to publish their post.
                rx.button("Submit", type="submit"),
            ),# else just submit the post
            on_submit=BlogEditFormState.handle_submit,
    )