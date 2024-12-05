import reflex as rx


class State(rx.State):
    """Estado global de la aplicación."""
    usuario_actual: str = ""
    carrito: list[dict] = []

    def iniciar_sesion(self, email: str):
        """Inicia sesión del usuario."""
        self.usuario_actual = email
        return rx.redirect("/home")

    def agregar_al_carrito(self, producto: dict):
        """Agrega un producto al carrito."""
        self.carrito.append(producto)

    def eliminar_del_carrito(self, producto: dict):
        """Elimina un producto del carrito."""
        self.carrito.remove(producto)


# Importar las páginas
from .pages.inicio import login_page
from .pages.home import home_page
from .pages.cart import cart_page

# Configurar la aplicación
app = rx.App(state=State)
app.add_page(login_page, route="/", title="Iniciar Sesión")
app.add_page(home_page, route="/home", title="Productos de Temporada")
app.add_page(cart_page, route="/cart", title="Carrito de Compras")
app.compile()
