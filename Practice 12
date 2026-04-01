import pandas as pd

# Creating the DataFrame from your provided data
data = {
    'carat': [0.23, 0.21, 0.23, 0.29, 0.31],
    'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'],
    'color': ['E', 'E', 'E', 'I', 'J'],
    'clarity': ['SI2', 'SI1', 'VS1', 'VS2', 'SI2'],
    'depth': [61.5, 59.8, 56.9, 62.4, 63.3],
    'table': [55.0, 61.0, 65.0, 58.0, 58.0],
    'price': [326, 326, 327, 334, 335],
    'x': [3.95, 3.89, 4.05, 4.20, 4.34],
    'y': [3.98, 3.84, 4.07, 4.23, 4.35],
    'z': [2.43, 2.31, 2.31, 2.63, 2.75]
}

df = pd.DataFrame(data)

# i) Calculate the mean of price for each cut
mean_price = df.groupby('cut')['price'].mean()
print("--- Mean Price per Cut ---")
print(mean_price)
print("\n")

# ii) Print count, minimum price, and maximum price for each cut
# We use the .agg() function to perform multiple calculations at once
cut_stats = df.groupby('cut')['price'].agg(['count', 'min', 'max'])
print("--- Price Statistics (Count, Min, Max) per Cut ---")
print(cut_stats)
print("\n")

# iii) Calculate and print average value of parameter x, y, and z separately
avg_x = df['x'].mean()
avg_y = df['y'].mean()
avg_z = df['z'].mean()

print("--- Average Dimensions ---")
print(f"Average of x: {avg_x:.2f}")
print(f"Average of y: {avg_y:.2f}")
print(f"Average of z: {avg_z:.2f}")
