import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('../01_seaborn/task1/datasets/dataset-airport-3.csv')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.datetime, 'y': df['horas vuelo'], 'type': 'line', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Airport 1'
            }
        }
    ),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    
    dcc.Graph(
        id='example-graph2',
        figure={
            'data': [
                {'x': df.datetime, 'y': df['horas vuelo'], 'type': 'line', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Airport 2'
            }
        }
    )        
])

if __name__ == '__main__':
    app.run_server(debug=True) 
