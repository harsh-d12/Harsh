import pandas as pd
import matplotlib.pyplot as plt

# --- Step 0: Create/Load Dataset ---
data = {
    'month_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    'bathingsoap': [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    'shampoo': [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    'moisturizer': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'total_profit': [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200]
}
df = pd.DataFrame(data)

# a) Total profit of all months using a Line Plot
plt.figure(figsize=(8, 4))
plt.plot(df['month_number'], df['total_profit'], marker='o', color='b', linestyle='--')
plt.title('Company Profit Per Month')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.xticks(df['month_number'])
plt.show()

# b) All product sales data using a Multiline Plot
plt.figure(figsize=(10, 6))
for column in df.columns[1:-1]: # Skipping month_number and total_profit
    plt.plot(df['month_number'], df[column], marker='o', label=f'{column} Sales')

plt.title('All Product Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales units')
plt.legend(loc='upper left')
plt.xticks(df['month_number'])
plt.show()

# c) Face cream and face wash sales data using Bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['month_number'] - 0.2, df['facecream'], width=0.4, label='Face Cream', align='center')
plt.bar(df['month_number'] + 0.2, df['facewash'], width=0.4, label='Face Wash', align='center')
plt.title('Facewash and Facecream Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales units')
plt.xticks(df['month_number'])
plt.legend()
plt.show()

# d) Total sale data for last year for each product using a Pie chart
labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'BathingSoap', 'Shampoo', 'Moisturizer']
sales_totals = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), 
                df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]

plt.figure(figsize=(7, 7))
plt.pie(sales_totals, labels=labels, autopct='%1.1f%%')
plt.title('Total Sales Contribution by Product')
plt.show()
