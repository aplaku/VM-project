import numpy
import matplotlib.pyplot as plt
import ast

#Grab data from file
f = open("MemoryOps_NB.txt", "r")
d = []
#Evaluate lines in file to get a list of dicts
for lines in f:
    d.append(ast.literal_eval(str(lines)))

#Setup dict of lists
dict_list = {0:[], 1:[], 5:[], 6:[], 32767:[]}

#Parse list to separate into a dict
for items in d:
    for keys in items.keys():
        dict_list[keys].append(items[keys])

#close file
f.close()

#Plot data using Numpy
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(len(dict_list[0])),dict_list[0],'r', range(len(dict_list[1])),dict_list[1],'g', range(len(dict_list[5])),dict_list[5],'b', range(len(dict_list[6])),dict_list[6],'k',linewidth=2.0)

#Setup axes and legend
leg = ax.legend(('Dom0', 'Dom1-Dbench', 'Dom2-gcc', 'Dom3-gcc'), 'upper left')
ax.set_ylabel('cycles used')
ax.set_xlabel('Timestep')
ax.set_title('Memory Operations -- No Boosting')
plt.show()
