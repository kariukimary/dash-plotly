#CONNECTING TO THE DATA
# there are amny ways to add data to an appsuch as APIs,external databases,local txtfiles etc
#import packages
from dash import Dash, html, dash_table
import pandas as pd

#incorporate data
df=pd.read_csv("gapminder - gapminder.csv")

#intialize the app
app=Dash(__name__)

#app layout
app.layout=html.Div([html.Div(children='my first app with data'),
                     dash_table.DataTable(data=df.to_dict('records'))
                     ])

#run the app
if __name__ == '__main__':
    app.run_server(debug=True)
