# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
fertility=[1,2]
female_literacy=[3,2]

# Add a circle glyph to the figure p
p.circle(fertility,female_literacy,size=10,alpha=0.8, color='red')
p.x([4,5],[1,9],size=10,alpha=0.8, color='red')

# Call the output_file() function and specify the name of the file
output_file('output.html')

# Display the plot
show(p)
