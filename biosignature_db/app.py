import pandas as pd
import plotly.express as px

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
        html.Div([
            html.Div(id='start-page', children=[
                html.Div([
                    html.Div(children = [
                        html.Div([
                            html.H3('Projection', style = {'order':'1', 'text-align': 'center', 'color': 'black', 'margin-bottom': '0px'}),
                            dcc.RadioItems(id = 'projection-selector',
                                        options = ['mercator', 'orthographic', 'natural earth'],
                                        value = 'mercator', inline= False, style = {'order': '2', 'color': 'black'})
                            ], className = 'projection-selector')], className= 'div-projection'),
                    html.Div(id = 'interactive-map', children = [], className = 'interactive-map')],
                    style = {'order': '1'}),
                
                html.Div([
                    html.Div(id = 'hover-bar-chart', children = [], style = {'order': '1'}),
                    html.Div(id = 'hover-pie-chart', children = [], style = {'order': '2'})],
                    className= 'hover-charts')

            ], className = 'main-panel')],
        className = 'main-body'),
        
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
    df = df.groupby(['latitude', 'longitude', 'location_name'], as_index=False).sum()[['latitude', 'longitude', 'location_name', 'number of samples']]
    return dcc.Graph(id = 'map', figure=plots.plot_interactive_map(df, projection), className = 'map-style')

@app.callback(
    Output('hover-bar-chart', 'children'),
    Input('map', 'hoverData'),
    Input('store-biosignature', 'data')
)
def create_bar_chart(hoverData, data):
    df = pd.DataFrame(data)
    grouped_df = df.groupby(['latitude', 'longitude', 'location_name', 'biosignature_cat']).sum()[['number of samples' ]]
    grouped_df.reset_index(level=['biosignature_cat'], inplace=True)
    if hoverData:
        loc = hoverData['points'][0]['hovertext']
        lat = hoverData['points'][0]['lat']
        lon = hoverData['points'][0]['lon']
        fig = plots.plot_bar_chart(grouped_df, lat, lon, loc)
        return dcc.Graph(figure=fig)
    else:
        return html.P('Hover on a location on the map to display more data', className = 'hover-default-text')

@app.callback(
    Output('hover-pie-chart', 'children'),
    Input('map', 'hoverData'),
    Input('store-biosignature', 'data')
)
def create_pie_chart(hoverData, data):
    df = pd.DataFrame(data)
    grouped_df = df.groupby(['latitude', 'longitude', 'location_name', 'detection_methods']).sum()[['number of samples' ]]
    grouped_df.reset_index(level=['detection_methods'], inplace=True)
    if hoverData:
        loc = hoverData['points'][0]['hovertext']
        lat = hoverData['points'][0]['lat']
        lon = hoverData['points'][0]['lon']
        fig = plots.plot_pie_chart(grouped_df, lat, lon, loc)
        return dcc.Graph(figure=fig)

# Runs the app ------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)