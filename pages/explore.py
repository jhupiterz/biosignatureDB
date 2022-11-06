import pandas as pd
import dash
from dash import html, dcc, callback, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import plots
import data

dash.register_page(__name__, path='/')

def generate_data_preview(df):
    return df.to_dict('records'),[{'id': x, 'name': x, 'presentation': 'markdown'} if x == 'pub_url' else {'id': x, 'name': x} for x in df.columns], [dict(selector='td[data-dash-column="pub_url"] table', rule='color: blue;')]

def generate_data_to_validate(df):
    df = df[df['status'] == '🟠 pending']
    return df.to_dict('records'), [{'id': x, 'name': x, 'presentation': 'markdown'} if x == 'pub_url' else {'id': x, 'name': x} for x in df.columns], [dict(selector='td[data-dash-row="1"][data-dash-column="pub_url"] table', rule='color: blue;')]

def create_dropdown(df):
    df = df[df['status'] == ' 🟢 validated']
    options = df['paleoenvironment'].unique().tolist()
    options = ['All'] + options
    return dcc.Dropdown(id = 'paleoenv-value', options = options, value = 'All', clearable= False,
                        placeholder = 'Paleoenvironment', style = {'color': 'black', 'width': '26vw'})

layout = html.Div(children=[
        dbc.Card(
            [
                dbc.CardHeader(
                    dbc.Tabs(
                        [
                            dbc.Tab(label="Dashboard", tab_id="dashboard"),
                            dbc.Tab(label="Data", tab_id="data"),
                        ],
                        style = {'margin-top': '0.5vh', 'margin-left': '0.1vw'},
                        id="card-tabs",
                        active_tab="dashboard",
                    ), style= {'z-index': '1000'}
                ),
                dbc.CardBody(html.P(id="card-content", className="card-text")),
            ], style = {'z-index': 0}),

    ], style={'z-index': '1'})

@callback(Output('card-content', 'children'),
          Input('card-tabs', 'active_tab'))
