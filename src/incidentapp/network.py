
import requests
from incidentapp.config import API_URLS, HEADERS



def login_to_api(username, password):
    """
    Sends a POST request to the login API with the given username and password.
    """
    api_url = API_URLS["kivy-login"]
    payload = {"username": username, "password": password}

    try:
        response = requests.post(api_url, json=payload, headers=HEADERS)
        if response.status_code == 200:
            # Successful login
            return True, response.json()
        else:
            # Login failed; return the error message
            return False, response.json().get("detail", response.text)
    except requests.exceptions.RequestException as e:
        # Handle network or API errors
        return False, f"Network error: {str(e)}"
    
    
    
def fetch_dropdown_data(username, password):
    """
    Sends a POST request to fetch the dropdown data using the provided credentials.
    """
    api_url = API_URLS["dropdown_data"]
    payload = {"username": username, "password": password}

    try:
        response = requests.post(api_url, json=payload, headers=HEADERS)
        if response.status_code == 200:
            # Return success status and response data
            return True, response.json()
        else:
            # Return failure status and error message
            return False, response.text
    except requests.exceptions.RequestException as e:
        # Handle network or API errors
        return False, f"Network error: {str(e)}"    

    
    
def submit_incident(form_data, username, password):
    """
    Sends a POST request to submit the incident report.
    """
    api_url = API_URLS["submit_incident"]
    payload = {
        "username": username,
        "password": password,
        **form_data  # Merge form data into the payload
    }

    try:
        response = requests.post(api_url, json=payload, headers=HEADERS)
        print(f"DEBUG: Status Code={response.status_code}, Response={response.text}")
        
        if response.status_code in [200, 201]:  # Treat 200 and 201 as success
            # Submission successful
            return True, response.json().get("message", "Submission succeeded!")
        else:
            # Submission failed
            return False, response.json().get("message", response.text)
    except requests.exceptions.RequestException as e:
        # Handle network or API errors
        return False, f"Network error: {str(e)}"
    
    
    
# def handle_submit(app, form_data, reset_form_callback):
#     """
#     Handles the form submission by sending data to the backend API.
#     If successful, displays a success message and clears the form.
#     If failed, displays an error message.
#     """
#     # Call the submit API
#     success, message = submit_incident(form_data, app.logged_in_username, app.logged_in_password)

#     # Debug print
#     print(f"DEBUG: Success={success}, Message={message}")

#     if success:
#         app.main_window.info_dialog("Success", message)  # Use synchronous info_dialog
#         reset_form_callback()  # Reset the form fields
#     else:
#         app.main_window.info_dialog("Error", message)  # Use synchronous info_dialog

    
def handle_submit(app, form_data, reset_form_callback):
    """
    Handles the form submission by sending data to the backend API.
    If successful, displays a success message and clears the form.
    If failed, displays an error message.
    """
    # Call the submit API
    success, message = submit_incident(form_data, app.logged_in_username, app.logged_in_password)

    # Debug print
    print(f"DEBUG: Success={success}, Message={message}")

    if success:
        app.main_window.info_dialog("Success", message)  # Use synchronous info_dialog
        reset_form_callback()  # Reset the form fields
    else:
        app.main_window.info_dialog("Error", message)  # Use synchronous info_dialog


