import matplotlib.pyplot as plt

# line 1 points
x1 = [10, 20, 30, 40]
#y1 = [23.85, 57.95, 75.96, 112.83]
#y1 = [12.40, 22.90, 35.40, 42.34]
y1 = [45.89, 79.06, 116.16, 194.32]

# plotting the line 1 points
plt.plot(x1, y1, label="PRE-CHECK", marker='o')
#plt.ylim(15, 125)


# line 2 points
x2 = [10, 20, 30, 40]
#y2 = [38.84, 53.33, 101.33, 110.16]
#y2 = [7.72, 13.24, 17.50, 23.42]
y2 = [32.35, 59.93, 84.56, 94.81]
# plotting the line 2 points
plt.plot(x2, y2, label="ONGOING CHECK", marker='o')
#plt.ylim(15, 125)

# line 3 points
x3 = [10, 20, 30, 40]
#y3 = [42.83, 57.64, 87.24, 124.30]
#y3 = [8.28, 14.54, 18.47, 24.40]
#y3 = [10.53, 18.50, 27.84, 37.93]
y3 = [40.14, 71.56, 99.97, 138.01]
# plotting the line 2 points
plt.plot(x3, y3, label="POST-CHECK", marker='o')
#plt.ylim(11, 125)

# naming the x axis
plt.xlabel('Number of Activity Requests')
# naming the y axis
plt.ylabel('Execution Time (in milliseconds)')
plt.xlim(4, 45)
plt.ylim(20, 200)
# giving a title to my graph
#plt.title('Activity request processing graph!')
plt.grid(True)
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()