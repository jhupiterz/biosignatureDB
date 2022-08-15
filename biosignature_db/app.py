import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from biosignature_db import user_profile

user_profile = user_profile.UserProfile()

app = dash.Dash(
    __name__, suppress_callback_exceptions = True,
    external_stylesheets=[dbc.themes.LITERA],
    use_pages=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1", 'charSet':'“UTF-8”'}])

app.title = "biosignature database"

admin_username_input = dbc.Col(
    [
        dbc.Label("Username", html_for="example-email-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text", value="admin", id="admin-username", placeholder="admin", step=1
            ),
            width=8,
        )
    ],
    className="mb-3",
)

admin_password_input = dbc.Col(
    [
        dbc.Label("Password", html_for="example-email-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="password", id="admin-password", placeholder="enter password", step=1
            ),
            width=10,
        )
    ],
    className="mb-3",
)

login_btn = dbc.Button("log in", id="login-btn", color="primary", n_clicks=0, style = {'margin-top': '1vh'})

dropdown_not_logged_in = dcc.Dropdown(id='dropdown-not-logged-in', options=['Log in'], placeholder='🟠 Not logged in',
                                      clearable=False, searchable=False,
                                      className='dropdown-not-logged-in')

dropdown_user_logged_in = dcc.Dropdown(id='dropdown-user-logged-in', options=['Log out'], placeholder='🟢 User',
                                       clearable=False, searchable=False,
                                       className='dropdown-user-logged-in')

dropdown_admin_logged_in = dcc.Dropdown(id='dropdown-admin-logged-in', options=['Log out'], placeholder='🟢 Admin',
                                        clearable=False, searchable=False,
                                        className='dropdown-admin-logged-in')

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
                    html.A('Documentation', href='https://jhupiterz.notion.site/jhupiterz/The-Biosignature-Database-f48effd1004f4155acfd76deee382436', className="menu-link", style = {'order': '3', 'margin-right': '2vw'}),
                    html.Div(id='login-dropdown', style={'order': '4'})
                ], className = "menu"),
            ],
            className="banner",
        ),

        dcc.Store(id='session-username', data = {'username': user_profile.username,
                                                 'is_authorized': user_profile.is_authorized},
                                         storage_type='session'),
        
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("How do you wish to log in?"), style={'margin': 'auto'}),
                dbc.ModalBody(children=[
                                    html.Div(id='login-popup-content', children = [
                                        html.Button(id='user-login-button', children=["Login as user"], n_clicks=0, className='btn btn-primary', style={'margin-right': '1vw'}),
                                        html.Button(id='admin-login-button', children=["Login as admin"], n_clicks=0, className='btn btn-primary', style={'margin-left': '1vw'})
                                    ], style = {'display':'flex', 'flex-direction':'row', 'align-items':'center', 'margin': 'auto'}),
                                ], style = {'margin': 'auto'})
            ],
            id="login-popup",
            size="lg",
            style={'color': 'black', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'},
            is_open=False,
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Enter admin credentials"), style={'margin': 'auto'}),
                dbc.ModalBody(children=[
                    admin_username_input,
                    admin_password_input,
                    login_btn
                ])
            ],
            id='admin-login-modal',
            size="lg",
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
    Output('session-username', 'data'),
    Input('admin-login-button', 'n_clicks'),
    Input('user-login-button', 'n_clicks'),
    Input('admin-password', 'value'),
    Input('login-btn', 'n_clicks'),
    prevent_initial_call=True
)
def login_as_user(n_clicks_admin, n_clicks_user, admin_password, n_clicks_login):
    if admin_password != None:
        if n_clicks_login > 0:
            user_profile.test_admin_password(admin_password)
            if user_profile.is_authorized:
                return {'username': user_profile.username,
                        'is_authorized': user_profile.is_authorized}
    else:
        if n_clicks_user > 0:
            user_profile.login_as_user()
            return {'username': user_profile.username,
                    'is_authorized': user_profile.is_authorized}
        if n_clicks_admin > 0:
            user_profile.login_as_admin()
            return {'username': user_profile.username,
                    'is_authorized': user_profile.is_authorized}

@app.callback(
    Output('admin-login-modal', 'is_open'),
    Input('session-username', 'data'),
    prevent_initial_call=True
)
def generate_admin_login(data):
    if data['is_authorized'] == True:
        return False
    elif data['username'] == 'user':
        return False
    return True

@app.callback(
    Output('login-popup', 'is_open'),
    Input('session-username', 'data'),
    Input('dropdown-not-logged-in', 'value'),
    prevent_initial_call=True
)
def login(data, value):
    username = data['username']
    if username == 'user' or username == 'admin':
        return False
    if value == 'Log in':
        return True

@app.callback(
    Output('login-dropdown', 'children'),
    Input('session-username', 'data'),
)
def generate_login_dropdown(data):
    if data['username'] == 'user':
        return dropdown_user_logged_in
    elif data['username'] == 'admin' and data['is_authorized'] == True:
        return dropdown_admin_logged_in
    else:
        return dropdown_not_logged_in

# Runs the app ------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=True)