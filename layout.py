#import packages
from dash import Dash,html,dcc 
import pandas as pd
import plotly.express as px

#intialize the app
app=Dash(__name__)

#create a dataframe
df=pd.DataFrame({'fruits':['oranges','mangoes','apples','ovacados','peas'],
                 'amount':[5,2,7,4,9],
                 'city':['kenya','kenya','kenya','US','US']
})

#draw the bar graph
fig=px.bar(df,x='fruits',y='amount',color='city',barmode='group')

#app layout
app.layout=html.Div(children=[html.H1(children='viisualizing data'),
                               html.Div(children='''dash: a web application framework for your data'''),
                               dcc.Graph(id='example-graph',figure=fig)
])


#running the app
if __name__=='__main__':
    app.run_server(debug=True)