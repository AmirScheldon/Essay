import reflex as rx
import asyncio
from .model import ContactDataModel
from sqlmodel import select
from typing import List

class ContactState(rx.State):
    form_data: dict = {}
    submitted: bool = False
    enteries: List['ContactDataModel']  = []
    
    def contact_list_entries(self):
        with rx.session() as session:
            enteries = session.exec(select(ContactDataModel)).all()
            self.enteries = enteries
        
        
    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get('first_name')
        return f'Thank You {first_name}!' 
    
    # @rx.event
    async def submit_handler(self, form_data: dict):
        self.form_data = form_data
        data: dict ={}
        for k,v in form_data.items():
            if v == '' or v is None:
                continue
            data[k] = v
        with rx.session() as session:
            db_entery = ContactDataModel(
                **data
            )
            session.add(db_entery)
            session.commit()
            
            self.submitted = True
            yield
        await asyncio.sleep(3)
        self.submitted = False