import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Set the font size for various elements
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['axes.titlesize'] = 18
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['legend.fontsize'] = 16
# mpl.rcParams['title.fontsize'] = 18

# Data for our paper
acc1 = [0.9964548494983277, 0.9606020066889632, 0.939933110367893, 0.9389297658862876, 0.9332441471571906, 0.9037458193979934, 0.8147157190635451, 0.8110367892976589, 0.8018060200668896, 0.7763879598662208, 0.7476923076923077, 0.7138461538461538, 0.6842809364548496, 0.6709030100334448, 0.6577257525083612, 0.5874247491638795, 0.5807357859531772, 0.5721070234113712]
pre1 = [0.9948263854342851, 0.9444601870218192, 0.9224057917208094, 0.9212014461852229, 0.9140754369825207, 0.8790401133445497, 0.7889226342710998, 0.7855153203342619, 0.7798902235303476, 0.766813627254509, 0.7480484307790346, 0.730020903682264, 0.7119120244019906, 0.7053354890864996, 0.6983185768824628, 0.6690488794776778, 0.6644052863436123, 0.6574049803407601]
rec1 = [0.9999, 0.9999, 0.9938, 0.9937, 0.9936, 0.9927, 0.9871, 0.987, 0.9804, 0.9566, 0.9391, 0.908, 0.8869, 0.8725, 0.8597, 0.7583, 0.7541, 0.7524]
f11 = [0.9973567403122039, 0.9973567403122039, 0.9713897119541459, 0.9567728891884085, 0.9560783181796315, 0.9521801629132727, 0.9324191048701451, 0.876954513148543, 0.8748061156658542, 0.8687253555447256, 0.8512569521690767, 0.8327569389021903, 0.8093412960156877, 0.7898299047110161, 0.7800625838176128, 0.7706512482631886, 0.7108840348739102, 0.7064168618266979]
x1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Data for paper: Performance evaluation of.. Marcos et al (2021)
# algorithm chosen: Random forest (Sliding window + BoSC)
pre2 = [0.977, 0.988, 0.993, 0.996, 0.998, 0.999]
rec2 = [0.921, 0.967, 0.985, 0.991, 0.995, 0.997]
f12 =  [0.948, 0.977, 0.989, 0.993, 0.996, 0.998]
x2 = [5, 10, 15, 20, 25, 30]

# Data for paper: Taking a peek... Gabriel et al (2021)
acc3 = [.914, .950, .959, .962, .964, .966, .968]
pre3 = [.991, .991, .992, .993, .992, .992, .992]
rec3 = [.681, .819, .852, .861, .870, .878, .885]
f13 =  [.807, .897, .917, .922, .927, .931, .935]
x3 = [3, 5, 7, 9, 11, 13, 15]

##########################
# Create the precision plot
plt.figure()
new_x = np.linspace(2, 30, 50)
interpolated_y1 = np.interp(new_x, x1, pre1)
interpolated_y2 = np.interp(new_x, x2, pre2)
interpolated_y3 = np.interp(new_x, x3, pre3)
plt.plot(new_x, interpolated_y1, label='Our Work')
plt.plot(new_x, interpolated_y2, label='Marcos et al.')
plt.plot(new_x, interpolated_y3, label='Gabriel et al.')

# Set the range for the x-axis and y-axis
plt.xlim(2, 15)  # x-axis range from 0 to 6
plt.ylim(0.5, 1) # y-axis range from 0 to 12

# Add labels and title
plt.xlabel('Bag size')
plt.ylabel('Precision')
plt.title('Precision vs. Bag Size')

# Add a legend
plt.legend(loc='lower left')

# Adjust the layout to accommodate the increased fontsize
plt.tight_layout()
# Save the plot as an image file (e.g., PNG)
plt.savefig('precision.png', dpi=300)

##########################
# Create the accuracy plot
plt.figure()
interpolated_y = np.interp(x1, x3, acc3)
plt.plot(x1, acc1, label='Our Work')
plt.plot(x1, interpolated_y, label='Gabriel et al.')

# Set the range for the x-axis and y-axis
plt.xlim(2, 15)  # x-axis range from 0 to 6
plt.ylim(0.5, 1) # y-axis range from 0 to 12

# Add labels and title
plt.xlabel('Bag size')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Bag Size')

# Add a legend
plt.legend(loc='lower left')
# Adjust the layout to accommodate the increased fontsize
plt.tight_layout()
# Save the plot as an image file (e.g., PNG)
plt.savefig('accuracy.png', dpi=300)

##########################
# Create the recall plot
plt.figure()
new_x = np.linspace(2, 30, 50)
interpolated_y1 = np.interp(new_x, x1, rec1)
interpolated_y2 = np.interp(new_x, x2, rec2)
interpolated_y3 = np.interp(new_x, x3, rec3)
plt.plot(new_x, interpolated_y1, label='Our Work')
plt.plot(new_x, interpolated_y2, label='Marcos et al.')
plt.plot(new_x, interpolated_y3, label='Gabriel et al.')

# Set the range for the x-axis and y-axis
plt.xlim(2, 15)  # x-axis range from 0 to 6
plt.ylim(0.5, 1) # y-axis range from 0 to 12

# Add labels and title
plt.xlabel('Bag size')
plt.ylabel('Recall')
plt.title('Recall vs. Bag Size')

# Add a legend
plt.legend(loc='lower left')
# Adjust the layout to accommodate the increased fontsize
plt.tight_layout()
# Save the plot as an image file (e.g., PNG)
plt.savefig('recall.png', dpi=300)

##########################
# Create the f1 plot
plt.figure()
new_x = np.linspace(2, 30, 50)
interpolated_y1 = np.interp(new_x, x1, f11)
interpolated_y2 = np.interp(new_x, x2, f12)
interpolated_y3 = np.interp(new_x, x3, f13)
plt.plot(new_x, interpolated_y1, label='Our Work')
plt.plot(new_x, interpolated_y2, label='Marcos et al.')
plt.plot(new_x, interpolated_y3, label='Gabriel et al.')

# Set the range for the x-axis and y-axis
plt.xlim(2, 15)  # x-axis range from 0 to 6
plt.ylim(0.5, 1) # y-axis range from 0 to 12

# Add labels and title
plt.xlabel('Bag size')
plt.ylabel('F1-Score')
plt.title('F1-Score vs. Bag Size')

# Add a legend
plt.legend(loc='lower left')
# Adjust the layout to accommodate the increased fontsize
plt.tight_layout()
# Save the plot as an image file (e.g., PNG)
plt.savefig('f1.png', dpi=300)