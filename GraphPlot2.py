import matplotlib.pyplot as plt

# line 1 points
x1 = [10, 20, 30, 40]
#y1 = [23.85, 57.95, 75.96, 112.83]
y1 = [38.84, 53.33, 101.33, 110.16]

# plotting the line 1 points
plt.plot(x1, y1, label="PRE-CHECK", marker='o')
#plt.ylim(15, 125)


# line 2 points
x2 = [10, 20, 30, 40]
#y2 = [38.84, 53.33, 101.33, 110.16]
y2 = [42.83, 57.64, 87.24, 124.30]
# plotting the line 2 points
plt.plot(x2, y2, label="ONGOING CHECK", marker='o')
#plt.ylim(15, 125)

# line 3 points
x3 = [10, 20, 30, 40]
#y3 = [42.83, 57.64, 87.24, 124.30]
y3 = [15.21, 22.09, 25.44, 60.76]
# plotting the line 2 points
plt.plot(x3, y3, label="POST-CHECK", marker='o')
#plt.ylim(11, 125)

# naming the x axis
plt.xlabel('Number of Activity Requests')
# naming the y axis
plt.ylabel('Execution Time (in milliseconds)')
plt.ylim(10, 130)
# giving a title to my graph
#plt.title('Activity request processing graph!')
plt.grid(True)
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()