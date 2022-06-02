from folium import Marker
import plotly.graph_objects as go
import plotly.express as px

def plot_interactive_map(df, projection):
    fig = px.scatter_geo(df, lat='latitude', lon='longitude',
                        size = 'biosignature_id',
                        hover_name='location_name',
                        width= 800,
                        height= 800,
                        projection=projection)
    fig.update_layout(
                        showlegend=False,
                        paper_bgcolor = "rgba(0, 0, 0, 0)",
                        plot_bgcolor = "rgba(60, 25, 240, 0.1)")
    return fig