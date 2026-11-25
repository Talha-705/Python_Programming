# import pandas as pd
# import matplotlib as plt
# df =pd.DataFrame({
#     'Category': ['A', 'B', 'C', 'D'],
#     'Sales': [250, 400, 150, 300],
#     'Profit': [60, 90, 30, 70],
#     'Units_Sold': [30, 50, 20, 40]
# })
# Csv6=df.to_csv("file.csv")
# df2=pd.read_csv("D:\\pandas\\file.csv")
# # print(df2)
# # print(df2.plot())
#
# print(df2.plot.area(alpha=0.4))


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Sales': [250, 400, 150, 300],
    'Profit': [60, 90, 30, 70],
    'Units_Sold': [30, 50, 20, 40]
}

df = pd.DataFrame(data)

# Set style for better visuals
sns.set(style="whitegrid")

# 1. Bar Plot
plt.figure(figsize=(6,4))
sns.barplot(x='Category', y='Sales', data=df)
plt.title("Bar Plot - Sales by Category")
plt.show()

# 2. Line Plot
plt.figure(figsize=(6,4))
plt.plot(df['Category'], df['Profit'], marker='o', color='green')
plt.title("Line Plot - Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

# 3. Histogram (for Units Sold)
plt.figure(figsize=(6,4))
plt.hist(df['Units_Sold'], bins=5, color='orange', edgecolor='black')
plt.title("Histogram - Units Sold")
plt.xlabel("Units")
plt.ylabel("Frequency")
plt.show()

# 4. Box Plot (Profit)
plt.figure(figsize=(6,4))
sns.boxplot(data=df[['Sales', 'Profit', 'Units_Sold']])
plt.title("Box Plot - Sales, Profit, Units Sold")
plt.show()

# 5. Scatter Plot (Sales vs Profit)
plt.figure(figsize=(6,4))
sns.scatterplot(x='Sales', y='Profit', data=df, hue='Category', s=100)
plt.title("Scatter Plot - Sales vs Profit")
plt.show()

# 6. Pie Chart (Category wise sales percentage)
plt.figure(figsize=(6,6))
plt.pie(df['Sales'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart - Sales Distribution")
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.show()
