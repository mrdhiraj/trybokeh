# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox
from bokeh.models import Slider
import numpy as np
from bokeh.layouts import column
from bokeh.plotting import ColumnDataSource

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)
slider.on_change('value', callback)
plot = figure()
x=1
source = ColumnDataSource()
# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)