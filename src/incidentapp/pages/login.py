import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from incidentapp.pages.report import build_report_page
from incidentapp.network import login_to_api
import asyncio


def build_login_page(app):
    # Login screen widgets
    label = toga.Label("Login Page", style=Pack(padding=10))
    username_input = toga.TextInput(placeholder="Enter your username", style=Pack(padding=10))
    password_input = toga.PasswordInput(placeholder="Enter your password", style=Pack(padding=10))
    status_label = toga.Label("", style=Pack(padding=10))  # Placeholder for status messages

    # Login button
    login_button = toga.Button(
        "Login",
        on_press=lambda widget: asyncio.create_task(handle_login(app, username_input, password_input, status_label)),
        style=Pack(padding=10)
    )

    # Back button
    back_button = toga.Button("Back to Home", on_press=app.go_to_home_screen, style=Pack(padding=10))

    # Login screen layout
    box = toga.Box(style=Pack(direction=COLUMN, padding=10))
    box.add(label)
    box.add(username_input)
    box.add(password_input)
    box.add(status_label)  # Add the status label to the layout
    box.add(login_button)
    box.add(back_button)

    return box


async def handle_login(app, username_input, password_input, status_label):
    """
    Handles the login process by calling the API and navigating to the next page on success.
    Displays a loading message and handles errors.
    """
    # Show loading message
    status_label.text = "Logging in..."
    await asyncio.sleep(0.1)  # Allow UI to update before login starts

    # Perform login
    success, response = login_to_api(username_input.value, password_input.value)

    if success:
        # Login succeeded
        app.logged_in_username = username_input.value  # Store the username
        app.logged_in_password = password_input.value  # Store the password
        app.main_window.content = build_report_page(app)  # Navigate to the report page
    else:
        # Login failed; show error message
        status_label.text = f"Login failed: {response}"
