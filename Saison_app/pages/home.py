import reflex as rx
from Saison_app import State


def handle_add_to_cart(producto):
    """Manejador para agregar al carrito."""
    return State().agregar_al_carrito(producto)


def home_page():
    """Página principal de productos."""
    productos = [
        {"nombre": "Disfraz de Vampiro", "precio": "$20", "imagen": "resources/vampiro.jpg"},
        {"nombre": "Calabaza Decorativa", "precio": "$10", "imagen": "resources/calabaza.jpg"},
        {"nombre": "Sombrero de Bruja", "precio": "$15", "imagen": "resources/sombrero.jpg"},
    ]

    return rx.box(
        rx.heading("Productos de Temporada", size="xl"),
        rx.grid(
            [
                rx.box(
                    rx.image(src=producto["imagen"], alt=producto["nombre"]),
                    rx.text(producto["nombre"]),
                    rx.text(producto["precio"]),
                    rx.button(
                        "Agregar al Carrito",
                        on_click=lambda p=producto: handle_add_to_cart(p),
                    ),
                )
                for producto in productos
            ],
            template_columns="repeat(3, 1fr)",
            gap=4,
        ),
        padding="5",
    )