def render_tab_content(tab_value):
    df = data.read_database()
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
                                html.H3('(Paleo)environment', style = {'order':'1', 'text-align': 'left', 'color': 'black', 'margin-bottom': '1vh', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'}),
                                html.Div(id = 'paleoenv-filter', children = [create_dropdown(df)], style = {'order': '2', 'z-index': '10', 'position': 'absolute'})
                            ], style = {'margin-top': '-1vh'}),
                            html.Div(id = 'interactive-map', children = [], className = 'interactive-map')],
                            style = {'order': '1', 'margin-left': '0vw', 'margin-top': '2vh'}),
                    
                    html.Div([
                        html.Div(id = 'hover-bar-chart', children = [], style = {'order': '1'}),
                        html.Div(id = 'hover-pie-chart', children = [], style = {'order': '2'})],
                        className= 'hover-charts')

                ], className = 'main-panel'),
            
            html.Div([
                html.Div([
                    html.H3('Mars counterpart(s)', style = {'color': 'black', 'text-align': 'center', 'margin-bottom': '-2vh', 'margin-left': '4vw', 'order': '1', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'}),
                    html.Div(id = 'mars-map', children = [],
                            style = {'width': '30vw', 'height': '25vh', 'order': '2', 'margin-left': '2vw', 'margin-top': '3vh'})],
                style = {'order':'1','display':'flex', 'flex-direction': 'column', 'align-items': 'center','margin-top': '0vh', 'height': '25vh'}),
                html.Div([
                    html.H3('Data preview', style = {'color': 'black', 'text-align': 'center', 'order':'1', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'}),
                    html.Div([
                        dash_table.DataTable(id = 'data-preview', data = generate_data_preview(df)[0], columns= generate_data_preview(df)[1],
                                            css = generate_data_preview(df)[2] ,editable = False, style_data = {'color': 'black', 'font-family': 'Arial, sans serif'},
                                            style_header= {'color': 'black', 'font-weight': 'bold', 'background-color': 'rgba(5, 8, 184, 0.4)', 'textAlign': 'left', 'font-family': 'Arial, sans serif'},
                                            style_cell = {'textAlign': 'left', 'padding': '0px'},
                                            style_table = {'width':'30vw', 'height':'37.5vh', 'overflow': 'auto'},
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
                                                                            'color': 'black',
                                                                            'padding-top': '17px'
                                                                        }
                                                                    ])],
                        style = {'order':'2', 'height': '38vh'})],
                style = {'order':'2','display':'flex', 'flex-direction': 'column', 'align-items': 'center',
                        'width':'30vw', 'height':'45vh', 'margin-top': '7vh', 'margin-left': '1vw'})],
                className = 'left-panel')],
            
            className = 'main-body')], style = {'height': '80vh','margin':'auto', 'margin-top': '-4.5vh', 'width': '98vw', 'backgroundColor': '#e6e6e6', 'border-radius': '10px'})
    else:
        return html.Div([
                    html.Div([
                        html.P(id='datatable-message', style = {'order':'1', 'color':'black', 'font-family': 'Arial, sans-serif', 'font-size': '1.3vw', 'margin-top': '1vh'}),
                            
                        html.Div(id='data-tab-buttons', style = {'display': 'flex', 'flex-direction': 'row', 'align-items': 'center', 'justify-content': 'flex-end', 'order': '2', 'width': '40vw'}),    
                            
                    ], style={'width': '95vw', 'margin': 'auto', 'margin-top': '1vh', 'display': 'flex', 'flex-direction': 'row', 'align-items': 'center', 'justify-content': 'space-between'}),
                    dash_table.DataTable(id = 'data-preview', data = generate_data_preview(df)[0], columns= generate_data_preview(df)[1], export_format = 'csv',
                                css = generate_data_preview(df)[2], editable = False, style_data = {'color': 'black', 'font-family': 'Arial, sans serif'},
                                style_header= {'color': 'black', 'font-weight': 'bold', 'background-color': 'rgba(5, 8, 184, 0.4)', 'textAlign': 'left', 'font-family': 'Arial, sans serif'},
                                style_cell = {'textAlign': 'left', 'padding': '0px'},
                                style_table = {'height':'65vh', 'width':'95vw', 'overflow': 'auto', 'margin': 'auto', 'margin-bottom': '2vh'},
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
                                                                'color': 'black',
                                                                'padding-top': '17px'
                                                            }
                                                        ])], style = {'height': '79vh', 'display': 'flex', 'flex-direction': 'column'})

@callback(
    Output('interactive-map', 'children'),
    Input('projection-selector', 'value'),
    Input('paleoenv-value', 'value'))
def create_interactive_map(projection, value_paleo):
    df = data.read_database()
    df_ = df[df['status'] == ' 🟢 validated']
    if value_paleo == 'All':
        df_ = df_.groupby(['latitude', 'longitude', 'location_name', 'max_age'], as_index=False).sum()[['latitude', 'longitude', 'location_name', 'number_of_samples', 'max_age']]
    elif value_paleo != 'All':
        df_ = df_[df_['paleoenvironment'] == value_paleo]
        df_ = df_.groupby(['latitude', 'longitude', 'location_name', 'max_age'], as_index=False).sum()[['latitude', 'longitude', 'location_name', 'number_of_samples', 'max_age']]
    return dcc.Graph(id = 'map', figure=plots.plot_interactive_map(df, projection), className = 'map-style', config= {'displayModeBar': False})

