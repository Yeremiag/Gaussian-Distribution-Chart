import matplotlib.pyplot as plt
import random

target = 10
xAxis = [0] * target * 2
yAxis = [0] * target * 2
up = 0
bellow = 0

for i in range(target * 2):
    xAxis[i] = random.triangular(1, target * 2)
    yAxis[i] = i
    if xAxis[i] > yAxis[i]:
        up = up + 1
    elif xAxis[i] < yAxis[i]: bellow = bellow + 1


avg = sum(xAxis)/(target * 2)
if(avg > target):
    plt.text(0, 0, "Target: " + str(target) + "   Average: " + str(avg) + "   Error: " + str(((avg/target)-1)*100) + "%" + "   Up: " + str(up) + "   Bellow: " + str(bellow), bbox=dict(facecolor='red', alpha=0.5))
else:
    plt.text(0, 0, "Target: " + str(target) + "   Average: " + str(avg) + "   Error: " + str(100-((avg/target)*100)) + "%" + "   Up: " + str(up) + "   Bellow: " + str(bellow), bbox=dict(facecolor='red', alpha=0.5))

plt.xlabel("Guess")
plt.ylabel("Person")
                    #random
plt.plot(yAxis,'-g', xAxis, 'ro')
plt.show()
