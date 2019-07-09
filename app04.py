"""A very basic to do list."""
from pathlib import Path
from typing import Iterable, Mapping

import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_table
import pandas as pd


# create the app
app = dash.Dash(__name__)

# load out initial dataset
data_store = {"tasks": []}  # mimics a database


def list_tasks(tasks: Iterable[str]) -> Iterable[html.Li]:
    """Return list items of tasks."""

    return [html.Li(children=task) for task in tasks]


app.layout = html.Div(
    children=[
        html.H1("To Do List"),
        html.Ul(
            id="my-ul",
            children=list_tasks(data_store["tasks"]),
        ),
        dcc.Input(id="my-input"),
        html.Button(
            id="my-button", n_clicks=0, children="Add"
        ),
    ]
)


@app.callback(
    Output("my-ul", "children"),
    [Input("my-button", "n_clicks")],
    [State("my-input", "value")],
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


if __name__ == "__main__":
    app.run_server(debug=True)
