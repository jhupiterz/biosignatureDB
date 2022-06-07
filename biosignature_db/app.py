from turtle import color
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
                            src="/assets/logo.png",
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
                            "Documentation", 
                            href="https://jhupiterz.notion.site/The-Biosignature-Database-f48effd1004f4155acfd76deee382436",
                            target='_blank', 
                            className="doc-link"
                        ),
                        html.A(
                            "Contribute", 
                            href="https://github.com/jhupiterz/research-analytics/blob/main/README.md",
                            target='_blank', 
                            className="doc-link"
                        ),
                        html.A(
                            "Download data", 
                            href="https://github.com/jhupiterz/research-analytics/blob/main/README.md",
                            target='_blank', 
                            className="doc-link-download"
                        )
                    
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
                        html.Div([
                            html.H3('Paleo-environment', style = {'order':'1', 'text-align': 'left', 'color': 'black', 'margin-bottom': '0px'}),
                            html.Div(id = 'paleoenv-filter', children = [], style = {'order': '2', 'z-index': '10', 'position': 'absolute'})
                        ], style = {'margin-top': '-20px'}),
                        html.Div(id = 'interactive-map', children = [], className = 'interactive-map')],
                        style = {'order': '1', 'margin-right': '40px'}),
                
                html.Div([
                    html.Div(id = 'hover-bar-chart', children = [], style = {'order': '1'}),
                    html.Div(id = 'hover-pie-chart', children = [], style = {'order': '2'})],
                    className= 'hover-charts')

            ], className = 'main-panel'),
        
        html.Div([
            html.Div([
                html.H3('Mars counterpart(s)', style = {'color': 'black', 'text-align': 'center', 'margin-bottom': '-20px', 'order': '1'}),
                html.Div(id = 'mars-map', children = [],
                        style = {'width': '40vw', 'height': '30vh', 'order': '2', 'margin-top': '-15vh', 'margin-left': '-35px'})],
            style = {'order':'1','display':'flex', 'flex-direction': 'column', 'align-items': 'center','margin-top': '2vh', 'height': '25vh'}),
            html.Div([
                html.H3('Supporting literature', style = {'color': 'black', 'text-align': 'center', 'order': '1'}),
                html.P('', style = {'order': '2'})],
            style = {'order':'2','display':'flex', 'flex-direction': 'column', 'align-items': 'center', 'margin-top': '5vh'})],
            className = 'left-panel')],
        
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
    Input('projection-selector', 'value'),
    Input('paleoenv-value', 'value'))
def create_interactive_map(data, projection, value_paleo):
    df = pd.DataFrame(data)
    if value_paleo == 'All':
        df = df.groupby(['latitude', 'longitude', 'location_name', 'max_age'], as_index=False).sum()[['latitude', 'longitude', 'location_name', 'number of samples', 'max_age']]
    elif value_paleo != 'All':
        df = df[df['paleoenvironment'] == value_paleo]
        df = df.groupby(['latitude', 'longitude', 'location_name', 'max_age'], as_index=False).sum()[['latitude', 'longitude', 'location_name', 'number of samples', 'max_age']]
    return dcc.Graph(id = 'map', figure=plots.plot_interactive_map(df, projection), className = 'map-style', config= {'displayModeBar': False})

@app.callback(
    Output('hover-bar-chart', 'children'),
    Input('map', 'hoverData'),
    Input('store-biosignature', 'data')
)
def create_bar_chart(hoverData, data):
    df = pd.DataFrame(data)
    grouped_df = grouped_df = df.groupby(['latitude', 'longitude', 'location_name', 'biosignature_cat', 'biosignature_subcat']).sum()[['number of samples' ]]
    grouped_df.reset_index(level=['biosignature_cat', 'biosignature_subcat'], inplace=True)
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

@app.callback(
    Output('paleoenv-filter', 'children'),
    Input('store-biosignature', 'data'))
def create_dropdown(data):
    df = pd.DataFrame(data)
    options = df['paleoenvironment'].unique().tolist()
    options = ['All'] + options
    return dcc.Dropdown(id = 'paleoenv-value', options = options, value = 'All',
                        placeholder = 'Paleoenvironment', style = {'color': 'black', 'width': '26vw'})

@app.callback(
    Output('mars-map', 'children'),
    Input('map', 'hoverData'),
    Input('store-biosignature', 'data'))
def generate_mars_map(hoverData, data):
    df = pd.DataFrame(data)
    if hoverData:
        location = hoverData['points'][0]['hovertext']
        mars_location = df[df['location_name'] == location]['mars_counterpart_1'][0]
        if mars_location == 'Columbia Hills, Mars':
            return html.Img(src='/assets/mars_map_columbia.png', style = {'width': '700px', 'height': '600px'})
        elif mars_location == 'Eberswalde delta, Mars':
            return html.Img(src='/assets/mars_map_eberswalde.png', style = {'width': '700px', 'height': '600px'})
        elif mars_location == 'Meridiani Planum, Mars':
            return html.Img(src='/assets/mars_map_meridiani.png', style = {'width': '700px', 'height': '600px'})
    return html.Img(src='/assets/mars_map.png', style = {'width': '700px', 'height': '600px'})

# Runs the app ------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=True)