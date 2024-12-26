from datetime import datetime
from typing import Optional, List
import reflex as rx 

import sqlalchemy
from sqlmodel import select

from .. import navigation
from ..auth.state import SessionState
from ..models import BlogPostModel, UserInfo

ARTICLE_LIST_ROUTE = navigation.routes.ARTICLE_LIST_ROUTE
if ARTICLE_LIST_ROUTE.endswith("/"): # If a user enters a URL with a '/' at the end
    ARTICLE_LIST_ROUTE = ARTICLE_LIST_ROUTE[:-1] # removes '/' from the URL

class ArticlePublicState(SessionState):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None
    post_content: str = ""
    post_publish_active: bool = False
    limit: int = 20

        
    @rx.var
    def dynamic_post_id(self) -> int :
        """_summary_
            returns ID of a post as a variable
        """        
        return self.router.page.params.get("post_id", "")

    @rx.var
    def post_url(self):
        """_summary_
            Returns a URL based on the post's ID as a variable.
        """   
        if not self.post:
            return f"{ARTICLE_LIST_ROUTE}"
        return f"{ARTICLE_LIST_ROUTE}/{self.post.id}"

    def get_post_detail(self):
        """_summary_
            returns post based of the written query.
        """        
        lookups = (
            (BlogPostModel.publish_active == True) &
            (BlogPostModel.publish_date < datetime.now()) &
            (BlogPostModel.id == self.dynamic_post_id)
        )
        with rx.session() as session:
            if self.post_id == "":
                self.post = None
                self.post_content = ""
                self.post_publish_active = False
                return
            sql_statement = select(BlogPostModel).options(
                sqlalchemy.orm.joinedload(BlogPostModel.userinfo).joinedload(UserInfo.user)
            ).where(lookups) 
            result = session.exec(sql_statement).one_or_none()
            self.post = result
            if result is None:
                self.post_content = ""
                return
            self.post_content = self.post.content # sets content of post
            self.post_publish_active = self.post.publish_active # sets published status

    def set_limit_and_reload(self, new_limit: int=5):
        """_summary_
            sets a limitation on the number of posts loaded per page.
        """        
        self.limit = new_limit
        self.load_posts()
        yield

    def load_posts(self, *args, **kwargs):
        lookup_args = ( 
            (BlogPostModel.publish_active == True) &
            (BlogPostModel.publish_date < datetime.now())
        )
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel).options(
                    sqlalchemy.orm.joinedload(BlogPostModel.userinfo)
                ).where(lookup_args).limit(self.limit)
            ).all() # Loads a limited number of published posts. 
            self.posts = result
    
    def to_post(self):
        if not self.post:
            return rx.redirect(ARTICLE_LIST_ROUTE)
        return rx.redirect(f"{self.post_url}")