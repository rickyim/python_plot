import numpy as np 
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(12, 9)
ax.tick_params(labelsize=24)
plot_len = 40
ax.plot(np.arange(plot_len)*0.8, 100*digital[:plot_len], label='Digital ({}%)'.format(100*np.max(digital)), linewidth=6)
plt.ylim(bottom=0, top=100)
#set y tick
plt.yticks(np.arange(11)*10)
#set axis color
color = 'tab:red'
ax_lr.tick_params(axis='y', labelcolor=color)
#set axis label
ax_lr.set_ylabel('learning rate', color=color)
#set x limit
plt.xlim(left=0)
plt.legend(fontsize=32)
#twin axis
ax_1 = ax.twinx()


ax.set_xlabel('Number of Epoch', fontsize=32)
ax.set_ylabel('Testing Accuracy (%)', fontsize=32)
plt.savefig('')
#tight layout
plt.tight_layout()
plt.show()
