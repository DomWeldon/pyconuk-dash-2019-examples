"""A very basic to do list."""
from typing import Iterable, Mapping

from dash.dependencies import Input, Output, State
import dash_html_components as html

from ..app import App
from ..store import data_store
from .utils import list_items


@App.callback(
    Output("my-shopping-ul", "children"),
    [Input("my-shopping-button", "n_clicks")],
    [State("my-shopping-input", "value")],
)
def add_item(
    n_clicks: int = 0,
    value: str = None,
    data_store: Mapping[str, Iterable] = data_store,
) -> Iterable[html.Li]:
    """Called when the button is clicked."""
    if value is not None and len(value.strip()):
        data_store["items"].append(value.strip())

    return list_items(data_store["items"])
