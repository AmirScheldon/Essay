import reflex as rx
from .state import BlogAddPostFormState

def blog_create_post_form() -> rx.Component:
    return rx.vstack(
                rx.form(
                    rx.vstack(
                        rx.hstack(
                            rx.input(
                                type='text',
                                name="title",
                                placeholder="Title",
                                required= True
                            ),
                        ),
                        rx.text_area(
                            type='text',
                            name= 'content',
                            placeholder= 'Enter a text',
                            required= True,
                            width = '100%',
                            height='50vh'
                        ),
                        rx.button("Submit", type="submit"),
                        align='center',
                    ),
                    on_submit=BlogAddPostFormState.submit_handler,
                    reset_on_submit=True,
                ),
            )