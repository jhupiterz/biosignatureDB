import dash
import dash_auth
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__, suppress_callback_exceptions = True,
    external_stylesheets=[dbc.themes.LITERA],
    use_pages=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1", 'charSet':'“UTF-8”'}])

VALID_USERNAME_PASSWORD_PAIRS = {
    'guest-user': 'guest-password',
    'admin': 'admin-password'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

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
                    href="/",
                    target="_self",
                    className="logo-banner",
                ),
                html.Div([
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Explore", href="/"),
                        dbc.DropdownMenuItem("Submit new data", href='/submit'),
                        dbc.DropdownMenuItem("Documentation", href='https://jhupiterz.notion.site/The-Biosignature-Database-f48effd1004f4155acfd76deee382436', target = "_blank")
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Menu",
                    size = 'md',
                    className = 'menu'
                )])
            ],
            className="banner",
        ),

        dcc.Store(id='session-username', storage_type='session'),

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
    Input('session-username', 'storage_type')
)
def store_session_username(session):
    if session == 'session':
        authenticateduser = auth._username
        return {'username': authenticateduser}

# Runs the app ------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=True)