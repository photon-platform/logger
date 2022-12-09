"""
PHOTON logger 
"""
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Button, Input

from rich import inspect, print

from datetime import datetime
from pathlib import Path


from jinja2 import Environment, PackageLoader, select_autoescape

LOG_TEMPLATE = 'log.rst.j2'


class Logger(App):
    CSS_PATH = "logger.css"
    TITLE = "PHOTON • logger"
    BINDINGS = [
            ('ctrl+s', 'save', 'save'),
            ('ctrl+q', 'quit', 'quit'),
            ]

    def compose(self) -> ComposeResult:
        log_time = datetime.now()
        log_str = log_time.strftime('%y.%j-%H%M%S')
        yield Header()
        yield Footer()
        yield Container(
            Static('LOG:', classes='label'),
            Input(value=log_str, id='log'),
            Static('TITLE:', classes='label'),
            Input(placeholder='Note Title', id='title'),
            Static('EXCERPT:', classes='label'),
            Input(placeholder='short desc', id='excerpt'),
            Static('TAGS:', classes='label'),
            Input(placeholder='comma separated list', id='tags'),
            Static('CATEGORY:', classes='label'),
            Input(placeholder='comma separated list', id='category'),
            Static(),
            Button("Save", id='save'),
            Static(),
            Button("Quit", id='quit'),
            id="dialog",
            classes="form"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "save":
            self.action_save()

        elif event.button.id == "quit":
            self.exit()
                

    def action_save(self):
        log_stamp = self.query_one('#log').value
        title = self.query_one('#title').value
        excerpt = self.query_one('#excerpt').value
        tags = self.query_one('#tags').value
        category = self.query_one('#category').value
        context = {
                'log_stamp': log_stamp,
                'title': title,
                'excerpt': excerpt,
                'tags': tags,
                'category': category
                }

        env = Environment(
            #  loader=FileSystemLoader(TEMPLATE_PATH),
            loader=PackageLoader('photonplatform.logger'),
            )
        template = env.get_template(LOG_TEMPLATE)
        rst_text = template.render(**context)

        filename = f'log/{log_stamp}.rst'
        file_path = Path(filename)
        file_path.write_text(rst_text)

        self.exit(filename)
