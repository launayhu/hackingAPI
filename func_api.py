from flask import Flask, render_template, request
import numpy as np
from joblib import dump, load
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


def make_picture(training_data_filename, model, new_input_arr, output_file='predictions_pic.svg'):
  # Plot training data with model
  data = pd.read_pickle(training_data_filename)
  x_new = np.array(list(range(19))).reshape(19, 1)
  preds  = model.predict(x_new)
  ages = data['Age']
  heights = data['Height']
  fig = px.scatter(x=ages, y=heights, title="Height vs Age", labels={'x': 'Age (Years)','y': 'Height (Inches)'})
  fig.add_trace(go.Scatter(x=x_new.reshape(x_new.shape[0]), y=preds, mode='lines', name='Model'))
  new_preds = model.predict(new_input_arr)
  fig.add_trace(go.Scatter(x=new_input_arr.reshape(new_input_arr.shape[0]), y=new_preds, name='New Outputs', mode='markers', marker=dict(
            color='purple',
            size=20,
            line=dict(color='purple', width=2))))
  fig.write_image(output_file, width=800, engine ='kaleido')
  # if you want interactive plot fig.show()
  # fig.show()
  return fig

def floats_string_to_input_arr(floats_str):
    floats = [float(x.strip()) for x in floats_str.split(',')]
    as_np_arr = np.array(floats).reshape(len(floats), 1)
    return as_np_arr
