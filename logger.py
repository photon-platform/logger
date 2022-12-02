import click
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class Logger(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
            ('d', 'toggle_dark', 'Toggle dark mode'),
            ('b', 'bell', 'bell'),
            ('ctrl+q', 'quit', 'quit'),
            ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def log(count, name):
    """start logger"""
    app = Logger()
    app.run()

if __name__ == '__main__':
    log()
