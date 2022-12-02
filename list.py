"""
https://gist.github.com/btbytes/72b24b5c194baaf2e22e64ee9d9af54c#file-restructuredtext_extract_metadata-py
"""
from pathlib import Path
from rich import print, inspect
from collections import namedtuple
from contextlib import contextmanager
from datetime import date, datetime

from docutils import core, io, nodes, readers


def extract_title(doctree, remove=True):
    """Find, extract, optionally remove, and return the document's first
    heading (which is assumed to be the main title).
    """
    with find_node_by_class(doctree, nodes.title, remove) as node:
        if node is not None:
            return node.astext()


def extract_metadata(doctree, field_names_and_parsers, remove=True):
    """Find, extract, optionally remove, and return the values for the
    specified names from the document's first field list (which is assumed to
    represent the document's meta data).
    """
    field_names = frozenset(field_names_and_parsers.keys())
    metadata = dict.fromkeys(field_names)

    with find_node_by_class(doctree, nodes.field_list, remove) as node:
        if node is not None:
            field_nodes = select_field_nodes(node, field_names)
            # Parse each field's value using the function
            # specified for the field's name.
            for name, value in field_nodes:
                metadata[name] = field_names_and_parsers[name](value)

    return metadata


@contextmanager
def find_node_by_class(doctree, node_class, remove):
    """Find the first node of the specified class."""
    index = doctree.first_child_matching_class(node_class)
    if index is not None:
        yield doctree[index]
        if remove:
            del doctree[index]
    else:
        yield


if __name__ == "__main__":
    
    p = Path('./log')

    notes = list(p.iterdir())
    #  print(notes)
    #  field_names_and_parsers = {
            #  'author': str,
            #  'date': lambda s: datetime.strptime(s, '%y.%j-%H%M%S').date(),
            #  'version': str,
            #  'tags': lambda s: frozenset([q.strip() for q in s.split(',')]),
        #  }
    for note in notes:
        #  note_text = note.read_text()
        #  overrides = {
            # Disable the promotion of a lone top-level section title to document
            # title (and subsequent section title to document subtitle promotion).
            #  'docinfo_xform': 0,
            #  'initial_header_level': 2,
        #  }

        # Read tree and extract metadata.
        #  doctree = core.publish_doctree(note_text, settings_overrides=overrides)

        #  title = extract_title(doctree)
        with note.open() as f:
            title = f.readline().strip()
            print(title)

        #  metadata = extract_metadata(doctree, field_names_and_parsers)
        #  print(metadata)

