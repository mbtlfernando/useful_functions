import time
import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd

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

    file_name = '../../plotly/' + str(time.time()) + ".html"
    plotly.offline.plot(data, filename=file_name)


if __name__== "__main__":


    import numpy as np

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

    import numpy as np
    import pandas as pd

    df = pd.DataFrame()
    for i in range(20):
        x = np.random.random(5)
        _df = pd.DataFrame([x])
        df = df.append(_df)
    df.reset_index(drop=True,inplace=True)
    print(df)

    draw_graph_df(df)

# trace0 = go.Scatter(
#     x = random_x,
#     y = random_y0,
#     mode = 'lines',
#     name = 'lines'
# )
# trace1 = go.Scatter(
#     x = random_x,
#     y = random_y1,
#     mode = 'lines+markers',
#     name = 'lines+markers'
# )
# trace2 = go.Scatter(
#     x = random_x,
#     y = random_y2,
#     mode = 'markers',
#     name = 'markers'
# )
# data = [trace0, trace1, trace2]
#
# file_name = '../../../plotly/' + str(time.time()) + ".html"
# plotly.offline.plot(data, filename=file_name)