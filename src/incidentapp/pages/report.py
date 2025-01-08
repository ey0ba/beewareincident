import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from incidentapp.network import fetch_dropdown_data
from incidentapp.pages.form import build_form_page


def build_report_page(app):
    # Report screen widgets
    label = toga.Label("Report Incident Page", style=Pack(padding=10))
    report_button = toga.Button("Report", on_press=lambda widget: handle_report(app), style=Pack(padding=10))
    logout_button = toga.Button("Logout", on_press=app.go_to_home_screen, style=Pack(padding=10))

    # Report screen layout
    box = toga.Box(style=Pack(direction=COLUMN, padding=10))
    box.add(label)
    box.add(report_button)
    box.add(logout_button)

    return box


def handle_report(app):
    """
    Handles the report button action by calling the dropdown API.
    If the API call succeeds, navigate to the form page.
    """
    username = app.logged_in_username  # Get the logged-in user's username
    password = app.logged_in_password  # Get the logged-in user's password

    success, response = fetch_dropdown_data(username, password)
    if success:
        print("Dropdown data fetched successfully!")
        app.dropdown_data = response  # Store the dropdown data in the app instance
        app.main_window.content = build_form_page(app)  # Navigate to the Form Page
    else:
        print(f"Failed to fetch dropdown data: {response}")
        toga.Dialog.info("Error", f"Failed to fetch dropdown data: {response}")
        
        
