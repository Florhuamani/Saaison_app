import reflex as rx
from Saison_app import State


def login_page():
    """Manejador para el botón de iniciar sesión."""
    email = rx.get("email")
    return State().iniciar_sesion(email)


def login_page():
    """Página de inicio de sesión."""
    return rx.center(
        rx.vstack(
            rx.heading("Iniciar Sesión", size="xl"),
            rx.input(placeholder="Correo Electrónico", id="email"),
            rx.button(
                "Ingresar",
                color="white",
                bg="beige",
                on_click=login_page,
            ),
            spacing=4,
        ),
        min_height="100vh",
    )
