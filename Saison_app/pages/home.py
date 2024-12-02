import reflex as rx
from Saison_app import State 

def home_page() -> rx.Component:
    """Página principal que muestra productos."""
    productos = [
        {"nombre": "Disfraz de vampiro", "precio":"s/.20", "imagen": ""},
        {"nombre": "Calabaza decorativa", "precio":"s/.25", "imagen": ""},
                ]
    return rx.box(
        rx.heading("Productos de Temporada", size="1"),
        rx.grid([
            rx.box(
                rx.image(src=producto[""],
                         alt=producto[""],),
                         rx.text(producto[""]),
                         rx.text(producto[""]),

                         rx.button("Agregar al carrito",
                                   on_click=lambda p=producto:
                                   State.agregar_al_carrito(p),
                ),
                    ),
                    for producto in productos
                ],
                template_columns="repeat(3,1fr)",
                gap=4,
        ),
        pading="5",
    )