@callback(
    Output('hover-bar-chart', 'children'),
    Input('map', 'hoverData')
)
def create_bar_chart(hoverData):
    df = data.read_database()
    df_ = df[df['status'] == ' 🟢 validated']
    grouped_df = df_.groupby(['latitude', 'longitude', 'location_name', 'biosignature_cat', 'biosignature_subcat']).sum()[['number_of_samples' ]]
    grouped_df.reset_index(level=['biosignature_cat', 'biosignature_subcat'], inplace=True)
    if hoverData:
        loc = hoverData['points'][0]['hovertext']
        lat = hoverData['points'][0]['lat']
        lon = hoverData['points'][0]['lon']
        fig = plots.plot_bar_chart(grouped_df, lat, lon, loc)
        return dcc.Graph(figure=fig)
    else:
        return html.P('Hover on a location on the map to display more data', className = 'hover-default-text', style = {'font-family': 'Arial, sans-serif'})

@callback(
    Output('hover-pie-chart', 'children'),
    Input('map', 'hoverData')
)
def create_pie_chart(hoverData):
    df = data.read_database()
    df_ = df[df['status'] == ' 🟢 validated']
    grouped_df = df_.groupby(['latitude', 'longitude', 'location_name', 'detection_methods']).sum()[['number_of_samples' ]]
    grouped_df.reset_index(level=['detection_methods'], inplace=True)
    if hoverData:
        loc = hoverData['points'][0]['hovertext']
        lat = hoverData['points'][0]['lat']
        lon = hoverData['points'][0]['lon']
        fig = plots.plot_pie_chart(grouped_df, lat, lon, loc)
        return dcc.Graph(figure=fig)

@callback(
    Output('mars-map', 'children'),
    Input('map', 'hoverData'))
def generate_mars_map(hoverData):
    df = data.read_database()
    df_ = df[df['status'] == ' 🟢 validated']
    if hoverData:
        #print(hoverData)
        location = hoverData['points'][0]['hovertext']
        #print(df_[df_['location_name'] == location])
        mars_location = df_[df_['location_name'] == location]['mars_counterpart'].iloc[0]
        if mars_location == 'Columbia Hills, Mars':
            return html.Img(src='/assets/mars_map_columbia.png', style = {'width': '38vw', 'height': '60vh', 'margin-left': '-4.5vw', 'margin-top': '-18vh'})
        elif mars_location == 'Eberswalde delta, Mars':
            return html.Img(src='/assets/mars_map_eberswalde.png', style = {'width': '38vw', 'height': '60vh', 'margin-left': '-4.5vw', 'margin-top': '-18vh'})
        elif mars_location == 'Meridiani Planum, Mars':
            return html.Img(src='/assets/mars_map_meridiani.png', style = {'width': '38vw', 'height': '60vh', 'margin-left': '-4.5vw', 'margin-top': '-18vh'})
    return html.Img(src='/assets/mars_map.png', style = {'width': '38vw', 'height': '60vh', 'margin-left': '-4.5vw', 'margin-top': '-18vh'})

# @callback(
#     Output("download-csv", "data"),
#     Input("btn-download-data", "n_clicks"),
#     prevent_initial_call=True,
# )
# def func(n_clicks):
#     if n_clicks > 0:
#         return dcc.send_data_frame(bio_df.to_csv, "biosignature_data.csv")

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

