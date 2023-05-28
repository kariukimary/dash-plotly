#VISUALIZING THE DATA
#There are many cahrts in plotly that can be used to visualize the data lets use the histogram

#import packages
from dash import Dash,html,dash_table, dcc
import pandas as pd
import plotly.express as px

#loading the data
df=pd.read_csv("gapminder - gapminder.csv")

#intialize the app
app=Dash(__name__)

#app layout
app.layout=html.Div([html.Div(children='my first app with data and a graph'),
                     dash_table.DataTable(data=df.to_dict('records'),page_size=10),
                     dcc.Graph(figure=px.histogram(df, x='continent',y='life_exp',histfunc='avg'))
                    ])

#running the app
if __name__== '__main__':
    app.run_server(debug=True)