import numpy as np 
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(12, 9)
ax.tick_params(labelsize=24)
plot_len = 40
ax.plot(np.arange(plot_len)*0.8, 100*digital[:plot_len], label='Digital ({}%)'.format(100*np.max(digital)), linewidth=6)
plt.ylim(bottom=0, top=100)
plt.yticks(np.arange(11)*10)
plt.xlim(left=0)
plt.legend(fontsize=32)
ax.set_xlabel('Number of Epoch', fontsize=32)
ax.set_ylabel('Testing Accuracy (%)', fontsize=32)
plt.savefig('./training_cpr.png')
plt.show()
