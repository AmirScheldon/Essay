import reflex as rx
from .. import navigations


class StateNav(rx.State):
    def to_home(self):
        return rx.redirect(navigations.routes.HOME_ROUTE)
    def to_about_us(self):
        return rx.redirect(navigations.routes.ABOUT_US_ROUTE)
    def to_contact(self):
        return rx.redirect(navigations.routes.CONTACT_ROUTE)    
    def to_pricing(self):
        return rx.redirect(navigations.routes.PRICING_ROUTE)
