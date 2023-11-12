import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import TwoSlopeNorm

# Data for creating the heatmap
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

# Find the min and max values for the color normalization
min_val = np.nanmin(data_array)
max_val = np.nanmax(data_array)

# Create a diverging colormap with a center at 0
cmap = sns.diverging_palette(220, 20, as_cmap=True)

# Create a TwoSlopeNorm instance with vmin at the min_val, vmax at max_val, and vcenter at 0
norm = TwoSlopeNorm(vmin=min_val, vcenter=0, vmax=max_val)

# Create the heatmap
plt.figure(figsize=(10, 8))
ax = sns.heatmap(data_array, cmap=cmap, annot=True, mask=np.isnan(data_array), square=True, norm=norm)

# Set the labels for the axes
axis_labels = ['NSSI', 'NC', 'CR', 'SA', 'PA', 'EN', 'EA']
# Set the labels for the axes
ax.set_xticklabels(axis_labels, rotation=0)
ax.set_yticklabels(axis_labels, rotation=0)
ax.xaxis.tick_top()  # Move the x-axis labels to the top
ax.xaxis.set_label_position('top')  # Set the x-axis labels to the top
plt.title("Correlation Heatmap with Diverging Colors", y=1.08)  # Adjust title position

# Adjust the plot to ensure everything fits without overlap
plt.tight_layout()

# Show the plot
plt.show()
