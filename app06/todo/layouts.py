"""A very basic to do list."""
from typing import Iterable

import dash_core_components as dcc
import dash_html_components as html


from ..app import App
from ..store import data_store
from .utils import list_tasks


@App.layout(label="Todo List", path="/todos")
def todo_layout() -> html.Div:
    return html.Div(
        children=[
            html.H1("To Do List"),
            html.Ul(id="my-todo-ul", children=list_tasks(data_store["tasks"])),
            dcc.Input(id="my-todo-input"),
            html.Button(id="my-todo-button", n_clicks=0, children="Add Task"),
        ]
    )
