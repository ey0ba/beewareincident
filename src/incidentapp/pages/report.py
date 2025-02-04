import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT
from incidentapp.network import fetch_dropdown_data
from incidentapp.pages.form import build_form_page


def build_report_page(app):
    # Header with Logout Button (Left-aligned)
    header_box = toga.Box(style=Pack(direction=ROW, padding=10, alignment=LEFT))
    logout_button = toga.Button("Logout", on_press=app.go_to_home_screen, style=Pack(padding=10))
    header_box.add(logout_button)

    # Main content - Report screen widgets
    label = toga.Label("Report Incident Page", style=Pack(padding=10))
    report_button = toga.Button("Report", on_press=lambda widget: handle_report(app), style=Pack(padding=10))

    # Add Report Button in a separate Box
    button_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
    button_box.add(report_button)

    # Wrap the content in a ScrollContainer
    scrollable_content = toga.Box(style=Pack(direction=COLUMN, padding=10))
    scrollable_content.add(header_box)  # Add header first (Logout Button on the left)
    scrollable_content.add(label)
    scrollable_content.add(button_box)

    scroll_container = toga.ScrollContainer(content=scrollable_content)

    return scroll_container


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
        toga.dialogs.info("Error", f"Failed to fetch dropdown data: {response}")





# import toga
# from toga.style import Pack
# from toga.style.pack import COLUMN, ROW, LEFT
# from incidentapp.network import fetch_dropdown_data
# from incidentapp.pages.form import build_form_page


# def build_report_page(app):
#     # Header with Logout Button
#     header_box = toga.Box(style=Pack(direction=ROW, padding=10, alignment=LEFT))
#     logout_button = toga.Button("Logout", on_press=app.go_to_home_screen, style=Pack(padding=10))
#     header_box.add(logout_button)

#     # Main content - Report screen widgets
#     label = toga.Label("Report Incident Page", style=Pack(padding=10))
#     report_button = toga.Button("Report", on_press=lambda widget: handle_report(app), style=Pack(padding=10))

#     # Add Report Button in a separate Box
#     button_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
#     button_box.add(report_button)

#     # Wrap the content in a ScrollContainer
#     scrollable_content = toga.Box(style=Pack(direction=COLUMN, padding=10))
#     scrollable_content.add(header_box)  # Add header first (Logout Button at the top)
#     scrollable_content.add(label)
#     scrollable_content.add(button_box)

#     scroll_container = toga.ScrollContainer(content=scrollable_content)

#     return scroll_container


# def handle_report(app):
#     """
#     Handles the report button action by calling the dropdown API.
#     If the API call succeeds, navigate to the form page.
#     """
#     username = app.logged_in_username  # Get the logged-in user's username
#     password = app.logged_in_password  # Get the logged-in user's password

#     success, response = fetch_dropdown_data(username, password)
#     if success:
#         print("Dropdown data fetched successfully!")
#         app.dropdown_data = response  # Store the dropdown data in the app instance
#         app.main_window.content = build_form_page(app)  # Navigate to the Form Page
#     else:
#         print(f"Failed to fetch dropdown data: {response}")
#         toga.dialogs.info("Error", f"Failed to fetch dropdown data: {response}")







# import toga
# from toga.style import Pack
# from toga.style.pack import COLUMN
# from incidentapp.network import fetch_dropdown_data
# from incidentapp.pages.form import build_form_page


# def build_report_page(app):
#     # Report screen widgets
#     label = toga.Label("Report Incident Page", style=Pack(padding=10))
#     report_button = toga.Button("Report", on_press=lambda widget: handle_report(app), style=Pack(padding=10))
#     logout_button = toga.Button("Logout", on_press=app.go_to_home_screen, style=Pack(padding=10))

#     # Add buttons to a Box
#     button_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
#     button_box.add(report_button)
#     button_box.add(logout_button)

#     # Wrap the content in a ScrollContainer
#     scrollable_content = toga.Box(style=Pack(direction=COLUMN, padding=10))
#     scrollable_content.add(label)
#     scrollable_content.add(button_box)

#     scroll_container = toga.ScrollContainer(content=scrollable_content)

#     return scroll_container


# def handle_report(app):
#     """
#     Handles the report button action by calling the dropdown API.
#     If the API call succeeds, navigate to the form page.
#     """
#     username = app.logged_in_username  # Get the logged-in user's username
#     password = app.logged_in_password  # Get the logged-in user's password

#     success, response = fetch_dropdown_data(username, password)
#     if success:
#         print("Dropdown data fetched successfully!")
#         app.dropdown_data = response  # Store the dropdown data in the app instance
#         app.main_window.content = build_form_page(app)  # Navigate to the Form Page
#     else:
#         print(f"Failed to fetch dropdown data: {response}")
#         toga.dialogs.info("Error", f"Failed to fetch dropdown data: {response}")
