import reflex as rx
import reflex_local_auth

import sqlmodel
from .. import navigation

from ..models import UserInfo


class SessionState(reflex_local_auth.LocalAuthState):
    
    @rx.var(cache=True)
    def my_user_id(self) -> int | None:
        """_summary_
            if user is authenticated, retruns user ID as variable
        Returns:
            int | None: user ID or None
        """        
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.id 
    
    @rx.var(cache=True)
    def authenticated_username(self) -> str | None:
        """_summary_
            if user is authenticated, retruns username as variable
        Returns:
            str | None: username or None
        """        
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.username        

    @rx.var(cache=True)
    def authenticated_user_info(self) -> UserInfo | None:
        """_summary_
            return an instance of UserInfo(a table from dataabase) as a variable
        Returns:
            UserInfo | None: instance of The UserInfo | None
        """        
        if self.authenticated_user.id < 0:
            return None
        try:
            with rx.session() as session:
                result = session.exec(
                    sqlmodel.select(UserInfo).where(
                        UserInfo.user_id == self.authenticated_user.id
                    ), #compares an user-id from database with authenticated user IDs
                ).one_or_none()
                if result is None:
                    return None
                return result
            
        except Exception as e:
            print(f'an error occured:\n {e}')
            return None
            
    def on_load(self):
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        print(self.is_authenticated)
        print(self.authenticated_user_info)
        
    def my_logout(self):
        self.do_logout()
        return rx.redirect(navigation.routes.HOME_ROUTE)


class MyRegisterState(reflex_local_auth.RegistrationState):
    
    def handle_registrations(self, form_data:dict) -> int:
        """_summary_
            depacks the registrations data from form and creates username, password and user_id
        Args:
            form_data (dictionary): data from registration form

        Returns:
            int: users ID
        """        
        username = form_data["username"]
        password = form_data["password"]
        validation_errors = self._validate_fields(
            username, password, form_data["confirm_password"]
        )
        if validation_errors:
            self.new_user_id = -1
            return validation_errors
        self._register_user(username, password)
        return self.new_user_id
    
    def handle_registration_email(self, form_data:dict):
        """_summary_
           depacks the registrations data from form and registers email 
        Args:
            form_data (dictionary): data from registration form

        """ 
        new_user_id = self.handle_registrations(form_data)
        if new_user_id >= 0:
            with rx.session() as session:
                session.add(
                    UserInfo(
                        email=form_data["email"],
                        user_id=self.new_user_id,
                    )
                )# fills email and user_id fields with form values
                session.commit()
        return type(self).successful_registration
