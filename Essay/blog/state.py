import reflex as rx
from typing import List, Optional
from .model import BlogPostModel
from sqlmodel import select



class BLogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None
    
    def load_posts(self):
        with rx.session() as session:
            result =  session.exec(select(BlogPostModel)).all()
            self.posts = result
            
    def create_post(self, form_data: dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            session.add(post)
            session.commit()
            session.refresh(post)
            self.post = post
            

class BlogAddPostFormState(BLogPostState):
    form_data: dict = {}
    
    def submit_handler(self, form_data: dict):
        self.form_data = form_data
        self.create_post(form_data)