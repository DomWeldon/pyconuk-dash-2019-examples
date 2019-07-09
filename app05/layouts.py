"""A very basic to do list."""
from typing import Iterable, Mapping

import dash_core_components as dcc
import dash_html_components as html
import dash_table


from .app import app, data_store


def list_tasks(tasks: Iterable[str]) -> Iterable[html.Li]:
    """Return list items of tasks."""

    return [html.Li(children=task) for task in tasks]


def todo_layout() -> html.Div:
    return html.Div(
        children=[
            html.H1("To Do List"),
            html.Ul(id="my-ul", children=list_tasks(data_store["tasks"])),
            dcc.Input(id="my-input"),
            html.Button(id="my-button", n_clicks=0, children="Add"),
        ]
    )
