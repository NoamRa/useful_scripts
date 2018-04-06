# -*- coding: utf-8 -*-
# python 2

# generate a plot using data collected by check_internet_connection.py


import plotly.graph_objs as go
from plotly import tools
from plotly.offline import plot
import json
import math
import pandas as pd


df = pd.read_csv('./conn_test.csv')

test_list = list(df)[2:] # header row without test-number and test-time

# trace each colum into raw data and log10
raw_data = []
for test in test_list:
    trace = go.Scatter( x = df['test time'], 
                        y=df[test],
                        name=test)
    raw_data.append(trace)

log_data = []
for test in test_list:
    trace = go.Scatter( x = df['test time'], 
                        y=df[test].map(lambda x: math.log10(x)), # use log10 scale
                        name=test + " log10")
    log_data.append(trace)

# stack plots in one page
fig = tools.make_subplots(rows=4, cols=1)

for trace_num in xrange(len(raw_data)-1):
    fig.append_trace(log_data[trace_num], 1, 1) # all log data together 
    fig.append_trace(raw_data[trace_num], trace_num+2, 1) # indevidual plot for each test


# plot to html
plot(fig)


# # plot and save png
# plot(fig, 
#     image = 'png', 
#     image_filename='conn_test',
#     output_type='file', 
#     image_width=1280, image_height=720
#       )

