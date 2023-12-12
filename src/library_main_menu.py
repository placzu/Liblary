from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header, Static


class LibraryMenuApp(App):
    CSS_PATH = "library_main_menu_css.css"
    BINDINGS = [("d", "dark_mode", "Set dark mode on/off")]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        yield Button("Add Book", id="addbook")
        yield Button("Rent Book", id="rentbook")
        yield Button("Rented Books", id="rentedbooks")
        yield Button("All Books", id="allbooks")
        yield Button("Add User", id="adduser")

    def action_dark_mode(self):
        self.dark = not self.dark

if __name__ == "__main__":
    LibraryMenuApp().run()
