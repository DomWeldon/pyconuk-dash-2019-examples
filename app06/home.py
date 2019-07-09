import dash_html_components as html

from .app import App


@App.layout(label="Home", path="/")
def homepage() -> html.Div:
    return html.Div(
        ["Welcome to demo app 6!", "This app uses routing and navigation."]
    )


__all__ = ["homepage"]
