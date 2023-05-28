#STYLING YOUR APP
#You can style your app so as to look more professional
#there are multiple tools taht can be used in styling your app such as Html and css,dash design kit,dash bootstrapp components and dash mantime components

#import packages
from dash import Dash, html, dash_table,dcc, callback,Input, Output
import pandas as pd
import plotly.express as px

#loading the data
df=pd.read_csv("gapminder - gapminder.csv")

#intializing the app/incorporating the stylesheet
external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app=Dash(__name__, external_stylesheets= external_stylesheets)

#styling our app
#app layout 

#STYLING THE TITLE NAME
app.latout=html.Div([
    html.Div(className='row',children='my first app with data graph and controls',
             style={'textalign':'center','color':'pink','font_size':30}),
    
    html.Div(className='row',children=[
        dcc.RadioItems(options=['population','life_exp','gdp_cap'],
                       value='life_exp',
                       inline=True,
                       id='my-radio-buttons-final')
     ]),
    html.Div(className='row',children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'),page_size=11, style_table={'overflowX':'auto'})
        ]),
        html.Div(className='six columns',children=[
            dcc.Graph(figure={}, id='hist-chart-final')
        ])
    ])
])
        

@callback(
    Output(component_id='histo-chart-final',component_property='figure'),
    Input(component_id='my-radio-button-final',component_property='value')
)
def update_graph(col_chosen):
    fig=px.histogram(df,x='continent',y=col_chosen,histfunc='avg')
    return fig

#running the app
if  __name__=='__main__':
    app.run_server(debug=True)