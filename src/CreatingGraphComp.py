import matplotlib
import matplotlib.pyplot as plt
import numpy as np



men_means, men_std = (0.001, 0.089, 10), (1, 1, 1)
women_means, women_std = (0.013, 0.058, 1.042), (1, 1, 1)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                label='Java - Ex2') # blue
rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
                label='Python - Ex3') # orange

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('time in seconds')
ax.set_title('Creating graphs comparison')
ax.set_xticks(ind)
ax.set_xticklabels(('100 nodes', '10^4 nodes', '10^6 nodes'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

fig.tight_layout()

plt.show()

if __name__ == '__main__':
    autolabel()