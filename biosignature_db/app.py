import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from biosignature_db import user_profile

user_profile = user_profile.UserProfile()
print(f"INITIAL: {user_profile.username}, {user_profile.password}")

app = dash.Dash(
    __name__, suppress_callback_exceptions = True,
    external_stylesheets=[dbc.themes.LITERA],
    use_pages=True,
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
                        html.H3("biosignature database")
                    ],
                    href="/",
                    target="_self",
                    className="logo-banner",
                ),
                html.Div([
                    html.A('Explore', href='/', className="menu-link",  style = {'order': '1', 'margin-right': '2vw'}),
                    html.A('Submit new data', href='/submit', className="menu-link", style = {'order': '2', 'margin-right': '2vw'}),
                    html.A('Documentation', href='https://jhupiterz.notion.site/jhupiterz/The-Biosignature-Database-f48effd1004f4155acfd76deee382436', className="menu-link", style = {'order': '3'}),
                ], className = "menu"),
            ],
            className="banner",
        ),

        dcc.Store(id='session-username', data = {'username': user_profile.username,
                                                 'password': user_profile.password,
                                                 'is_authorized': user_profile.is_authorized},
                                         storage_type='session'),
        
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("You need to login"), style={'margin': 'auto'}),
                dbc.ModalBody(children=[
                                    html.Div(id='login-popup-content', children = [
                                        html.Button(id='user-login-button', children=["Login as user"], n_clicks=0, className='btn btn-primary'),
                                        html.Button(id='admin-login-button', children=["Login as admin"], n_clicks=0, className='btn btn-primary')
                                    ], style = {'display':'flex', 'flex-direction':'row', 'align-items':'center', 'margin': 'auto'}),
                                ], style = {'margin': 'auto'})
            ],
            id="login-popup",
            size="sm",
            style={'color': 'black', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'},
            is_open=False,
        ),

        # Main content ----------------------------------------------------------
        html.Div([]),
        dash.page_container,
        
        # Footer ----------------------------------------------------------------
        html.Footer(
            [
                html.P(
                    [
                        "Built with ", 
                        html.A("Plotly Dash", href="https://plotly.com/dash/", target="_blank")
                    ], style = {'height': '3vh', 'padding-top': '0vh'}
                )
            ]
        )
    ],
    className="app-layout",
    )

@app.callback(
    Output('login-popup', 'is_open'),
    Input('session-username', 'data')
)
def store_session_username(data):
    print(f"CALLBACK: {data}")
    username = data['username']
    if username == '':
        return True

@app.callback(
    Output('session-username', 'data'),
    Input('admin-login-button', 'n_clicks'),
    Input('user-login-button', 'n_clicks'),
    prevent_initial_call=True
)
def login_as_user(n_clicks_admin, n_clicks_user):
    if n_clicks_user > 0:
        user_profile.login_as_user()
        return {'username': user_profile.username,
                'password': user_profile.password,
                'is_authorized': user_profile.is_authorized}
    if n_clicks_admin > 0:
        user_profile.login_as_admin()
        return {'username': user_profile.username,
                'password': user_profile.password,
                'is_authorized': user_profile.is_authorized}

# Runs the app ------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=True)