#dash core component includes sets of high level components like dropdowns,checkboxes,buttons
from dash import Dash, html, dcc

#intialize the app
app=Dash(__name__)

#app layout
app.layout=html.Div([html.Div(children=[html.Label('dropdown'),
                                        dcc.Dropdown(['c language','css','python','java'],'python'),
                                        
                                        html.Br(),
                                        html.Label('multi-seleted Dropdown'),
                                        dcc.Dropdown(['c language','css','python','java'],
                                                     ['python','c language'],
                                                     multi=True),
                                        
                                        html.Br(),
                                        html.Label('checkboxes'),
                                        dcc.Checklist(['deep  learning','tensorflow','keras','pytorch'],
                                                     ['deep learning','tensorflow']),
                                        
                                        html.Br(),
                                        html.Label('text input'),
                                        dcc.Input(value='mary',type='text'),
                                        
                                        html.Br(),
                                        html.Label('radio items'),
                                        dcc.RadioItems(['machine learning','deep learning','technical'],'deep learning'),
                                        ],style={'padding':10, 'flex':1})
                     ])
if __name__=='__main__':
    app.run_server(debug=True)