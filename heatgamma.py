import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Sample data for the heatmap, the values should be replaced with the actual data
# data = np.array([
#     [1.00, 0.11, 0.34, 0.31, 0.30, 0.33],
#     [1.00, 0.23, 0.23, 0.22, 0.21],
#     [1.00, 0.90, 0.95, 0.88],
#     [1.00, 0.77, 0.73],
#     [1.00, 0.80],
#     [1.00]
# ])

# data = np.array([
#     [1.000, 0.465, 0.183, 0.297, 0.158, 0.391, 0.466],
#     [1.000, 0.378, 0.145, 0.213, 0.152, 0.360],
#     [1.000, 0.086, 0.189, 0.224, 0.318],
#     [1.000, 0.234, 0.176, 0.279],
#     [1.000, 0.358, 0.603],
#     [1.000, 0.497],
#     [1.000]
# ])

data = [
    [1.000, 0.465, 0.183, 0.297, 0.158, 0.391, 0.466],
    [1.000, 0.378, 0.145, 0.213, 0.152, 0.360],
    [1.000, 0.086, 0.189, 0.224, 0.318],
    [1.000, 0.234, 0.176, 0.279],
    [1.000, 0.358, 0.603],
    [1.000, 0.497],
    [1.000]
]
max_length = max(len(seq) for seq in data)

data_array = np.full((len(data), max_length), fill_value=np.nan)

for i, seq in enumerate(data):
    data_array[i, :len(seq)] = seq

# Since the heatmap is triangular, we need to create a mask to hide the upper triangle
mask = np.zeros_like(data_array, dtype=bool)
mask[np.triu_indices_from(mask, k=1)] = True

# We need to make sure the data is in a square matrix form
square_data = np.zeros((max(data_array.shape), max(data_array.shape)))
# Copy the data to the square matrix and leave the rest as zero (which will be masked)
for i, row in enumerate(data_array):
    square_data[i, :len(row)] = row

# Create the heatmap
sns.set(style="white")
plt.figure(figsize=(10, 8))
sns.heatmap(square_data, mask=mask, cmap='Oranges', annot=True, square=True, cbar_kws={"shrink": .5})
plt.xticks(ticks=np.arange(0.5, len(square_data)), labels=['NSSI', 'NC', 'CR', 'SA', 'PA', 'EN', 'EA'], rotation=45)
plt.yticks(ticks=np.arange(0.5, len(square_data)), labels=['NSSI', 'NC', 'CR', 'SA', 'PA', 'EN', 'EA'], rotation=0)
plt.title("Correlation Heatmap")
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlap

# Show the plot
plt.show()
