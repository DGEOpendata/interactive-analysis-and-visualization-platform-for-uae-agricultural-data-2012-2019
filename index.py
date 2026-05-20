python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def filter_data_by_region(data, region):
    """Filter the dataset by a specific region."""
    return data[data['Region'] == region]

def visualize_data(data, x_axis, y_axis, title):
    """Create a visualization for the data."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_axis, y=y_axis, data=data)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage
data = load_data('Agricultural_Farms_UAE_2012_2019.csv')
filtered_data = filter_data_by_region(data, 'Abu Dhabi')
visualize_data(filtered_data, 'Year', 'Number of Farms', 'Number of Farms in Abu Dhabi (2012-2019)')
