import time
import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd

__path = '../../plotly/' #make sure this exists. you can change this

def draw_graph_df(df_data):
    """
    :param df_data:
    :return: Plotly graph on browser
    df has to be numeric.
    x axis is the index
    """
    dict_data = {
        'x': df_data.index,
        'y': {
        },
    }

    for _col in df_data.columns:
        dict_data['y'][_col] = df_data[_col]
    draw_graph(dict_data)


def draw_graph(dict_data):
    """
    :param dict_data:
    dict_data = {
        'x': random_x,
        'y' : {
           'v1': random_y0,
           'v2': random_y1,
           'v3': random_y2,
        } ,
    }
    :return: Shows the graph on the browser
    """

    data = []
    for _key in dict_data['y'].keys():
        _trace = go.Scatter(
            x = dict_data['x'],
            y = dict_data['y'][_key],
            mode ='lines+markers',
            name = _key
        )
        data.append(_trace)

    file_name = __path + str(time.time()) + ".html"
    plotly.offline.plot(data, filename=file_name)

def draw_graph_two_df(df1,df2,str_title = None,str_df1_title = None,
                      str_df2_title=None, vertical=None):

    if vertical is None:
        vertical = True

    if vertical:
        [_rows, _cols] = [2, 1]
    else:
        [_rows, _cols] = [1, 2]

    fig = plotly.tools.make_subplots(rows=_rows, cols=_cols, subplot_titles=(
    str_df1_title, str_df2_title))

    for _col in df1.columns:
        _trace = go.Scatter(
            y=list(df1[_col]),
            x=list(df1.index),
            mode='lines+markers',
            name=_col
        )
        fig.append_trace(_trace, 1, 1)

    for _col in df2.columns:
        _trace = go.Scatter(
            y=list(df2[_col]),
            # x = list(df2.index),
            mode='lines+markers',
            name=_col,
            yaxis='y2'
        )
        fig.append_trace(_trace, _rows, _cols)

    fig['layout'].update(title=str_title)

    file_name = '../../plotly/' + str(time.time()) + ".html"
    plotly.offline.plot(fig, filename=file_name)

def draw_graph_two_df_overlay(df1,df2,str_title = None,str_df1_title = None,
                      str_df2_title=None):
    data = []
    for _col in df1.columns:
        _trace = go.Scatter(
            y=list(df1[_col]),
            x=list(df1.index),
            mode='lines+markers',
            name=_col
        )
        data.append(_trace)

    for _col in df2.columns:
        _trace = go.Scatter(
            y=list(df2[_col]),
            # x = list(df2.index),
            mode='lines+markers',
            name=_col,
            yaxis='y2'
        )
        data.append(_trace)

    layout = go.Layout(
        title=str_title,
        yaxis=dict(
            title=str_df1_title
        ),
        yaxis2=dict(
            title=str_df2_title,
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y',
            side='right'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    file_name = __path + str(time.time()) + ".html"
    plotly.offline.plot(fig, filename=file_name)

if __name__== "__main__":
    import numpy as np
    import pandas as pd

    if True:
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        for i in range(20):
            x = np.random.random(5)
            x2 = 2 * np.random.random(5)
            _df = pd.DataFrame([x])
            _df2 = pd.DataFrame([x2])
            df1 = df1.append(_df)
            df2 = df2.append(_df2)
        df1.reset_index(drop=True, inplace=True)
        df2.reset_index(drop=True, inplace=True)
        draw_graph_two_df_overlay(df1,df2)
        draw_graph_two_df(df1, df2, vertical=True)

    if False:

        N = 100
        random_x = np.linspace(0, 1, N)
        random_y0 = np.random.randn(N)+5
        random_y1 = np.random.randn(N)
        random_y2 = np.random.randn(N)-5

        # Create traces


        dict_data = {
            'x': random_x,
            'y' : {
               'v1': random_y0,
               'v2': random_y1,
               'v3': random_y2,
            } ,
        }


        draw_graph(dict_data)


        df = pd.DataFrame()
        for i in range(20):
            x = np.random.random(5)
            _df = pd.DataFrame([x])
            df = df.append(_df)
        df.reset_index(drop=True,inplace=True)
        print(df)

        draw_graph_df(df)

