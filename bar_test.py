"""
Simple demo of a horizontal bar chart.
"""
# import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def addPercentSymbol(listConvert):
    """
    takes a list of the percentages and returns a list of the rounded #s with
    the percent symbol
    """

    list_percent = listConvert
    list_percentages = []
    for element in list_percent:
        list_percentages.append(str(int(element))+'%')

    return list_percentages

#### Data
courseTitle = ['Tom', 'Dick', 'Harry', 'Slim', 'Jimothy the III of London']
y_position = np.arange(len(courseTitle))
print y_position
y_pos = y_position[::-1]
print y_pos
performance = 3 + 10 * np.random.rand(len(courseTitle))
performanceLabel = addPercentSymbol(performance)

#### Sets up the figure
fig, ax1 = plt.subplots(figsize=(20,15), facecolor='white')
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['top'].set_visible(False)
# Pushes the left border/labels out
ax1.spines['left'].set_position(('outward', .4))
# Set the color scheme
colors=['#D0DD2B','#98C73D', '#00A9E0', '#67CDDC', '#3B3B3D']

#### Plots the horizontal bars
rects = plt.barh(y_pos, performance, align='center', color=colors, edgecolor='none')

#### Adds the appropriate labeling of data points
plt.xticks([])
plt.yticks(y_pos,performanceLabel, color='#3B3B3D', size='x-large')
plt.tick_params(right="off")
plt.tick_params(left="off")

# Write in the courseTitle inside each bar
for i,rect in enumerate(rects):
    barWidth = rect.get_width()
    barHeight = rect.get_height()
    print 'height', barHeight
    # print 'width', barWidth
    # print courseTitle[i], len(courseTitle[i])

    # If bars aren't wide enough to print the title inside
    if barWidth < (len(courseTitle[i]) + 0.1*barWidth):
        # Shift the text to the right side of the right edge
        xloc = barWidth + .3
        clr = '#3B3B3D'
        align = 'left'
    else:
        # Shift the text to the left side of the right edge
        xloc = barWidth-.3
        clr = 'white'
        align = 'right'

    # Center the text vertically in the bar
    yloc = rect.get_y()+rect.get_height()/2.0
    ax1.text(xloc, yloc, courseTitle[i], horizontalalignment=align,
             verticalalignment='center', color=clr, size='x-large')

#### Saves the plot to a file name
# plt.savefig("plot.png",bbox_inches='tight', transparent=True, edgecolor='none')

plt.show()