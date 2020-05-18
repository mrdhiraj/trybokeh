# Import CheckboxGroup, RadioGroup, Toggle from bokeh.models
from bokeh.models import CheckboxGroup, RadioGroup, Toggle
from bokeh.io import curdoc
from bokeh.plotting import figure

from bokeh.layouts import widgetbox

# Add a Toggle: toggle
toggle = Toggle(label='Toggle button', button_type='success')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
curdoc().add_root(widgetbox(toggle, checkbox, radio))