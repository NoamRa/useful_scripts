# -*- coding: utf-8 -*-
# python 2

# generate a plot using data collected by check_internet_connection.py


import numpy as np
import pandas as pd
import plotly.figure_factory as FF
import plotly.graph_objs as go
# import plotly.plotly as py
import json
import plotly.offline as offline
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

df = pd.read_csv('./conn_test.csv')
df_tabe = FF.create_table(df)
# print(json.dumps(df_tabe, indent=2))

# generate html table
# fig = plot(df_tabe)


trace = go.Scatter(x = df['test time'], y = df['8.8.8.8'],
                  name='connection test')
layout = go.Layout(title='connection test',
                   plot_bgcolor='rgb(230, 230,230)', 
                   showlegend=True)

fig = go.Figure(data=[trace], layout=layout)

# plot in html
offline.plot(fig)

# plot and save png
# offline.plot(fig, 
#             image = 'png', 
#             image_filename='conn_test',
#             output_type='file', 
#             image_width=800, image_height=600)