@callback(
    Output("data-tab-buttons", "children"),
    Input("session-username", "data")
)
def generate_tab_buttons(session_user):
    if session_user['is_authorized'] == True and session_user['username'] == 'admin':
        df = data.read_database()
        return  [
                        html.Button(
                             "Validate data",
                             className="doc-link-download",
                             style = {'font-family': 'Arial, sans-serif', 'font-size': '1vw', 'order': '2', 'padding': '7px', 'margin-right': '12vw', 'margin-bottom': '-9vh', 'z-index': '1000'},
                             id = "btn-validate-data",
                             n_clicks= 0
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("What data do you wish to validate?"), style={'margin': 'auto'}),
                                dbc.ModalBody(children=[
                                    dash_table.DataTable(id='data-to-validate', columns = generate_data_to_validate(df)[1], data = generate_data_to_validate(df)[0], css = generate_data_to_validate(df)[2],
                                                         editable = False, style_data = {'color': 'black', 'font-family': 'Arial, sans serif'},
                                                         row_selectable = True,
                                                         selected_rows = [],
                                                         style_header= {'color': 'black', 'font-weight': 'bold', 'background-color': 'rgba(5, 8, 184, 0.4)', 'textAlign': 'left', 'font-family': 'Arial, sans serif'},
                                                         style_cell = {'textAlign': 'left', 'padding': '0px'},
                                                         style_table = {'order':'1', 'height':'20vh', 'width':'60vw', 'overflow': 'auto', 'margin': 'auto', 'margin-top': '3vh'}),
                                    html.Div(id='validate-data-modal-body', children = [], style = {'order':'2', 'display':'flex', 'flex-direction': 'column', 'align-items': 'center'}),
                                ], style = {'display':'flex', 'flex-direction': 'column', 'align-items': 'center'}),
                            ],
                            id="validate-pop-up",
                            size="xl",
                            style={'color': 'black', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'},
                            is_open=False,
                        ),
                        #dcc.Download(id="download-csv"),
                        html.A(
                                            "Submit new data", 
                                            href="/submit",
                                            className="doc-link-download",
                                            style = {'font-family': 'Arial, sans-serif', 'font-size': '1vw', 'order': '2', 'padding': '7px', 'margin-right': '12vw', 'margin-bottom': '-9vh', 'z-index': '1000'},
                                        )
                ]
    elif session_user['username'] == 'user':
        return [
            #dcc.Download(id="download-csv"),
            html.A(
                    "Submit new data", 
                    href="/submit",
                    className="doc-link-download",
                    style = {'font-family': 'Arial, sans-serif', 'font-size': '1vw', 'order': '2', 'padding': '7px', 'margin-right': '12vw', 'margin-bottom': '-9vh', 'z-index': '1000'},
                ),
                ]

@callback(
    Output('datatable-message', 'children'),
    Input('session-username', 'data')
)
def generate_message(data):
    if (data['is_authorized'] == True and data['username'] == 'admin') or (data['username'] == 'user'):
        return ['👋 Make sure to read the ',
                html.A("contribution guidelines", href="https://jhupiterz.notion.site/The-Biosignature-Database-f48effd1004f4155acfd76deee382436", target="_blank", style = {'color': '#a0a4e4', 'font-weight': 'bold'}),
                ' before submitting any new data']
    return ['👋 Log in for more features (top right corner)']

@callback(
    Output('validate-data-modal-body', 'children'),
    Input('data-to-validate', 'data'))
def generate_modal_mody(data_to_validate):
    if data_to_validate:
        return [html.Button(
                    "Validate data",
                    className="doc-link-validate",
                    style = {'font-family': 'Arial, sans-serif', 'font-size': '1vw', 'order': '1', 'margin-top': '3vh'},
                    id = "btn-validate-data-modal",
                    n_clicks= 0),
                html.P(id='validate-output', style={'order': '2', 'color': 'black', 'font-family': 'Arial, sans-serif', 'font-size': '20px', 'text-align': 'center', 'margin-top': '3vh'})]
    return "No pending data to validate"

@callback(
    Output('validate-output', 'children'),
    Input('data-to-validate', 'data'),
    Input('data-to-validate', 'selected_rows'),
    Input("btn-validate-data-modal", "n_clicks"),
    prevent_initial_call=True,
)
def func(data_to_validate, selected_rows, n_clicks):
    if n_clicks > 0:
        if data_to_validate:
            df_to_validate = pd.DataFrame(data_to_validate)
            for row in selected_rows:
                bio_id = df_to_validate.iloc[row]['biosignature_id']
                data.update_validated_data(bio_id)
            return [" ✅ Your data has been successfully validated.",html.Br(),"Close the pop-up window and refresh the page to see the changes."]
        return [" Choose which data entry to validate"]

@callback(
    Output('edit-pop-up-content', 'is_open'),
    Input('edit-data-btn', 'n_clicks'),
)
def generate_pop_up(n_clicks):
    if n_clicks > 0:
        return True