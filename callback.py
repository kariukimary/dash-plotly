#CONTROLS AND THE CALLBACK
# the callback functions are used  in adding controls such as radio buttons so as togive the app user the freedom to interact with the app and exlore data in graeter depths

#import packages
from dash import Dash, html,dcc,dash_table, callback , Input, Output
import pandas as pd
import plotly.express as px

#loading the data
df=pd.read_csv("gapminder - gapminder.csv")

#intialize the app
app=Dash(__name__)

#app layout
app.layout=html.Div([html.Div(children="my first app with data,Graph and controls"),
                     html.Hr(),
                     dcc.RadioItems(options=['population','life_exp','gdp_cap'],value='life_exp',id='controls-and-radio-item'),
                     dash_table.DataTable(data=df.to_dict('records'),page_size=6),
                     dcc.Graph(figure={},id='controls-and-graph')
                     ])

#add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item',component_property='value')
)
def update_graph(col_chosen):
    fig=px.histogram(df,x='continent',y=col_chosen, histfunc='avg')
    return fig

#run the app
if __name__ =='__main__':
    app.run_server(debug=True)
