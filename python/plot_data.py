import matplotlib.pyplot as plt
import csv

voltage = []
current = []

# read data from text file
with open('data/sample.txt') as file:
	reader = csv.reader(file, delimiter='\t')
	# trow away first line with labels
	next(reader)
	for line in reader:
	    voltage.append(float(line[3]))
	    current.append(float(line[2]))

# set font similar to latex
plt.rc('font', family='serif')

# plot data
plt.plot(current, voltage, '.')

# add labels to plot
plt.xlabel('Current [A]')
plt.ylabel('Voltage [V]')
plt.title('Ebike battery data', fontsize='16')
plt.show()

