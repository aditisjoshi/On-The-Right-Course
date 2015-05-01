"""
Simple demo of a horizontal bar chart.
"""
# import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt


#### Data
courseTitle = ['Tom', 'Dick', 'Harry', 'Slim', 'Jimothy the III of London']
y_pos = np.arange(len(courseTitle))
performance = 3 + 10 * np.random.rand(len(courseTitle))

#### Sets up the figure
fig, ax1 = plt.subplots(figsize=(5,5), facecolor='white')
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['top'].set_visible(False)
# Pushes the left border/labels out
ax1.spines['left'].set_position(('outward', 5))
# Set the color scheme
colors=['#D0DD2B','#98C73D', '#00A9E0', '#67CDDC', '#3B3B3D']

#### Plots the horizontal bars
rects = plt.barh(y_pos, performance, align='center', color=colors, edgecolor='none')

#### Adds the appropriate labeling of data points
plt.xticks([])
plt.yticks(y_pos,performance, color='#3B3B3D')
plt.tick_params(right="off")
plt.tick_params(left="off")

# Write in the courseTitle inside each bar
for i,rect in enumerate(rects):
    barWidth = rect.get_width()
    # print 'width', barWidth
    # print courseTitle[i], len(courseTitle[i])

    # If bars aren't wide enough to print the title inside
    if barWidth < (len(courseTitle[i]) + 0.2*barWidth):
        # Shift the text to the right side of the right edge
        xloc = barWidth + .25
        clr = '#3B3B3D'
        align = 'left'
    else:
        # Shift the text to the left side of the right edge
        xloc = barWidth-.25
        clr = 'white'
        align = 'right'

    # Center the text vertically in the bar
    yloc = rect.get_y()+rect.get_height()/2.0
    ax1.text(xloc, yloc, courseTitle[i], horizontalalignment=align,
             verticalalignment='center', color=clr)

#### Saves the plot to a file name
# plt.savefig("plot.png",bbox_inches='tight', transparent=True, edgecolor='none')

plt.show()