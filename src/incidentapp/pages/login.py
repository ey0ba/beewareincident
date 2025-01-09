import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from incidentapp.pages.report import build_report_page

from incidentapp.network import login_to_api




def build_login_page(app):
    # Login screen widgets
    label = toga.Label("Login Page", style=Pack(padding=10))
    username_input = toga.TextInput(placeholder="Enter your username", style=Pack(padding=10))
    password_input = toga.PasswordInput(placeholder="Enter your password", style=Pack(padding=10))
    login_button = toga.Button(
        "Login",
        on_press=lambda widget: handle_login(app, username_input.value, password_input.value),
        style=Pack(padding=10)
    )
    back_button = toga.Button("Back to Home", on_press=app.go_to_home_screen, style=Pack(padding=10))

    # Login screen layout
    box = toga.Box(style=Pack(direction=COLUMN, padding=10))
    box.add(label)
    box.add(username_input)
    box.add(password_input)
    box.add(login_button)
    box.add(back_button)

    return box


        
def handle_login(app, username, password):
    """
    Handles the login process by calling the API and navigating to the next page on success.
    """
    success, response = login_to_api(username, password)
    if success:
        print("Login successful!")
        app.logged_in_username = username  # Store the username
        app.logged_in_password = password  # Store the password
        app.main_window.content = build_report_page(app)  # Navigate to Report Page
    else:
        print(f"Login failed: {response}")
        toga.dialogs.info("Login Failed", response)  # Correct usage of dialogs.info
