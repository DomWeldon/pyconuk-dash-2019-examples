import dash
from dash.dependencies import Input, Output

from .app import App
from .base import base_layout


def create_dash_app() -> dash.dash.Dash:
    """Register Dash app with our own Flask server."""
    app = dash.Dash(__name__)
    # required if loading callbacks before layouts
    app.config.supress_callback_exceptions = True

    return app


def register_template(app: dash.dash.Dash) -> None:
    """Register the main template of the application, including css."""
    app.layout = base_layout()
    app.callback(
        Output("page_content", "children"), [Input("url", "pathname")]
    )(App.route)


def register_callbacks(app: dash.dash.Dash) -> None:
    """Put all the callbacks into the app."""
    for callback_id, d in App._CALLBACKS.items():
        app.callback(**{k: v for k, v in d.items() if k[0] != "_"})(
            d["_callable"]
        )


def create_app() -> dash.dash.Dash:
    """Create the full working application."""
    app = create_dash_app()

    # register template and router
    register_template(app)
    register_callbacks(app)

    return app
