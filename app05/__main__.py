from .app import app

from .layouts import todo_layout

app.layout = todo_layout()

from .callbacks import add_task

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
