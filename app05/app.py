import dash

# create the app
app = dash.Dash(__name__)

# load out initial dataset
data_store = {"tasks": []}  # mimics a database
