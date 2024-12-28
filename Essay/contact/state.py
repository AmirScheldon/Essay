from typing import List
import asyncio
import reflex as rx 

from sqlmodel import select
import sqlalchemy

from ..auth.state import SessionState
from ..models import ContactEntryModel

class ContactState(SessionState):
    form_data: dict = {}
    entries: List['ContactEntryModel'] = []
    did_submit: bool = False

    @rx.var
    def thank_you(self):
        # returns a  thank_you message after the user sends a message
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + "!"

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v
        print('contact data', data),
        print('user_id', self.my_user_id),
        if self.my_user_id is not None:
            data['user_id'] = self.my_user_id   
        with rx.session() as session:
            # depack the data(from form) and save it on database
            db_entry = ContactEntryModel(
                **data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield

    def list_entries(self):
        with rx.session() as session:
            # retrieves all contacts form database
            entries = session.exec(
                select(ContactEntryModel).options(
                    sqlalchemy.orm.joinedload(ContactEntryModel.userinfo)
                     ).where(ContactEntryModel.user_id == self.my_user_id) 
            ).all()
            self.entries = entries