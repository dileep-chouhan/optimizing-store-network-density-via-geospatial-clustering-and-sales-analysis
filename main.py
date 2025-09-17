import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point
# --- 1. Synthetic Data Generation ---
# Generate synthetic data for store locations, sales, and coordinates
np.random.seed(42)  # for reproducibility
num_stores = 50
data = {
    'StoreID': range(1, num_stores + 1),
    'Sales': np.random.randint(1000, 10000, size=num_stores),
    'Longitude': np.random.uniform(-122.5, -122, size=num_stores),
    'Latitude': np.random.uniform(37.7, 37.8, size=num_stores)
}
df = pd.DataFrame(data)
# Create geometry column for geospatial analysis
df['geometry'] = df.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
# --- 2. Geospatial Clustering and Sales Analysis ---
# (Simplified clustering for demonstration - replace with KMeans or DBSCAN for robust analysis)
#  This example uses a simple quartile-based approach for demonstration purposes.
sales_quartiles = pd.qcut(df['Sales'], 4, labels=['Low', 'Medium', 'High', 'Very High'])
df['SalesQuartile'] = sales_quartiles
# --- 3. Visualization ---
# Create a scatter plot of store locations colored by sales quartile
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Longitude', y='Latitude', hue='SalesQuartile', size='Sales', sizes=(20, 200))
plt.title('Store Locations and Sales Performance')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Sales Quartile')
# Save the plot to a file
output_filename = 'store_locations.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# --- 4.  Further Analysis (Illustrative example)---
#  Calculate average sales per quartile
average_sales_by_quartile = df.groupby('SalesQuartile')['Sales'].mean()
print("\nAverage Sales per Quartile:")
print(average_sales_by_quartile)
# Identify potential areas for new stores (simplified example -  requires more sophisticated analysis in a real-world scenario)
#  This example simply highlights the lowest sales quartile for illustrative purposes.  A real-world approach would involve more sophisticated spatial analysis.
low_sales_stores = df[df['SalesQuartile'] == 'Low']
print("\nStores in the lowest sales quartile:")
print(low_sales_stores[['StoreID', 'Sales', 'Longitude', 'Latitude']])
# Note:  This is a simplified example. A real-world application would involve more sophisticated clustering algorithms (like KMeans or DBSCAN), 
# more robust spatial analysis techniques (e.g., spatial autocorrelation analysis, market potential modeling), and potentially incorporating external data 
# (e.g., demographics, competition).  Error handling and more detailed data validation would also be crucial in a production environment.