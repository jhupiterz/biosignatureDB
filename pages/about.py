import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/about')

# layout = html.Div(children=[
#         dbc.Card(
#             [
#                 dbc.CardHeader(
#                     dbc.Tabs(
#                         [
#                             dbc.Tab(label="About the database", tab_id="database"),
#                             dbc.Tab(label="Data standards", tab_id="standards"),
#                             dbc.Tab(label="Contribution guidelines", tab_id="contribution"),
#                             dbc.Tab(label="Contact", tab_id="contact"),
#                         ],
#                         style = {'margin-top': '0.5vh', 'margin-left': '0.1vw'},
#                         id="about-tabs",
#                         active_tab="database",
#                     ), style= {'z-index': '1000'}
#                 ),
#                 dbc.CardBody(html.P(id="tab-content", className="card-text")),
#             ], style = {'z-index': 0}),

#     ], style={'z-index': '1'})

layout = html.Div([
            html.H1('About the database', style = {'text-align': 'left', 'color': 'black'}),
            html.P(children=['Thousands of research papers report on the detection and characterisation of potential biosignatures and abiosignatures in analogue environments on Earth, and fewer in extraterrestrial planetary contexts.',
                             ' Biosignatures are often defined as objects, substances, and/or patterns whose origin specifically requires a biological agent (Des Marais et al., 2003), whereas abiosignatures are non-biological signatures that mimic the signal of biosignatures (i.e. false positives).',
                             ' The results being scattered, it prevents any systematic, standardised reporting, or statistical analysis of the data.',
                             ' The vision of the Biosignature Database is to:',
                             html.Br(),
                             html.Br(),
                             html.Ol([
                                html.Li('Provide a centralised repository of biosignature and abiosignature data, with a standardised format for reporting and analysis.'),
                                html.Li('Enhance the collaboration among the astrobiology community by providing a platform for sharing data.'),
                                html.Li('Highlight research gaps by providing a visual representation of the distribution of the data.'),
                             ]),
                             html.Br(),
                             html.P(['For contribution guidelines and feature requests, please check out the ', html.A(children = ['Notion page'], href="https://alien-research.notion.site/The-Biosignature-Database-5165a9dff4e14b50ba1278c0f2012e3a", style = {'color': 'blue'}), '.']),
                             html.P(['For technical information about the Biosignature Database, please check out the ', html.A(children = ['white paper'], href="/assets/white_paper.pdf", style = {'color': 'blue'}), ' (work in progress, available soon).'])], style = {'width': '85vw','text-align': 'left', 'color': 'black', 'margin-left': '2vw'}),
                             html.H1('How it started', style = {'text-align': 'left', 'color': 'black'}),
            html.P(children = ['Hi! My name is Julie and I currently am a PhD student in Astrobiology at McMaster University in Hamilton, Canada. ',
                               'My research focuses on biosignatures and how to differentiate them from abiosignatures (i.e. abiotic mimics of biosignatures). ',
                               'While working on my research, I noticed that there was no standard reporting strategy for biosignature data. ',
                               "Being a coding and data science enthusiast, I decided to take on the challenge of creating the world's first Biosignature Database.",], style = {'width': '85vw','text-align': 'left', 'color': 'black', 'margin-left': '2vw'}),
            html.P(['To request more information, contribute to the data standards, request new features for the app, or to simply reach out please send an email to ', html.A(children = ['biosignature.database@gmail.com'], href="mailto:biosignature.database@gmail.com", style = {'color': 'blue'})], style = {'width': '85vw','text-align': 'left', 'color': 'black', 'margin-left': '2vw'})
            ]
        )

@callback(Output('tab-content', 'children'),
          Input('about-tabs', 'active_tab'))
def render_tab_content(tab_value):
    if tab_value == 'database':
        return html.Div([
            html.H1('About the database', style = {'text-align': 'left', 'color': 'black'}),
            html.P(children=['Thousands of research papers report on the detection and characterisation of potential biosignatures and abiosignatures in analogue environments on Earth, and fewer in extraterrestrial planetary contexts.',
                             ' Biosignatures are often defined as objects, substances, and/or patterns whose origin specifically requires a biological agent (Des Marais et al., 2003), whereas abiosignatures are non-biological signatures that mimic the signal of biosignatures (i.e. false positives).',
                             ' The results being scattered, it prevents any systematic, standardised reporting, or statistical analysis of the data.',
                             ' The vision of the Biosignature Database is to:',
                             html.Br(),
                             html.Br(),
                             html.Ol([
                                html.Li('Provide a centralised repository of biosignature and abiosignature data, with a standardised format for reporting and analysis.'),
                                html.Li('Enhance the collaboration among the astrobiology community by providing a platform for sharing data.'),
                                html.Li('Highlight research gaps by providing a visual representation of the distribution of the data.'),
                             ]),
                             html.Br(),
                             html.P(['For contribution guidelines and feature requests, please check out the ', html.A(children = ['Notion page'], href="https://alien-research.notion.site/The-Biosignature-Database-5165a9dff4e14b50ba1278c0f2012e3a", style = {'color': 'blue'}), '.'])], style = {'width': '85vw','text-align': 'left', 'color': 'black', 'margin-left': '2vw'}),
            html.H1('How it started', style = {'text-align': 'left', 'color': 'black'}),
            html.P(children = ['Hi! My name is Julie and I currently am a PhD student in Astrobiology at McMaster University in Hamilton, Canada. ',
                               'My research focuses on biosignatures and how to differentiate them from abiosignatures (i.e. abiotic mimics of biosignatures). ',
                               'While working on my research, I noticed that there was no standard reporting strategy for biosignature data. ',
                               "Being a coding and data science enthusiast, I decided to take on the challenge of creating the world's first Biosignature Database.",], style = {'width': '85vw','text-align': 'left', 'color': 'black', 'margin-left': '2vw'}),
            html.P(['To request more information, contribute to the data standards, request new features for the app, or to simply reach out please send an email to ', html.A(children = ['biosignature.database@gmail.com'], href="mailto:biosignature.database@gmail.com", style = {'color': 'blue'})], style = {'width': '85vw','text-align': 'left', 'color': 'black', 'margin-left': '2vw'})
            ]
        )
    elif tab_value == 'contribution':
        return html.Div([
            html.H1('Data contributions', style = {'text-align': 'center', 'color': 'black'}),
            html.P('Below are some generic guidelines to help contributors submit new data to the database and/or improve the code of the web application.', style = {'text-align': 'center', 'color': 'black'}),
            html.H1('App contributions', style = {'text-align': 'center', 'color': 'black'}),
            html.P('Contributions to the application include feature requests, back-end optimization, and UI/UX optimization.', style = {'text-align': 'center', 'color': 'black'})
            ]
        )
    elif tab_value == 'contact':
        return html.Div([
            html.H1('How it started', style = {'text-align': 'center', 'color': 'black'}),
            html.P(children = [
                                'To request more information, contribute to the data standards, request new features for the app (for non-tech users), or to simply reach out please send an email to biosignature.database@gmail.com.'
                            ], style = {'text-align': 'left', 'color': 'black'}),
            ]
        )