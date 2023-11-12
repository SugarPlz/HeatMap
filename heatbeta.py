import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Adjusting the data to be 2-dimensional with NaN fillings for the heatmap
data = [
    [1.000, 0.465, 0.183, 0.297, 0.158, -0.391, 0.466],
    [np.nan, 1.000, -0.378, 0.145, 0.213, 0.152, 0.360],
    [np.nan, np.nan, 1.000, -0.086, -0.189, -0.224, -0.318],
    [np.nan, np.nan, np.nan, 1.000, 0.234, 0.176, 0.279],
    [np.nan, np.nan, np.nan, np.nan, 1.000, 0.358, 0.603],
    [np.nan, np.nan, np.nan, np.nan, np.nan, 1.000, 0.497],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 1.00]
]

# Convert the list of lists into a numpy array
data_array = np.array(data)

# Create the heatmap
sns.set(style="white")
plt.figure(figsize=(10, 8))
sns.heatmap(data_array, cmap='Oranges', annot=True, mask=np.isnan(data_array), square=True, cbar_kws={"shrink": .5})

# Set the labels for the axes
axis_labels = ['NSSI', 'NC', 'CR', 'SA', 'PA', 'EN', 'EA']
plt.xticks(ticks=np.arange(0.5, len(data_array)), labels=axis_labels, rotation=45)
plt.yticks(ticks=np.arange(0.5, len(data_array)), labels=axis_labels, rotation=0)
plt.title("Correlation Heatmap")

# Adjust the plot to ensure everything fits without overlap
plt.tight_layout()

# Show the plot
plt.show()
