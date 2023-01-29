import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(children=[

    html.Div([
        html.Div(
            [
                html.H4(children='Explore the database',
                        style={
                            'order': '1',
                            'margin-bottom': '3vh',
                            'color': 'black',
                            'text-align': 'center'
                        }),
                html.A(href="/explore",
                       children=[
                           html.Img(alt="Dashboard",
                                    src="assets/explore.png",
                                    className="zoom")
                       ],
                       className="blog-post-1")
            ],
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
                'margin-right': '5vw'
            }),
        html.Div(
            [
                html.H4(children='Submit data',
                        style={
                            'order': '1',
                            'margin-bottom': '3vh',
                            'color': 'black',
                            'text-align': 'center'
                        }),
                html.A(href="/submit",
                       children=[
                           html.Img(alt="Submit",
                                    src="assets/submit.png",
                                    className='zoom')
                       ],
                       className="blog-post-1")
            ],
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
                'margin-right': '5vw'
            }),
        html.Div(
            [
                html.H4(children='About',
                        style={
                            'order': '1',
                            'margin-bottom': '3vh',
                            'color': 'black',
                            'text-align': 'center'
                        }),
                html.A(href="/about",
                       target = "_blank",
                       children=[
                           html.Img(alt="About the database",
                                    src="assets/about.png",
                                    className='zoom')
                       ],
                       className="blog-post-1")
            ],
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
                'margin-right': '5vw'
            })
    ],
             className="blog-posts"),
    
    html.Div(children=[html.H1("Welcome to the Biosignature Database", style = {'text-align': 'center', 'color': 'black', 'order': '1', 'font-size': '5.5vh'}),
                       html.P(['Developed and curated by ', html.A(html.U('Julie Hartz'), href="https://www.linkedin.com/in/julie-hartz-research/", style = {'color': 'black'}), ', PhD candidate at McMaster University, Canada.'], style = {'text-align': 'center', 'color': 'black', 'order': '2', 'font-size': '2vh', 'margin-top': '-2vh'})],
    style = {'background-color': '#e8d4fc', 'width': '100%', 'height': '40vh', 'padding-top': '12vh'}),
],
                  style={
                      'display': 'flex',
                      'flex-direction': 'column',
                      'justify-content': 'flex-start',
                      'height': '89vh',
                  })