from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label, Button, Static
from textual.containers import Grid
from tcode.problems import load_index

class SearchProblems(Screen):
    # TODO: Add list of all problems with pagination (Late : optimize so it doesnt load all 2000+ problems at once, maybe like 20 per page)
    
    CSS_PATH = "assets/search.tcss"
    
    def __init__(self) -> None:
        super().__init__()
        self.problems = load_index()
    
    def compose(self) -> ComposeResult:
        yield Label("Search Problems", id="title")
        with Grid(id="problems-grid"):
            for p in self.problems:
                yield Static(f"[b]{p.title}[/b]\n#{p.id} · {p.difficulty}", classes="card", id=f"problem-{p.id}")
            yield Button("Back", id="back-button")
        
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-button":
            self.app.pop_screen()