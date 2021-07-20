''''from matplotlib import pyplot as plt
import numpy as np

#Creating dataset
marks = np.array([70, 50, 40, 90, 55, 85, 74, 66, 33, 11, 45, 36, 89])

# Creating histogram
fig, ax = plt.subplots(1, 1)
ax.hist(marks)

# Set title
ax.set_title("Title")

# adding labels
ax.set_xlabel('x-label')
ax.set_ylabel('y-label')

# Make some labels.
rects = ax.patches
labels = ["label%d" % i for i in range(len(rects))]

for rect, label in zip(rects, labels):
	height = rect.get_height()
	ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
			ha='center', va='bottom')

#Show plot
#plt.show()
plt.savefig("histogram.png")'''


import matplotlib.pyplot as plt
import numpy as np

price = np.asarray([2.50, 1.23, 4.02, 3.25, 5.00, 4.40])
sales_per_day = np.asarray([34, 62, 49, 22, 13, 19])
profit_margin = np.asarray([20, 35, 40, 20, 27.5, 15])

plt.scatter(x=price, y=sales_per_day, s=profit_margin * 10)
#plt.show()
plt.savefig("Plot1.png")