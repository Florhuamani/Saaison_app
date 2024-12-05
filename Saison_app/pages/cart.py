import reflex as rx
from Saison_app import State


def handle_remove_from_cart(producto):
    """Manejador para eliminar del carrito."""
    return State().eliminar_del_carrito(producto)


def cart_page():
    """Página del carrito."""
    return rx.center(
        rx.vstack(
            rx.heading("Carrito de Compras", size="xl"),
            rx.foreach(
                State().carrito,
                lambda producto: rx.hstack(
                    rx.text(producto["nombre"]),
                    rx.text(producto["precio"]),
                    rx.button(
                        "Eliminar",
                        on_click=lambda p=producto: handle_remove_from_cart(p),
                    ),
                ),
            ),
            rx.button("Proceder al Pago", bg="beige", color="white"),
            spacing=4,
        ),
    )
