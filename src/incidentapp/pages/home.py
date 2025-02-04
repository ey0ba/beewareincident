import toga
from toga.style import Pack
from toga.style.pack import COLUMN


def build_home_page(app):
    # Home screen widgets
    title = toga.Label("Incident Reporting System", style=Pack(padding=(0, 0, 20, 0), font_size=24, text_align='center'))
    label = toga.Label("Welcome to the Incident App!", style=Pack(padding=10, font_size=18, text_align='center'))
    login_button = toga.Button(
        "Login",
        on_press=app.go_to_login_screen,
        style=Pack(padding=10, width=200, alignment='center')
    )

    # Home screen layout
    box = toga.Box(style=Pack(direction=COLUMN, padding=10, alignment='center'))
    box.add(title)
    box.add(label)
    box.add(login_button)

    return box
