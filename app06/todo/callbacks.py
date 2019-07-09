"""A very basic to do list."""
from typing import Iterable, Mapping

from dash.dependencies import Input, Output, State
import dash_html_components as html

from ..app import App
from ..store import data_store
from .utils import list_tasks


@App.callback(
    Output("my-todo-ul", "children"),
    [Input("my-todo-button", "n_clicks")],
    [State("my-todo-input", "value")],
)
def add_task(
    n_clicks: int = 0,
    value: str = None,
    data_store: Mapping[str, Iterable] = data_store,
) -> Iterable[html.Li]:
    """Called when the button is clicked."""
    if value is not None and len(value.strip()):
        data_store["tasks"].append(value.strip())

    return list_tasks(data_store["tasks"])
