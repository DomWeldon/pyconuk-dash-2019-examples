"""A very basic shopping list."""
from typing import Iterable

import dash_core_components as dcc
import dash_html_components as html


from ..app import App
from ..store import data_store
from .utils import list_items


@App.layout(label="Shopping List", path="/shopping")
def shopping_layout() -> html.Div:
    return html.Div(
        children=[
            html.H1("Shopping List"),
            html.Ul(
                id="my-shopping-ul", children=list_items(data_store["items"])
            ),
            dcc.Input(id="my-shopping-input"),
            html.Button(
                id="my-shopping-button", n_clicks=0, children="Add Item"
            ),
        ]
    )
