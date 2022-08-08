import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children="You're about to submit new data!", style = {'color': 'black'}),
    html.Div([
        html.P(children=["👏 Thank you for willing to contribute to the biosignature database.",
                        "The purpose of this project is to have as much data as possible on (potential) biosignatures.\n","However, data only makes sense if it is consistent and of good quality.",
                        "\n⚠️ PLEASE, once again make sure to read the ",
                        html.A("contribution guidelines", href="https://jhupiterz.notion.site/The-Biosignature-Database-f48effd1004f4155acfd76deee382436", target="_blank", style = {'color': 'blue', 'font-weight': 'bold'}),
                        " before submitting any new data."], style = {'color': 'black', 'font-family': 'Arial, sans-serif', 'margin': 'auto', 'text-align': 'center', 'padding-top': '2vh'})],
            style = {'width': '75vw', 'height': '13vh', 'margin': 'auto', 'backgroundColor': '#e6e6e6', 'border-radius': '10px'}),
    

    ])