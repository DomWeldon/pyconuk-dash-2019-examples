"""Example of correctly filtering titanic dataset."""
from collections import Counter
from pathlib import Path
from string import ascii_lowercase
from typing import Iterable, Mapping, Tuple

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
assert titanic_path.exists(), "Cannot find titanic dataset."
df = pd.read_csv(titanic_path)


def series_count_first_letter(
    s: Iterable[str]
) -> Tuple[Iterable[str], Iterable[int]]:
    """I felt like being a bit silly and wrote this in one line for fun."""
    return zip(
        *sorted(
            dict(
                **{
                    k: v - 1
                    for k, v in Counter(
                        [
                            x.replace("(", "")
                            .split(".", 1)[1]
                            .strip()[0]
                            .lower()
                            for x in s
                        ]
                        + list(ascii_lowercase)
                    ).items()
                }
            ).items(),
            key=lambda t: ascii_lowercase.find(t[0]),
        )
    )  # for loops are your friends someimes.


# get our numbers
letters, freq = series_count_first_letter(df.Name)

app.layout = html.Div(
    children=[
        html.H1("Titanic Names"),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {
                        "x": letters,
                        "y": freq,
                        "type": "bar",
                        "name": "Titanic Passengers By First Name",
                    }
                ],
                "layout": {
                    "title": (
                        "Number of Passengers on the Titanic By First "
                        "Letter of First Name"
                    )
                },
            },
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
