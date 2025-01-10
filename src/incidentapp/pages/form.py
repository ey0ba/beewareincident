from datetime import datetime
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from incidentapp.network import handle_submit



def build_form_page(app):
    """
    Builds the form page using dropdown data fetched from the API.
    """
    dropdown_data = app.dropdown_data or {}

    # Map dropdown data to include PK values
    departments = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("departments", [])]
    reporter_departments = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("reporter_departments", [])]
    suspected_causes = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("suspected_causes", [])]
    contributing_factors = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("contributing_factors", [])]
    mitigating_factors = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("mitigating_factors", [])]
    incident_types = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("incident_types", [])]
    incident_outcomes = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("incident_outcomes", [])]
    resulting_actions = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("resulting_actions", [])]
    reporter_roles = [{"id": item["id"], "name": item["name"]} for item in dropdown_data.get("reporter_roles", [])]
    sex_choices = ["Select Sex", "Male", "Female"]

    # Add default options for dropdowns
    departments.insert(0, {"id": None, "name": "Select Department"})
    reporter_departments.insert(0, {"id": None, "name": "Select Reporter Department"})
    suspected_causes.insert(0, {"id": None, "name": "Select Suspected Cause"})
    contributing_factors.insert(0, {"id": None, "name": "Select Contributing Factor"})
    mitigating_factors.insert(0, {"id": None, "name": "Select Mitigating Factor"})
    incident_types.insert(0, {"id": None, "name": "Select Incident Type"})
    incident_outcomes.insert(0, {"id": None, "name": "Select Incident Outcome"})
    resulting_actions.insert(0, {"id": None, "name": "Select Resulting Action"})
    reporter_roles.insert(0, {"id": None, "name": "Select Reporter Role"})

    # Default incident time
    default_incident_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create widgets
    incident_time_input = toga.TextInput(value=default_incident_time, readonly=True, style=Pack(padding=10))
    age_input = toga.TextInput(placeholder="Age", style=Pack(padding=10))
    sex_dropdown = toga.Selection(items=sex_choices, style=Pack(padding=10))
    department_dropdown = toga.Selection(items=[item["name"] for item in departments], style=Pack(padding=10))
    reporter_department_dropdown = toga.Selection(items=[item["name"] for item in reporter_departments], style=Pack(padding=10))
    suspected_cause_dropdown = toga.Selection(items=[item["name"] for item in suspected_causes], style=Pack(padding=10))
    suspected_cause_other_input = toga.TextInput(placeholder="Other Suspected Causes", style=Pack(padding=10))
    contributing_factor_dropdown = toga.Selection(items=[item["name"] for item in contributing_factors], style=Pack(padding=10))
    contributing_factor_other_input = toga.TextInput(placeholder="Other Contributing Factors", style=Pack(padding=10))
    mitigating_factor_dropdown = toga.Selection(items=[item["name"] for item in mitigating_factors], style=Pack(padding=10))
    mitigating_factor_other_input = toga.TextInput(placeholder="Other Mitigating Factors", style=Pack(padding=10))
    incident_type_dropdown = toga.Selection(items=[item["name"] for item in incident_types], style=Pack(padding=10))
    incident_outcome_dropdown = toga.Selection(items=[item["name"] for item in incident_outcomes], style=Pack(padding=10))
    resulting_action_dropdown = toga.Selection(items=[item["name"] for item in resulting_actions], style=Pack(padding=10))
    reporter_role_dropdown = toga.Selection(items=[item["name"] for item in reporter_roles], style=Pack(padding=10))
    reporter_name_input = toga.TextInput(placeholder="Reporter Name", style=Pack(padding=10))
    other_opinions_input = toga.TextInput(placeholder="Other Opinions", style=Pack(padding=10))
    

    def reset_form():
        """
        Resets all form fields to their initial state.
        """
        incident_time_input.value = default_incident_time
        age_input.value = ""
        sex_dropdown.value = "Select Sex"
        department_dropdown.value = "Select Department"
        reporter_department_dropdown.value = "Select Reporter Department"
        suspected_cause_dropdown.value = "Select Suspected Cause"
        suspected_cause_other_input.value = ""
        contributing_factor_dropdown.value = "Select Contributing Factor"
        contributing_factor_other_input.value = ""
        mitigating_factor_dropdown.value = "Select Mitigating Factor"
        mitigating_factor_other_input.value = ""
        incident_type_dropdown.value = "Select Incident Type"
        incident_outcome_dropdown.value = "Select Incident Outcome"
        resulting_action_dropdown.value = "Select Resulting Action"
        reporter_role_dropdown.value = "Select Reporter Role"
        reporter_name_input.value = ""
        other_opinions_input.value = ""
        

    # Submit button
    submit_button = toga.Button(
        "Submit",
        on_press=lambda widget: handle_submit(
            app,
            {
                "incident_time": incident_time_input.value,
                "age": age_input.value,
                "sex": sex_dropdown.value,
                "incident_locations": get_selected_pk(department_dropdown, departments),
                "reporter_department": get_selected_pk(reporter_department_dropdown, reporter_departments),
                "suspected_cause": get_selected_pk(suspected_cause_dropdown, suspected_causes),
                "suspected_cause_other": suspected_cause_other_input.value,
                "contributing_factor": get_selected_pk(contributing_factor_dropdown, contributing_factors),
                "contributing_factor_other": contributing_factor_other_input.value,
                "mitigating_factor": get_selected_pk(mitigating_factor_dropdown, mitigating_factors),
                "mitigating_factor_other": mitigating_factor_other_input.value,
                "incident_type": get_selected_pk(incident_type_dropdown, incident_types),
                "incident_outcome": get_selected_pk(incident_outcome_dropdown, incident_outcomes),
                "resulting_action": get_selected_pk(resulting_action_dropdown, resulting_actions),
                "reporter_name": reporter_name_input.value,
                "reporter_role": get_selected_pk(reporter_role_dropdown, reporter_roles),
                "other_opinions": other_opinions_input.value,
            },
            reset_form  # Pass reset_form as a callback
        ),
        style=Pack(padding=10),
    )

    # Back button
    back_button = toga.Button("Back to Report Page", on_press=app.go_to_report_screen, style=Pack(padding=10))

    # Layout
    form_box = toga.Box(style=Pack(direction=COLUMN, padding=10))  # Define `form_box`
    form_box.add(incident_time_input)
    form_box.add(age_input)
    form_box.add(sex_dropdown)
    form_box.add(department_dropdown)
    form_box.add(reporter_department_dropdown)
    form_box.add(suspected_cause_dropdown)
    form_box.add(suspected_cause_other_input)
    form_box.add(contributing_factor_dropdown)
    form_box.add(contributing_factor_other_input)
    form_box.add(mitigating_factor_dropdown)
    form_box.add(mitigating_factor_other_input)
    form_box.add(incident_type_dropdown)
    form_box.add(incident_outcome_dropdown)
    form_box.add(resulting_action_dropdown)
    form_box.add(reporter_role_dropdown)
    form_box.add(reporter_name_input)
    form_box.add(other_opinions_input)
    form_box.add(submit_button)
    form_box.add(back_button)

    # Wrap in ScrollContainer
    scroll_container = toga.ScrollContainer(content=form_box)

    return scroll_container


def get_selected_pk(selection_widget, data_list):
    """
    Retrieves the primary key (PK) for the selected dropdown value.
    """
    selected_name = selection_widget.value
    for item in data_list:
        if item["name"] == selected_name:
            return item["id"]
    return None  # Return None if no match is found
