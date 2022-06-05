from folium import Marker
from matplotlib.pyplot import margins, title
import plotly.graph_objects as go
import plotly.express as px

def plot_interactive_map(df, projection):
    fig = px.scatter_geo(df, lat='latitude', lon='longitude',
                        size = 'number of samples',
                        hover_name='location_name',
                        width= 600,
                        height= 600,
                        projection=projection)
    fig.update_layout(
                        showlegend=False,
                        margin=dict(l=0, r=0, t=0, b=0),
                        paper_bgcolor = "rgba(0, 0, 0, 0)",
                        plot_bgcolor = "rgba(60, 25, 240, 0.1)")
    return fig

def plot_bar_chart(df, lat, lon, loc):
    fig = px.bar(df.loc[lat, lon, loc].reset_index(), x='biosignature_cat',
                 y='number of samples', width=300, height=200)
    fig.update_yaxes(visible=False)
    fig.update_xaxes(title='')
    fig.update_layout(
        margin=dict(l=1, r=1, t=30, b=0),
        paper_bgcolor='white',
        plot_bgcolor='white',
        title_text= 'Types of biosignatures',
        title_x = 0.5)
    return fig

def plot_pie_chart(df, lat, lon, loc):
    fig = px.pie(df.loc[lat, lon,loc].reset_index(drop=True),
                     values = 'number of samples', names='detection_methods',
                     width=300, height=300)
    fig.update_layout(
        margin=dict(l=1, r=1, t=30, b=0),
        paper_bgcolor='white',
        plot_bgcolor='white',
        title_text= 'Detection methods',
        title_x = 0.5,
        legend=dict(
                    y=0.5,
                    x=1
                ))
    return fig
