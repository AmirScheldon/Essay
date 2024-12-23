import reflex as rx
import reflex_local_auth

import sqlmodel
from .. import navigation

from ..models import UserInfo


class SessionState(reflex_local_auth.LocalAuthState):
    
    @rx.var(cache=True)
    def authenticated_username(self) -> str | None:
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.username        

    @rx.var(cache=True)
    def authenticated_user_info(self) -> UserInfo | None:
        if self.authenticated_user.id < 0:
            return None
        try:
            with rx.session() as session:
                result = session.exec(
                    sqlmodel.select(UserInfo).where(
                        UserInfo.user_id == self.authenticated_user.id
                    ),
                ).one_or_none()
                if result is None:
                    return None
                print(result)
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
    
    def handle_registrations(self, form_data):
        username = form_data["username"]
        password = form_data["password"]
        validation_errors = self._validate_fields(
            username, password, form_data["confirm_password"]
        )
        if validation_errors:
            self.new_user_id = -1
            print('smt')
            return validation_errors
        self._register_user(username, password)
        return self.new_user_id
    
    def handle_registration_email(self, form_data):
        new_user_id = self.handle_registrations(form_data)
        if new_user_id >= 0:
            with rx.session() as session:
                session.add(
                    UserInfo(
                        email=form_data["email"],
                        user_id=self.new_user_id,
                    )
                )
                session.commit()
        return type(self).successful_registration
