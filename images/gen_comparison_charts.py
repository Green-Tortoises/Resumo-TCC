import matplotlib.pyplot as plt
import numpy as np

# Sample data
datasets = ["Haberman", "Optdigits", "Mushroom", "Body Performance"]
gpu_times = [0.004, 1.9948, 1.4557, 1.99423]  # Sample times for GPU in minutes
cpu_times = [0.0005, 6.031, 8.416, 24.04]  # Sample times for CPU in minutes

x = np.arange(len(datasets))  # the label locations
width = 0.4  # the width of the bars

# Bar Chart
fig, ax1 = plt.subplots()
rects1 = ax1.bar(x - width/2, gpu_times, width, label='GPU')
rects2 = ax1.bar(x + width/2, cpu_times, width, label='CPU')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax1.set_ylabel('Time (minutes)')
ax1.set_title('Comparison of Running Time on GPU vs CPU')
ax1.set_xticks(x)
ax1.set_xticklabels(datasets)
ax1.legend()

ax1.bar_label(rects1, padding=3)
ax1.bar_label(rects2, padding=3)

fig.tight_layout()

# Save the bar chart as PNG
bar_chart_path = 'GPU_vs_CPU_Bar_Chart.png'
fig.savefig(bar_chart_path)

# Line Chart for growth of execution time
fig2, ax2 = plt.subplots()
ax2.plot(datasets, gpu_times, label='GPU Time Growth', marker='o')
ax2.plot(datasets, cpu_times, label='CPU Time Growth', marker='o')

ax2.set_xlabel('Datasets')
ax2.set_ylabel('Time (minutes)')
ax2.set_title('Growth of Execution Time for GPU and CPU')
ax2.legend()

# Save the line chart as PNG
line_chart_path = 'Execution_Time_Growth_Line_Chart.png'
fig2.savefig(line_chart_path)

# Sample data
datasets = ["Optdigits", "Mushroom", "Body Performance"]
gpu_times = [1.9948, 1.4557, 1.99423]  # Sample times for GPU in minutes
cpu_times = [6.031, 8.416, 24.04]  # Sample times for CPU in minutes

# Calculating performance gain: (CPU Time - GPU Time) / CPU Time * 100
performance_gain = [(cpu - gpu) / cpu * 100 for gpu, cpu in zip(gpu_times, cpu_times)]

# Line Chart for Performance Gain
fig3, ax3 = plt.subplots()
ax3.plot(datasets, performance_gain, label='Performance Gain', marker='o', color='green')

ax3.set_xlabel('Datasets')
ax3.set_ylabel('Performance Gain (%)')
ax3.set_title('Performance Gain of GPU over CPU')
ax3.legend()

# Save the performance gain chart as PNG
performance_gain_chart_path = 'Performance_Gain_Line_Chart.png'
fig3.savefig(performance_gain_chart_path)

performance_gain_chart_path
