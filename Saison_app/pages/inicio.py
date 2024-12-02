import reflex as rx
from Saison_app import State

def inicio() -> rx.Component:
    "Página de inicio de sesión"
    return rx.center(
        rx.vstack(
            rx.heading("Iniciar sesión",size="2x1"),
            rx.input(
                placeholder="Correo electrónico", on_change=lambda
                value : setattr(State,"email", value),
                ),
                rx.input(
                    placeholder="Contraseña",
                    type="Password", on_change=lambda 
                    value:setattr(State,"password",value),
                ),
                rx.button("Iniciar Sesión",
                          on_click=State.inicio,
                          color_scheme="blue",
                          ),
                          spacing="4",
        ),
        min_height="100vh",
    )
