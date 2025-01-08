import toga
from toga.style import Pack
from toga.style.pack import COLUMN


def build_home_page(app):
    # Home screen widgets
    label = toga.Label("Welcome to the Incident App!", style=Pack(padding=10))
    login_button = toga.Button(
        "Login",
        on_press=app.go_to_login_screen,
        style=Pack(padding=10)
    )

    # Home screen layout
    box = toga.Box(style=Pack(direction=COLUMN, padding=10))
    box.add(label)
    box.add(login_button)

    return box
