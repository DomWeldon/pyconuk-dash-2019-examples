"""Run the app."""
from .factory import create_app

from .home import *
from .todo import *
from .shopping import *

app = create_app()

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
