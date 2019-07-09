"""A very basic to do list."""
from typing import Iterable

import dash_html_components as html


def list_items(items: Iterable[str]) -> Iterable[html.Li]:
    """Return list items of tasks."""

    return [html.Li(children=item) for item in items]
