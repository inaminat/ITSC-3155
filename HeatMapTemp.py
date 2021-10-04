import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')



# Preparing data
data = [go.Heatmap(x=df['month'], y=df['day'], z=df["record_max_temp"].values.tolist(),
                   colorscale="Jet")]

# Preparing layout
layout = go.Layout(title='Recorded max temperature', xaxis_title="Month",
                   yaxis_title="Days")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')
