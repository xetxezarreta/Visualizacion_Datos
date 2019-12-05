import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


app = dash.Dash(__name__)


app.layout = html.Div(children=[

html.Div(
    [html.H2(children='Práctica de visualización de datos con Dash - Plot.ly'),
        html.Img(
                            src=app.get_asset_url("logo.png"),
                            id="logo2",
                            style={
                                "height": "120px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )],
        className="box a"),




    html.Div(
            [
               
                html.Div(
                    [
                       html.Div([
                        html.Div(id='graph1', children='example-graph-1'),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])
                    ],
                    className="box b",
                    id="title",
                ),
                html.Div(
                    [
                         html.Div(id='graph2', children='example-graph-1'),

                         dcc.Graph(
                                id='example-graph',
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                                    ],
                                    'layout': {
                                        'title': 'Dash Data Visualization'
                                    }
                                },
                                className="box c"
                            )
                    ],
                    className="box c",
                    id="button",
                ),
            ],
            id="wrapper2",
            className="wrapper2",
            
        ),







   

])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(dict(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'GDP Per Capita',
                   'range':[2.3, 4.8]},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }



if __name__ == '__main__':
    app.run_server(debug=True)
 
