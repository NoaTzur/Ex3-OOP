import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['100 nodes', '10^4 nodes', '10^6 nodes']
java_means = [0.001, 0.089, 1.856]
python_means = [0.013, 0.058, 10.172]
network_means = [0.000, 0.011, 1.315]

x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, java_means, width, label='Java')
rects2 = ax.bar(x + width/2, python_means, width, label='Python')
rects3 = ax.bar(x + width+0.1, network_means, width, label='networkX')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('time in seconds')
ax.set_title('Comparing graph creation')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)


fig.tight_layout()

plt.show()