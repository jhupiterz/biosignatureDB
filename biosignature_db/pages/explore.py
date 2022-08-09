import pandas as pd
import dash
from dash import html, dcc, callback, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from biosignature_db import plots
from biosignature_db import data

dash.register_page(__name__, path='/')

biosignature_json = data.read_json_data('data/biosignature.json')
bio_df = pd.DataFrame(biosignature_json)
bio_df = bio_df[bio_df['status'] == ' 🟢 validated']

layout = html.Div(children=[
    dcc.Store(id='store-biosignature', data = data.read_json_data('data/biosignature.json'), storage_type = 'memory'),
        
        dbc.Card(
            [
                dbc.CardHeader(
                    dbc.Tabs(
                        [
                            dbc.Tab(label="Dashboard", tab_id="dashboard"),
                            dbc.Tab(label="Data", tab_id="data"),
                        ],
                        style = {'margin-top': '0.5vh'},
                        id="card-tabs",
                        active_tab="dashboard",
                    ), style= {'z-index': '1000'}
                ),
                dbc.CardBody(html.P(id="card-content", className="card-text")),
            ]),

    ])

@callback(Output('card-content', 'children'),
          Input('card-tabs', 'active_tab'))
def render_tab_content(tab_value):
    if tab_value == 'dashboard':
        return html.Div([
            html.Div([
                html.Div(id='start-page', children=[
                    html.Div([
                        html.Div(children = [
                            html.Div([
                                html.H3('Projection', style = {'order':'1', 'text-align': 'center', 'color': 'black', 'margin-bottom': '0px', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'}),
                                dcc.RadioItems(id = 'projection-selector',
                                            options = ['mercator', 'orthographic', 'natural earth'],
                                            value = 'mercator', inline= False, style = {'order': '2', 'color': 'black'})
                                ], className = 'projection-selector')], className= 'div-projection'),
                            html.Div([
                                html.H3('(Paleo)environment', style = {'order':'1', 'text-align': 'left', 'color': 'black', 'margin-bottom': '8px', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'}),
                                html.Div(id = 'paleoenv-filter', children = [], style = {'order': '2', 'z-index': '10', 'position': 'absolute'})
                            ], style = {'margin-top': '-10px'}),
                            html.Div(id = 'interactive-map', children = [], className = 'interactive-map')],
                            style = {'order': '1', 'margin-left': '0vw', 'margin-top': '2vh'}),
                    
                    html.Div([
                        html.Div(id = 'hover-bar-chart', children = [], style = {'order': '1'}),
                        html.Div(id = 'hover-pie-chart', children = [], style = {'order': '2'})],
                        className= 'hover-charts')

                ], className = 'main-panel'),
            
            html.Div([
                html.Div([
                    html.H3('Mars counterpart(s)', style = {'color': 'black', 'text-align': 'center', 'margin-bottom': '-24px', 'margin-left': '4vw', 'order': '1', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'}),
                    html.Div(id = 'mars-map', children = [],
                            style = {'width': '40vw', 'height': '30vh', 'order': '2', 'margin-top': '-12vh', 'margin-left': '2vw'})],
                style = {'order':'1','display':'flex', 'flex-direction': 'column', 'align-items': 'center','margin-top': '0vh', 'height': '25vh'}),
                html.Div([
                    html.H3('Data preview', style = {'color': 'black', 'text-align': 'center', 'order':'1', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'}),
                    html.Div([
                        dash_table.DataTable(id = 'data-preview', editable = False, style_data = {'color': 'black', 'font-family': 'Arial, sans serif'},
                                            style_header= {'color': 'black', 'font-weight': 'bold', 'background-color': 'rgba(5, 8, 184, 0.4)', 'textAlign': 'left', 'font-family': 'Arial, sans serif'},
                                            style_cell = {'textAlign': 'left', 'padding': '0px'},
                                            style_table = {'height':'500px', 'width':'30vw', 'height':'275px', 'overflow': 'auto'},
                                            style_data_conditional=[
                                                                        {
                                                                            'if': {'row_index': 'even'},
                                                                            'backgroundColor': 'rgba(5, 8, 184, 0.1)',
                                                                        },
                                                                        {
                                                                            'if': {'row_index': 'odd'},
                                                                            'backgroundColor': 'rgba(5, 8, 184, 0.4)',
                                                                        },
                                                                        {
                                                                            'if': {'column_id': 'pub_url'},
                                                                            'color': 'black'
                                                                        }
                                                                    ])],
                        style = {'order':'2'})],
                style = {'order':'2','display':'flex', 'flex-direction': 'column', 'align-items': 'center',
                        'width':'30vw', 'height':'37vh', 'margin-top': '10vh', 'margin-left': '1vw'})],
                className = 'left-panel')],
            
            className = 'main-body')], style = {'height': '80vh','margin':'auto', 'margin-top': '-4.5vh', 'width': '98vw', 'backgroundColor': '#e6e6e6', 'border-radius': '10px'})
    else:
        return html.Div([
                    html.Div([
                        html.P(['👋 Make sure to read the ',
                                html.A("contribution guidelines", href="https://jhupiterz.notion.site/The-Biosignature-Database-f48effd1004f4155acfd76deee382436", target="_blank", style = {'color': 'blue', 'font-weight': 'bold'}),
                                ' before submitting any new data'], style = {'order':'1', 'color':'black', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw', 'margin-top': '1vh'}),
                        html.Button(
                             "Download data",
                             className="doc-link-download",
                             style = {'font-family': 'Arial, sans-serif', 'font-size': '1vw'},
                             id = "btn-download-data",
                             n_clicks= 0
                        ),
                        html.Button(
                             "Validate data",
                             className="doc-link-download",
                             style = {'font-family': 'Arial, sans-serif', 'font-size': '1vw', 'order': '3'},
                             id = "btn-validate-data",
                             n_clicks= 0
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("What data do you wish to validate?")),
                                dbc.ModalBody("A small modal."),
                            ],
                            id="validate-pop-up",
                            size="lg",
                            style={'color': 'black', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'},
                            is_open=False,
                        ),
                        dcc.Download(id="download-csv"),
                        html.A(
                            "Submit new data", 
                            href="/submit",
                            className="doc-link-submit",
                            style = {'font-family': 'Arial, sans-serif', 'font-size': '1vw', 'order': '4'}
                        )], style={'width': '95vw', 'margin': 'auto', 'margin-top': '1vh', 'display': 'flex', 'flex-direction': 'row', 'align-items': 'center', 'justify-content': 'space-between'}),
                    dash_table.DataTable(id = 'data-preview', editable = False, style_data = {'color': 'black', 'font-family': 'Arial, sans serif'},
                                style_header= {'color': 'black', 'font-weight': 'bold', 'background-color': 'rgba(5, 8, 184, 0.4)', 'textAlign': 'left', 'font-family': 'Arial, sans serif'},
                                style_cell = {'textAlign': 'left', 'padding': '0px'},
                                style_table = {'height':'65vh', 'width':'95vw', 'overflow': 'auto', 'margin': 'auto', 'margin-top': '3vh'},
                                style_data_conditional=[
                                                            {
                                                                'if': {'row_index': 'even'},
                                                                'backgroundColor': 'rgba(5, 8, 184, 0.1)',
                                                            },
                                                            {
                                                                'if': {'row_index': 'odd'},
                                                                'backgroundColor': 'rgba(5, 8, 184, 0.4)',
                                                            },
                                                            {
                                                                'if': {'column_id': 'pub_url'},
                                                                'color': 'black'
                                                            }
                                                        ])], style = {'height': '79vh', 'display': 'flex', 'flex-direction': 'column'})

@callback(
    Output('interactive-map', 'children'),
    Input('store-biosignature', 'data'),
    Input('projection-selector', 'value'),
    Input('paleoenv-value', 'value'))
def create_interactive_map(data, projection, value_paleo):
    df = pd.DataFrame(data)
    df = df[df['status'] == ' 🟢 validated']
    if value_paleo == 'All':
        df = df.groupby(['latitude', 'longitude', 'location_name', 'max_age'], as_index=False).sum()[['latitude', 'longitude', 'location_name', 'number of samples', 'max_age']]
    elif value_paleo != 'All':
        df = df[df['paleoenvironment'] == value_paleo]
        df = df.groupby(['latitude', 'longitude', 'location_name', 'max_age'], as_index=False).sum()[['latitude', 'longitude', 'location_name', 'number of samples', 'max_age']]
    return dcc.Graph(id = 'map', figure=plots.plot_interactive_map(df, projection), className = 'map-style', config= {'displayModeBar': False})

@callback(
    Output('hover-bar-chart', 'children'),
    Input('map', 'hoverData'),
    Input('store-biosignature', 'data')
)
def create_bar_chart(hoverData, data):
    df = pd.DataFrame(data)
    df = df[df['status'] == ' 🟢 validated']
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

@callback(
    Output('hover-pie-chart', 'children'),
    Input('map', 'hoverData'),
    Input('store-biosignature', 'data')
)
def create_pie_chart(hoverData, data):
    df = pd.DataFrame(data)
    df = df[df['status'] == ' 🟢 validated']
    grouped_df = df.groupby(['latitude', 'longitude', 'location_name', 'detection_methods']).sum()[['number of samples' ]]
    grouped_df.reset_index(level=['detection_methods'], inplace=True)
    if hoverData:
        loc = hoverData['points'][0]['hovertext']
        lat = hoverData['points'][0]['lat']
        lon = hoverData['points'][0]['lon']
        fig = plots.plot_pie_chart(grouped_df, lat, lon, loc)
        return dcc.Graph(figure=fig)

@callback(
    Output('paleoenv-filter', 'children'),
    Input('store-biosignature', 'data'))
def create_dropdown(data):
    df = pd.DataFrame(data)
    df = df[df['status'] == ' 🟢 validated']
    options = df['paleoenvironment'].unique().tolist()
    options = ['All'] + options
    return dcc.Dropdown(id = 'paleoenv-value', options = options, value = 'All', clearable= False,
                        placeholder = 'Paleoenvironment', style = {'color': 'black', 'width': '26vw'})

@callback(
    Output('mars-map', 'children'),
    Input('map', 'hoverData'),
    Input('store-biosignature', 'data'))
def generate_mars_map(hoverData, data):
    df = pd.DataFrame(data)
    df = df[df['status'] == ' 🟢 validated']
    if hoverData:
        location = hoverData['points'][0]['hovertext']
        mars_location = df[df['location_name'] == location]['mars_counterpart_1'][0]
        if mars_location == 'Columbia Hills, Mars':
            return html.Img(src='/assets/mars_map_columbia.png', style = {'width': '600px', 'height': '500px'})
        elif mars_location == 'Eberswalde delta, Mars':
            return html.Img(src='/assets/mars_map_eberswalde.png', style = {'width': '600px', 'height': '500px'})
        elif mars_location == 'Meridiani Planum, Mars':
            return html.Img(src='/assets/mars_map_meridiani.png', style = {'width': '600px', 'height': '500px'})
    return html.Img(src='/assets/mars_map.png', style = {'width': '600px', 'height': '500px'})

@callback(
    Output("data-preview", "data"),
    Output("data-preview", "columns"),
    Output("data-preview", "css"),
    Input("store-biosignature", "data")
)
def generate_datatable(data):
    df = pd.DataFrame(data)[['biosignature_id', 'biosignature_cat', 'biosignature_subcat', 'name',
                             'indicative_of', 'detection_methods', 'sample_type', 'number of samples',
                             'min_age', 'max_age', 'pub_url', 'paleoenvironment', 'status']]
    return df.to_dict('records'),[{'id': x, 'name': x, 'presentation': 'markdown'} if x == 'pub_url' else {'id': x, 'name': x} for x in df.columns], [dict(selector='td[data-dash-row="1"][data-dash-column="pub_url"] table', rule='color: blue;')]

@callback(
    Output("download-csv", "data"),
    Input("btn-download-data", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    if n_clicks > 0:
        return dcc.send_data_frame(bio_df.to_csv, "biosignature_data.csv")

@callback(
    Output("validate-pop-up", "is_open"),
    Input("btn-validate-data", "n_clicks"),
    State("validate-pop-up", "is_open"),
    prevent_initial_call=True
)
def toggle_modal(n_clicks, is_open):
    if n_clicks > 0:
        return not is_open
    return is_open