import dash
from dash import html
import dash_bootstrap_components as dbc

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

# Runs the app ------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=True)

# html.Button(
#                             "Download data",
#                             className="doc-link-download",
#                             id = "btn-download-data",
#                             n_clicks= 0
#                         ),
#                         dcc.Download(id="download-csv")