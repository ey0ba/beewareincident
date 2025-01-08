import toga
from incidentapp.pages.home import build_home_page
from incidentapp.pages.login import build_login_page
from incidentapp.pages.report import build_report_page
from incidentapp.pages.form import build_form_page




class IncidentApp(toga.App):
    def startup(self):
        # Create the main application window
        self.main_window = toga.MainWindow(title="Incident App")

        # Build the home screen
        self.main_window.content = build_home_page(self)

        # Show the window
        self.main_window.show()

    # Navigation methods
    def go_to_home_screen(self, widget):
        self.main_window.content = build_home_page(self)

    def go_to_login_screen(self, widget):
        self.main_window.content = build_login_page(self)

    def go_to_report_screen(self, widget):
        self.main_window.content = build_report_page(self)

    def go_to_form_screen(self, widget):
        self.main_window.content = build_form_page(self)

    # Submit form method
    def submit_form(self, widget):
        print(f"Name: {self.name_input.value}")
        print(f"Description: {self.description_input.value}")
        print("Form submitted!")


def main():
    return IncidentApp()


if __name__ == "__main__":
    main().main_loop()
