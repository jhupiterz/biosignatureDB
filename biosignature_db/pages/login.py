# import dash
# from dash import html, dcc, callback, Input, Output
# import dash_bootstrap_components as dbc

# dash.register_page(__name__, path='/login')

# admin_username_input = dbc.Col(
#     [
#         dbc.Label("Username", html_for="example-email-row", width=3, color="black"),
#         dbc.Col(
#             dbc.Input(
#                 type="text", value="admin", id="admin-username", placeholder="admin", step=1
#             ),
#             width=8,
#         ),
#     ],
#     className="mb-3",
# )

# admin_password_input = dbc.Col(
#     [
#         dbc.Label("Password", html_for="example-email-row", width=3, color="black"),
#         dbc.Col(
#             dbc.Input(
#                 type="text", id="admin-password", placeholder="enter password", step=1
#             ),
#             width=10,
#         ),
#     ],
#     className="mb-3",
# )

# login_btn = dbc.Button("log in", id="login-btn", color="primary", n_clicks=0, style = {'margin-top': '1vh'})

# layout = html.Div(children=[
#     html.H1('Log in as', style={'text-align': 'center', 'color': 'black'}),
#         html.Div(children=[
#                 html.A(
#                     [
#                         html.Img(
#                             src="/assets/user.png",
#                             alt="user",
#                             className='profile-image'
#                         )
#                     ],
#                     id='user-image',
#                     href="/explore",
#                     target="_self",
#                     n_clicks=0
#                 ),
#                 html.Button(
#                     [
#                         html.Img(
#                             src="/assets/admin.png",
#                             alt="user",
#                             className='profile-image'
#                         )
#                     ],
#                     id='admin-button',
#                     n_clicks=0
#                 ),
#                 dcc.Store(id='session-username', storage_type='session'),
#                 dbc.Modal(
#                             [
#                                 dbc.ModalHeader(dbc.ModalTitle("Login as admin"), style={'margin': 'auto'}),
#                                 dbc.ModalBody(children=[
#                                     html.Div(id='admin-credentials-content', children = [
#                                         admin_username_input,
#                                         admin_password_input,
#                                         login_btn
#                                     ], style = {'display':'fley', 'flex-direction':'column', 'align-items':'center','margin': 'auto'}),
#                                 ], style = {'margin': 'auto'}),
#                             ],
#                             id="admin-credentials",
#                             size="sm",
#                             style={'color': 'black', 'font-family': 'Arial, sans-serif', 'font-size': '1.5vw'},
#                             is_open=False,
#                         )
#         ], style={'display': 'flex', 'flex-direction':'row', 'justify-content':'center', 'align-items':'center', 'margin-top': '-5vw'})
#     ])

# @callback(
#     Output('session-username', 'data'),
#     Input('user-image', 'n_clicks'),
#     Input('admin-button', 'n_clicks')
# )
# def assign_profile(n_clicks_user, n_clicks_admin):
#     if n_clicks_user > 0:
#         authenticateduser = 'user'
#         return {'username': authenticateduser}
#     elif n_clicks_admin > 0:
#         authenticateduser = 'admin'
#         return {'username': authenticateduser}

# @callback(
#     Output('admin-credentials', 'is_open'),
#     Input('session-username', 'data'))
# def generate_login_popup(username):
#     if username['username'] == 'admin':
#         return True

# # @callback(
# #     Output('session-username', 'data'),
# #     Input('login-btn', 'n_clicks'),
# #     Input('admin-username', 'value'),
# #     Input('admin-password', 'value')
# # )
# # def login_admin(n_clicks, username, password):
# #     if n_clicks > 0:
# #         if username == 'admin' and password == 'admin':
# #             authenticateduser = 'admin'
# #             return {'username': authenticateduser}
# #         else:
# #             return {'username': authenticateduser}