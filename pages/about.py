import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/about')

layout = html.Div(children=[
        dbc.Card(
            [
                dbc.CardHeader(
                    dbc.Tabs(
                        [
                            dbc.Tab(label="About the database", tab_id="database"),
                            dbc.Tab(label="Data standards", tab_id="standards"),
                            dbc.Tab(label="How it started", tab_id="started"),
                        ],
                        style = {'margin-top': '0.5vh', 'margin-left': '0.1vw'},
                        id="about-tabs",
                        active_tab="database",
                    ), style= {'z-index': '1000'}
                ),
                dbc.CardBody(html.P(id="tab-content", className="card-text")),
            ], style = {'z-index': 0}),

    ], style={'z-index': '1'})

@callback(Output('tab-content', 'children'),
          Input('about-tabs', 'active_tab'))
def render_tab_content(tab_value):
    if tab_value == 'database':
        return html.Div([
            html.H1('About the database', style = {'text-align': 'left', 'color': 'black'}),
            html.P(children=['Thousands of research papers report on the detection and characterisation of biosignatures in analogue environments on Earth, and fewer in extraterrestrial planetary contexts.',
                             'The results being scattered, it prevents any systematic and standardised reporting and statistical analysis of the data.',
                             'The vision of the Biosignature Database is to:',
                             html.Br(),
                             html.Ul([
                                html.Li('Provide a centralised repository of biosignature data, with a standardised format for reporting and analysis.'),
                                html.Li('Enhance the collaboration among the astrobiology community by providing a platform for sharing data.'),
                                html.Li('Highlight research gaps by providing a visual representation of the distribution of the data.'),
                             ])], style = {'text-align': 'left', 'color': 'black'}),
                             html.Br(),
            html.P('To request more information, contribute to the data standards, request new features for the app, or to simply reach out please send an email to biosignature.database@gmail.com.', style = {'text-align': 'left', 'color': 'black'})
            ]
        )
    elif tab_value == 'standards':
        return html.Div([
            html.H1('Data standards', style = {'text-align': 'center', 'color': 'black'}),
            html.P('The Biosignature Database aims to act as a repository of standardized data on biosignatures. ', style = {'text-align': 'center', 'color': 'black'}),
            ]
        )
    elif tab_value == 'started':
        return html.Div([
            html.H1('How it started', style = {'text-align': 'center', 'color': 'black'}),
            html.P(children = ['Hi! My name is Julie and I currently am a PhD student in Astrobiology at McMaster University in Hamilton, Canada. ',
                               'My research focuses on biosignatures and how to differentiate them from abiosignatures (i.e. abiotic mimics of biosignatures). ',
                               'While working on my research, I noticed that there was no standard reporting strategy for biosignture data. ',
                               "Being a coding and data science enthusiast, I decided to take on the challenge of creating the world's first Biosignature Database.",
                            ], style = {'text-align': 'center', 'color': 'black'}),
            ]
        )