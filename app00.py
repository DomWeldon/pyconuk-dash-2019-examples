"""Hello world example."""
import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1(children="Hello PyCon!!")])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
