import pandas as pd
import dash
from dash import html, callback, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from biosignature_db import data

dash.register_page(__name__)

bio_id_input = dbc.Row(
    [
        dbc.Label("Biosignature ID", html_for="example-email-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number", id="bio-id-row", placeholder="E.g. 24"
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

bio_cat_input = dbc.Row(
    [
        dbc.Label("Biosignature category", html_for="example-password-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="bio-cat-row",
                placeholder="E.g. organics",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

bio_subcat_input = dbc.Row(
    [
        dbc.Label("Biosignature sub-category", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="bio-subcat-row",
                placeholder="E.g. biomarker",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

name_input = dbc.Row(
    [
        dbc.Label("Biosignature name", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="name-row",
                placeholder="E.g. n-alkanes",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

indicative_input = dbc.Row(
    [
        dbc.Label("Indicative of", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="indicative-row",
                placeholder="E.g. cyanobacteria",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

methods_input = dbc.Row(
    [
        dbc.Label("Detection methods", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="methods-row",
                placeholder="E.g. gc-ms",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

sample_type_input = dbc.Row(
    [
        dbc.Label("Sample type", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="sample-type-row",
                placeholder="E.g. geological",
            ),
            width=3,
        ),
        dbc.Label("Number of samples", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="n-samples-row",
                placeholder="E.g. 3",
            ),
            width=3,
        )
    ],
    className="mb-3",
)

sample_subtype_input = dbc.Row(
    [
        dbc.Label("Sample subtype", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="sample-subtype-row",
                placeholder="E.g. sedimentary",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

min_age_input = dbc.Row(
    [
        dbc.Label("Min. age (years)", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="min-age-row",
                placeholder="E.g. 3500000",
            ),
            width=3,
        ),
        dbc.Label("Max. age (years)", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="max-age-row",
                placeholder="E.g. 1000",
            ),
            width=3,
        )
    ],
    className="mb-3",
)

pub_ref_input = dbc.Row(
    [
        dbc.Label("Pub. reference", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="pub-ref-row",
                placeholder="E.g. Teece et al. (2020)",
            ),
            width=3,
        ),
        dbc.Label("Pub. year", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="pub-year-row",
                placeholder="E.g. 2020",
            ),
            width=3,
        )
    ],
    className="mb-3",
)

pub_url_input = dbc.Row(
    [
        dbc.Label("Publication URL", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="pub-url-row",
                placeholder="Enter the publication URL",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

env_input = dbc.Row(
    [
        dbc.Label("Environment", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="env-row",
                placeholder="E.g. hydrothermal",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

paleo_input = dbc.Row(
    [
        dbc.Label("Paleoenvironment", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="paleo-row",
                placeholder="E.g. silica hot-springs",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

location_input = dbc.Row(
    [
        dbc.Label("Location", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="location-row",
                placeholder="E.g. Taupo Volcanic Zone",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

coord_input = dbc.Row(
    [
        dbc.Label("Latitude", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="lat-row",
                placeholder="E.g. 3500000",
            ),
            width=3,
        ),
        dbc.Label("Longitude", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="lon-row",
                placeholder="E.g. 1000",
            ),
            width=3,
        )
    ],
    className="mb-3",
)

mars1_input = dbc.Row(
    [
        dbc.Label("Mars counterpart (1)", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="mars1-row",
                placeholder="E.g. Columbia Hills",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

coord1_input = dbc.Row(
    [
        dbc.Label("Mars latitude (1)", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="lat1-row",
                placeholder="E.g. 3500000",
            ),
            width=3,
        ),
        dbc.Label("Mars longitude (1)", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="lon1-row",
                placeholder="E.g. 1000",
            ),
            width=3,
        )
    ],
    className="mb-3",
)

mars2_input = dbc.Row(
    [
        dbc.Label("Mars counterpart (2)", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="mars2-row",
                placeholder="E.g. Columbia Hills",
            ),
            width=5,
        ),
    ],
    className="mb-3",
)

coord2_input = dbc.Row(
    [
        dbc.Label("Mars latitude (2)", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="lat2-row",
                placeholder="E.g. 3500000",
            ),
            width=3,
        ),
        dbc.Label("Mars longitude (2)", html_for="example-radios-row", width=3, color="black"),
        dbc.Col(
            dbc.Input(
                type="number",
                id="lon2-row",
                placeholder="E.g. 1000",
            ),
            width=3,
        )
    ],
    className="mb-3",
)

layout = html.Div(children=[
    dcc.Store(id='store-biosignature', data = data.read_json_data('data/biosignature.json'), storage_type = 'memory'),
    html.H1(children="You're about to submit new data!", style = {'color': 'black'}),
    html.Div([
        html.P(children=["👏 Thank you for willing to contribute to the biosignature database.",
                        "The purpose of this project is to have as much data as possible on (potential) biosignatures.\n","However, data only makes sense if it is consistent and of good quality.",
                        "\n⚠️ PLEASE, once again make sure to read the ",
                        html.A("contribution guidelines", href="https://jhupiterz.notion.site/The-Biosignature-Database-f48effd1004f4155acfd76deee382436", target="_blank", style = {'color': 'blue', 'font-weight': 'bold'}),
                        " before submitting any new data."], style = {'color': 'black', 'font-family': 'Arial, sans-serif', 'margin': 'auto', 'text-align': 'center', 'padding-top': '2vh'})],
            style = {'width': '75vw', 'height': '13vh', 'margin': 'auto', 'backgroundColor': '#e6e6e6', 'border-radius': '10px'}),
    
    dbc.Form([bio_id_input, bio_cat_input, bio_subcat_input,
              name_input, indicative_input, methods_input,
              sample_type_input, sample_subtype_input, min_age_input,
              pub_ref_input, pub_url_input, env_input, paleo_input,
              location_input, coord_input, mars1_input, coord1_input,
              mars2_input, coord2_input], style={'width': '60vw', 'margin': 'auto', 'margin-top': '2vh'}),
    
    html.Hr(style={'borderWidth': "1vh", "width": "60vw", "color": "grey", "margin": "auto", "margin-top": "5vh"}),
    
    html.Div([
        dbc.Col(dbc.Button("Submit data", id="submit-data", color="primary", n_clicks=0), width="10vw", style={'order':'1','margin': 'auto', 'margin-left':'0px', 'height': '8vh'}),
        html.P(id='submit-output', style={'order': '2', 'color': 'black', 'font-family': 'Arial, sans-serif', 'font-size': '26px', 'margin-left': '2vw'})
        ], style = {'display': 'flex', 'flex-direction': 'row', 'justify-content': 'flex-start', 'align-items': 'center', 'margin':'auto',  'margin-top': '2vh', 'margin-bottom': '2vh', 'width': '60vw'}),

    ])

@callback(Output('submit-output', 'children'),
          Input('bio-id-row', 'value'),
          Input('bio-cat-row', 'value'),
          Input('bio-subcat-row', 'value'),
          Input('name-row', 'value'),
          Input('indicative-row', 'value'),
          Input('methods-row', 'value'),
          Input('sample-type-row', 'value'),
          Input('sample-subtype-row', 'value'),
          Input('min-age-row', 'value'),
          Input('max-age-row', 'value'),
          Input('pub-url-row', 'value'),
          Input('paleo-row', 'value'),
          Input('n-samples-row', 'value'),
          Input('env-row', 'value'),
          Input('location-row', 'value'),
          Input('lat-row', 'value'),
          Input('lon-row', 'value'),
          Input('mars1-row', 'value'),
          Input('lat1-row', 'value'),
          Input('lon1-row', 'value'),
          Input('mars2-row', 'value'),
          Input('lat2-row', 'value'),
          Input('lon2-row', 'value'),
          Input('pub-ref-row', 'value'),
          Input('pub-year-row', 'value'),
          Input('store-biosignature', 'data'), 
          Input('submit-data', 'n_clicks'))
def send_data_to_validation(bio_id, bio_cat, bio_subcat, name, indicative,
                            methods, sample_type, sample_subtype, min_age, max_age,
                            pub_url, paleo, n_samples, env, location, lat, lon, mars1,
                            lat1, lon1, mars2, lat2, lon2, pub_ref, pub_year, data, n_clicks):
    if n_clicks > 0:
        df = pd.DataFrame(data)
        data_status = '🟠 pending'
        df.loc[len(df.index)] = [bio_id, bio_cat, bio_subcat, name, indicative, methods, sample_type, sample_subtype,
                                n_samples, min_age, max_age, env, paleo, location, lat, lon, mars1, lat1, lon1, mars2, lat2, lon2, pub_ref, pub_year, pub_url, data_status]
        df.to_json('data/biosignature.json', orient='records')
        n_clicks = 0
        return " ✅ Your data has been submitted and will shortly be validated"