#import packages
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


#intialize the app
app=Dash(__name__)

#loading the data
df=pd.read_csv("gapminder - gapminder.csv")

#drawing the scatter plot
fig=px.scatter(df,x='gdp_cap',y='life_exp',size='population',color='continent',
               hover_name='country',log_x=True,size_max=60)

#app layout
app.layout=html.Div([dcc.Graph(id='life_exp_vs_gdp',figure=fig)
])

#run the app
if __name__=='__main__':
    app.run_server(debug=True)

