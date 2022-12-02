from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Button, Input

from rich import inspect, print

from datetime import datetime

import subprocess


def write_log(log, title, excerpt='', tags='', category='') -> str:
    """TODO: Docstring for write_log.

    :log: TODO
    :title: TODO
    :excerpt: TODO
    :tags: TODO
    :categories: TODO
    :returns: filename

    """
    filename = f'log/{log}.rst'
    with open(filename, 'w') as f:
        f.write(title)
        f.write('\n')
        f.write('='*(len(title)))
        f.write('\n')
        f.write('\n')
        f.write(f'.. post:: {log}\n')
        f.write(f'   :tags: {tags}\n')
        f.write(f'   :category: {category}\n')
        f.write('\n')
        f.write(f'{excerpt}\n')

    return filename



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
            Static('LOG:'),
            Input(value=log_str, id='log'),
            Static('TITLE:'),
            Input(placeholder='Note Title', id='title'),
            Static('EXCERPT:'),
            Input(placeholder='short desc', id='excerpt'),
            Static('TAGS:'),
            Input(placeholder='comma separated list', id='tags'),
            Static('CATEGORY:'),
            Input(placeholder='comma separated list', id='category'),
            Static(),
            Container(
                Button("Save", id='save'),
                Button("Quit", id='quit'),
                classes="buttons",
            ),
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
        log = self.query_one('#log').value
        title = self.query_one('#title').value
        excerpt = self.query_one('#excerpt').value
        tags = self.query_one('#tags').value
        category = self.query_one('#category').value

        filename = write_log(log, title, excerpt, tags, category)
        self.exit(filename)

if __name__ == "__main__":
    app = Logger()
    reply = app.run()
    print(reply)

    if reply:
        subprocess.run(['vim', reply])

    
