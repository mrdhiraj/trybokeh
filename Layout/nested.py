# Import column and row from bokeh.layouts
from bokeh.layouts import column, row

# Make a row layout that will be used as the second row: row2
row2 = row([mpg_hp, mpg_weight], sizing_mode='scale_width')

# Make a column layout that includes the above row layout: layout
layout = column([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)