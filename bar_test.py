"""
Simple demo of a horizontal bar chart.
"""
# import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt


#### Data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))

#### Sets up the figure
fig, ax1 = plt.subplots(figsize=(10, 10), facecolor='white')
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['top'].set_visible(False)
# Pushes the left border/labels out
ax1.spines['left'].set_position(('outward', 5))
# Set the color scheme
colors=['#B2AE6D','#10BFFF', '#FFF10B', '#CC0935', '#B24E65']

#### Plots the horizontal bars
# rects = ax1.barh(pos, rankings, align='center', height=0.5, color='m')
rects = plt.barh(y_pos, performance, align='center', color=colors, edgecolor='none')

#### Adds the appropriate labeling of data points
plt.xticks([])
plt.yticks(y_pos,people)
plt.tick_params(right="off")
plt.tick_params(left="off")

#### Makes the axes labels
# plt.xlabel('Performance')
# plt.title('How fast do you want to go today?')



"""
For putting labels within the bars
http://matplotlib.org/examples/pylab_examples/barchart_demo2.html
"""

# Lastly, write in the ranking inside each bar to aid in interpretation
for rect in rects:
    """
    Rectangle widths are already integer-valued but are floating
    type, so it helps to remove the trailing decimal point and 0 by
    converting width to int type
    """
    width = int(rect.get_width())

    for name in people:
        nameLabel = name

    # rankStr = str(width)
    if (width < 2):        # The bars aren't wide enough to print the ranking inside
        xloc = width + 1   # Shift the text to the right side of the right edge
        clr = 'black'      # Black against white background
        align = 'left'
    else:
        xloc = 0.98*width  # Shift the text to the left side of the right edge
        clr = 'white'
        align = 'right'

    # Center the text vertically in the bar
    yloc = rect.get_y()+rect.get_height()/2.0
    ax1.text(xloc, yloc, nameLabel, horizontalalignment=align,
             verticalalignment='center', color=clr, weight='bold')


#### Saves the plot to a file name
# plt.savefig("plot.png",bbox_inches='tight', transparent=True, edgecolor='none')

plt.show()