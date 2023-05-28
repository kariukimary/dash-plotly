#DASH DESIGN KIT(ddk)
#it is the higher level framework for dash,ddk makes the app to be rensponsible by default and everything is themeable
from dash import Dash, html, dash_table,  callback, Input, Output,dcc
import pandas as pd
import plotly.express as px
import dash_design_kit as ddk

#load the data
df=pd.read_csv("gapminder - gapminder.csv")

#app intialization
app=Dash(__name__)

#app layout
app.layout=ddk.App([
    ddk.Header(ddk.Ttitle("my first app with data,graph and control")),
    dcc.RadioItems(options=['population','life_exp','gdp_cap'],
                   value='life_exp',
                   inline=True,
                   id='my-ddk-radio-items-final'),
    ddk.row([
        ddk.card([
            dash_table.DataTable(data=df.to_dict('records'),page_size=12,style_table={'overflowX':'auto'})
        ],width=50),
        ddk.card([
            ddk.graph(figure={},id='graph-placeholder-ddk-final')
        ],width=50),
    ])
                  
             ])
@callback(
    Output(component_id='graph-placeholder-ddk-final',component_property='figure'),
    Input(component_id='my-ddk-radio-items-final',component_property='value')
)  
def update_graph(col_chosen):
    fig=px.histogram(df,x='continent',y=col_chosen,histfunc='avg')
    return fig

#running the app
if __name__=='__main__':
    app.run_server(debug=True)

