
# -*- coding: utf-8 -*-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import datetime
import random
import decimal
import numpy as np
import time
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import descriptions





url = 'https://raw.githubusercontent.com/chefdarek/hotel-app/master/hotel_metric.csv'
df = pd.read_csv(url,index_col=0, parse_dates=True)

app = dash.Dash(__name__)
app.title = 'Darek Tidwell'
server = app.server
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list
labels_for_drop = df.columns.to_list()
labels_for_drop.sort(reverse=True)

app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('Salutations'),
                                 html.P('• KRI Interaction Analysis'),
                                 html.P('• Combine KRI\'s to compare metrics'),
                                 html.P('• Click + hold to zoom graph, Double Click to reset'),
                                 html.Div(
                                     className='div-for-dropdown',
                                     children=[
                                         dcc.Dropdown(id='stockselector', options=get_options(labels_for_drop),
                                                      multi=True, value=[labels_for_drop.sort()],
                                                      style={'backgroundColor': '#1E1E1E'},
                                                      className='stockselector')]),
                                html.H2('Darek Tidwell'),
                                
                                html.A( html.P('• INSPIRATION'), 
                                href='https://youtu.be/8IQ7lgCneyA?t=830'),
                                html.A(html.P('• ABOUT ME'),
                                href='https://chefdarek.github.io/aboutme/'),
                                html.A(html.P(' • RESUME'), 
                                href='https://drive.google.com/file/d/11N5X-cCkJO1HTeP0R7VZn7kdSNhNKidn/view?usp=sharing'),
                                html.Div(html.Img(src=app.get_asset_url('table.png'),style={'padding-left':'10%','height':'65%', 'width':'80%'}))]),
                    html.Div(id='graph',className='eight columns div-for-charts bg-grey',                                   
                             children=[
                                 dcc.Graph(id='timeseries', config={'displayModeBar': False},animate=True),
                                 dcc.Loading(
                                    id="loading-2",
                                    children=[html.Div([html.Div(id="loading-output-2")])],
                                    type="default"),
                                 html.H2(id='header-description'),
                                 html.P(id="description-p"),
                                 html.Img(src=app.get_asset_url('livit.png'), style={'height':'30%','width':'100%', 'padding-top':'10px'})]),
                    ])])
# 
# 



# Callback for timeseries price
@app.callback(Output("loading-2", "children"), Input("loading-2", "value"))
def input_triggers_nested(value):
    return value
@app.callback(Output('timeseries', 'figure'),
              [Input('stockselector', 'value')])
def update_graph(selected_dropdown_value):
    trace1 = []
    df_sub = df

    
    for stock in selected_dropdown_value:
        sine_wave = (np.sin(df_sub[stock])*-100)+ df_sub[stock].median()
        trace1.append(go.Scatter(x=df_sub.index,
                                 y=df_sub[stock],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))
        
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#fcba03", '#fc5e03', '#03f0fc', '#6c70ba', '#b210c7', '#d9327a'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(233,230,221,20)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  xaxis={'range': [ df_sub[stock].index.min() if df_sub[stock].index.min() == True else df_sub.index.min(),
                                    df_sub[stock].index.min() if df_sub[stock].index.min() == True else df_sub.index.max()]},
              ),

              }
              
    return figure
#callback for description
@app.callback(
    dash.dependencies.Output('header-description', 'children'),
    [dash.dependencies.Input('stockselector', 'value')])
def update_output(selected_dropdown_value):
    titles_desc = []
    for x in selected_dropdown_value:
        titles_desc.append("•")
        titles_desc.append(x)
        
    return titles_desc
@app.callback(
    dash.dependencies.Output('description-p', 'children'),
    [dash.dependencies.Input('stockselector', 'value')])

def update_p(selected_dropdown_value):
    paragraph_query = []
    for x in selected_dropdown_value:
        paragraph_query.append(x)
    descriptor = descriptions.test_print(paragraph_query[-1])
    return paragraph_query[-1] + descriptor
if __name__ == '__main__':
    #app.run_server(debug=False, port=8080)
    app.run_server(debug=True, port=8080)
    
