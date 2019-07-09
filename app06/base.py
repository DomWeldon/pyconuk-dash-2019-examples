import dash_core_components as dcc
import dash_html_components as html

# import dash_table_experiments as dt

from .app import App


def base_layout() -> html.Div:
    """Return a Dash Component which will serve as the top-level layout."""
    # register the layout
    return html.Div(
        [dcc.Location(id="url", refresh=False)]
        + [
            html.Div(
                html.Ul(
                    [
                        html.Li(dcc.Link(route["label"], href=path))
                        for path, route in App._ROUTES.items()
                    ]
                )
            ),
            html.Div(id="page_content", children="Click link to continue"),
        ]
    )
