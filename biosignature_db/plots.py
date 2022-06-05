from folium import Marker
from matplotlib.pyplot import margins, title
import plotly.graph_objects as go
import plotly.express as px

def plot_interactive_map(df, projection):
    fig = px.scatter_geo(df, lat='latitude', lon='longitude',
                        size = 'number of samples',
                        color = 'max_age',
                        color_continuous_scale= px.colors.sequential.Viridis,
                        hover_name='location_name',
                        width= 600,
                        height= 600,
                        projection=projection)
    fig.update_layout(
                        showlegend=False,
                        coloraxis_colorbar=dict(
                                title="Age of samples",
                                thicknessmode="pixels", thickness=30,
                                lenmode="pixels", len=485,
                                ticks="outside", ticksuffix=" years"
                            ),
                        margin=dict(l=0, r=0, t=0, b=0),
                        paper_bgcolor = "rgba(0, 0, 0, 0)",
                        plot_bgcolor = "rgba(60, 25, 240, 0.1)")
    return fig

def plot_bar_chart(df, lat, lon, loc):
    colorscheme = ['#1f9e89','#fde725', '#b5de2b',
                    '#35b779','#26828e','#3e4989']
    fig = px.bar(df.loc[lat, lon, loc].reset_index(), x='biosignature_cat',
                 y='number of samples', color='biosignature_subcat', color_discrete_sequence= colorscheme,
                 width=400, height=250)
    fig.update_yaxes(visible=False)
    fig.update_xaxes(title='')
    fig.update_layout(
        margin=dict(l=1, r=1, t=30, b=0),
        paper_bgcolor='white',
        legend={'title_text':''},
        plot_bgcolor='white',
        title_text= 'Types of biosignatures',
        title_x = 0.5)
    return fig

def plot_pie_chart(df, lat, lon, loc):
    colorscheme = ['#1f9e89','#fde725', '#b5de2b',
                    '#35b779','#26828e','#3e4989']
    fig = px.pie(df.loc[lat, lon,loc].reset_index(drop=True), color_discrete_sequence= colorscheme,
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
