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
    'guest': 'guest',
    'admin': 'admin'
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
                        html.H3("biosignature database")
                    ],
                    href="/",
                    target="_self",
                    className="logo-banner",
                ),
                html.Div([
                    html.A('Explore', href='/explore', className="menu-link",  style = {'order': '1', 'margin-right': '2vw'}),
                    html.A('Submit new data', href='/submit', className="menu-link", style = {'order': '2', 'margin-right': '2vw'}),
                    html.A('Documentation', href='https://jhupiterz.notion.site/jhupiterz/The-Biosignature-Database-f48effd1004f4155acfd76deee382436', className="menu-link", style = {'order': '3'}),
                ], className = "menu"),
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