import pandas as pd

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from biosignature_db import plots
from biosignature_db import data

app = dash.Dash(
    __name__, suppress_callback_exceptions = True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1", 'charSet':'“UTF-8”'}])

app.title = "Biosignature Database"

app.layout = html.Div(
    [
        # Banner ------------------------------------------------------------
        html.Div(
            [
                html.A(
                    [
                        html.Img(
                            src="/assets/dna.png",
                            alt="biosignature database"
                        ),
                        html.H3("Biosignature Database")
                    ],
                    href="https://www.notion.so/jhupiterz/The-Biosignature-Database-\
                          f48effd1004f4155acfd76deee382436",
                    target='_blank',
                    className="logo-banner",
                ),
                html.Div(
                    [
                        html.A(
                            "Contribute", 
                            href="https://github.com/jhupiterz/biosignature_db",
                            target='_blank', 
                            className="doc-link"
                        ),
                        html.A(
                            "Documentation", 
                            href="https://github.com/jhupiterz/research-analytics/blob/main/README.md",
                            target='_blank', 
                            className="doc-link"
                        ),
                    
                    ],
                    className="navbar"
                ),
            ],
            className="banner",
        ),
        
        dcc.Store(id='store-biosignature', data = data.read_json_data('data/biosignature.json'), storage_type='memory'),

        # Main content ----------------------------------------------------------
        html.Div(id='start-page', children=[
            html.Div(children = [
                dcc.RadioItems(id = 'projection-selector',
                               options = ['mercator', 'orthographic', 'natural earth'],
                               value = 'natural earth', inline= False, style = {'color': 'black'})
                ], className = 'projection-selector'),
            html.Div(id = 'interactive-map', children = [], className = 'interactive-map')

        ], className = 'main-body'),
        
        # Footer ----------------------------------------------------------------
        html.Footer(
            [
                html.P(
                    [
                        "Built with ", 
                        html.A("Plotly Dash", href="https://plotly.com/dash/", target="_blank")
                    ],
                ),
                html.P(
                    [
                        "Powered by ", 
                        html.A("Semantic Scholar", href="https://www.semanticscholar.org/", target="_blank")
                    ],
                ),
            ]
        ),
    ],
    className="app-layout",
)

@app.callback(
    Output('interactive-map', 'children'),
    Input('store-biosignature', 'data'),
    Input('projection-selector', 'value'))
def create_interactive_map(data, projection):
    df = pd.DataFrame(data)
    df = df.groupby(['latitude', 'longitude', 'location_name'], as_index=False).count()[['latitude', 'longitude', 'location_name', 'biosignature_id']]
    return dcc.Graph(figure=plots.plot_interactive_map(df, projection), className = 'map-style')

# Runs the app ------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)