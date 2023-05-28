import plotly.express as px

def plot_interactive_map(df, projection):
    fig = px.scatter_geo(df, lat='latitude', lon='longitude',
                        size = 'number of samples',
                        color = 'max_age',
                        color_continuous_scale= px.colors.sequential.Viridis,
                        hover_name='location_name',
                        width= 650,
                        height= 650,
                        projection=projection)
    fig.update_layout(
                        showlegend=False,
                        coloraxis_colorbar=dict(
                                title="Age of samples",
                                thicknessmode="pixels", thickness=30,
                                lenmode="pixels", len=535,
                                ticks="outside", ticksuffix=" years"
                            ),
                        margin=dict(l=0, r=0, t=0, b=0),
                        paper_bgcolor = "rgba(0, 0, 0, 0)",
                        plot_bgcolor = "rgba(0, 0, 0, 0)")
    return fig

def plot_bar_chart(df, lat, lon, loc):
    colorscheme = ['#1f9e89','#fde725', '#b5de2b',
                    '#35b779','#26828e','#3e4989']
    fig = px.bar(df.loc[lat, lon, loc].reset_index(), x='biosignature_cat',
                 y='number of samples', color='biosignature_subcat', color_discrete_sequence= colorscheme,
                 width=320, height=250)
    fig.update_yaxes(visible=False)
    fig.update_xaxes(title='')
    fig.update_layout(
        margin=dict(l=1, r=1, t=30, b=0),
        paper_bgcolor='rgba(0, 0, 0, 0)',
        legend={'title_text':''},
        plot_bgcolor='rgba(0, 0, 0, 0)',
        title_text= 'Types of biosignatures',
        title_x = 0.5)
    return fig

def plot_pie_chart(df, lat, lon, loc):
    colorscheme = ['#1f9e89','#fde725', '#b5de2b',
                    '#35b779','#26828e','#3e4989']
    fig = px.pie(df.loc[lat, lon,loc].reset_index(drop=True), color_discrete_sequence= colorscheme,
                     values = 'number of samples', names='detection_methods',
                     width=320, height=320)
    fig.update_layout(
        margin=dict(l=1, r=1, t=30, b=0),
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        title_text= 'Detection methods',
        title_x = 0.5,
        legend=dict(
                    y=0.5,
                    x=1
                ))
    return fig

# def generate_mars_map(lat,lon):
#     fig = plt.figure(figsize=(12, 12))
#     img_extent = (-180, 180, -90, 90)

#     img = plt.imread('assets/mars.png')

#     ax = plt.axes(projection=ccrs.Mercator())
#     ax.imshow(img, origin='upper', extent=img_extent)
#     ax.set_xmargin(0.05)
#     ax.set_ymargin(0.10)
#     ax.gridlines()
#     plt.scatter(lat,lon, s= 30, c='black', marker= '')
#     plt.imsave(projections = ccrs.Mercator(), fname= 'assets/mars_loc.png', arr = img)