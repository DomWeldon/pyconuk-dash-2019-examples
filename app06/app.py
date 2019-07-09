import inspect
from typing import Callable, Hashable, Iterable, Optional, Tuple, Union

import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html


class App:
    """A very basic tool for declaring Dash apps.

    Simplified from decisionLab/GrandUI.
    """

    _ROUTES = {}
    """Store of routes which map to layouts."""

    _CALLBACKS = {}
    """Callbacks which are built into a graph."""

    @classmethod
    def callback(
        cls,
        output: Union[Tuple[str, str], Output],
        inputs: Optional[Iterable[Union[Tuple[str, str], Input]]] = None,
        state: Optional[Iterable[Union[Tuple[str, str], State]]] = None,
    ) -> Callable:
        """Register a callable as a callback to give to dash in factory.

        Mimics the callback function.

        Args:
            output: dash output area id
            inputs: dash input ids
            state: dash state
            events: dash events
        """
        # python annoyance: need for fresh instances
        inputs = inputs if inputs is not None else []
        state = state if state is not None else []
        # check the feature exists
        # designed to be called as a decorator

        def decorator(f):
            """Simply put a callable into our function map."""
            callback_id = "{}.{}".format(
                output.component_id, output.component_property
            )
            cls._CALLBACKS[callback_id] = {
                "output": output,
                "inputs": inputs,
                "state": state,
                "_callable": f,
                "_declared_in": inspect.getsourcefile(f),
            }

        return decorator

    @classmethod
    def layout(
        cls,
        label: str = None,
        path: str = None,
        feature: Optional[Hashable] = None,
    ):
        """Register a layout with our app.

        Mimics layout function.

        Args:
            label: Dash label for this area
            path: GrandUI routing path
        """

        # use as a decorator
        def decorator(f):
            cls._ROUTES[path] = {"label": label, "callable": f}

        return decorator

    @classmethod
    def route(cls, path) -> dash.development.base_component.Component:
        """Return the desired layout."""
        try:
            return cls._ROUTES[path]["callable"]()
        except KeyError:
            return cls._not_found()

    @staticmethod
    def _not_found() -> html.Div:
        return html.Div("Not Found")
