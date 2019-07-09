"""Example of interactivity."""
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(id="my-h1"),
        dcc.Input(
            id="my-input", value="Lithuania", type="text"
        ),
    ]
)


@app.callback(
    Output(
        component_id="my-h1", component_property="children"
    ),
    [
        Input(
            component_id="my-input",
            component_property="value",
        )
    ],
)
def update_output_div(input_value: str) -> str:
    return f"Hello {input_value}!"


if __name__ == "__main__":
    app.run_server(debug=True)
