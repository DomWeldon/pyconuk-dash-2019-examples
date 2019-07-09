"""Example of correctly filtering titanic dataset."""
from pathlib import Path
from typing import Iterable, Mapping

import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_table
import pandas as pd


# create the app
app = dash.Dash(__name__)

# load out initial dataset
titanic_path = Path("./datasets/titanic.csv")
assert (
    titanic_path.exists()
), "Cannot find titanic dataset."
df = pd.read_csv(titanic_path)

app.layout = html.Div(
    children=[
        html.H1("Titanic Dataset"),
        html.H5("Search for a name"),
        dcc.Dropdown(
            id="my-dropdown",
            options=[{"label": "All", "value": "both"}]
            + [
                {"label": sex, "value": sex}
                for sex in df.Sex.unique()
            ],
            value="both",
        ),
        html.Div(id="my-div"),
        dash_table.DataTable(
            id="my-table",
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            data=[],
        ),
    ]
)


@app.callback(
    Output(
        component_id="my-table", component_property="data"
    ),
    [
        Input(
            component_id="my-dropdown",
            component_property="value",
        )
    ],
)
def provide_passengers(sex: str) -> Iterable[Mapping]:
    if sex == "both":
        return df.to_dict("rows")

    return df[df.Sex == sex].to_dict("rows")


@app.callback(
    Output(
        component_id="my-div",
        component_property="children",
    ),
    [
        Input(
            component_id="my-dropdown",
            component_property="value",
        )
    ],
)
def update_output_div(sex: str) -> str:
    if sex == "both":
        return "Showing all sexes."

    return f"Showing all {sex}s."


if __name__ == "__main__":
    app.run_server(debug=True)
