import matplotlib.pyplot as plt

# Sample Data
companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS', 'Amdocs']
recruits = [1200, 1500, 1800, 1100, 2500, 2200, 900, 1050]

# a) Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(companies, recruits, color='skyblue')
plt.title('New Recruitments by Company')
plt.ylabel('Number of Recruits')
plt.show()

# b) Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(recruits, labels=companies, autopct='%1.1f%%')
plt.title('Recruitment Distribution')
plt.show()

# c) Customized Pie Chart (Exploding the highest recruitment)
explode = [0.1 if r == max(recruits) else 0 for r in recruits] 
plt.figure(figsize=(8, 8))
plt.pie(recruits, labels=companies, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Customized Recruitment Distribution')
plt.show()

# d) Doughnut Chart
plt.figure(figsize=(8, 8))
plt.pie(recruits, labels=companies, autopct='%1.1f%%', pctdistance=0.85)
# Draw circle at center to make it a doughnut
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('New Recruitments (Doughnut Chart)')
plt.show()

# Comparison: IBM & Amdocs
comp_names = ['IBM', 'Amdocs']
comp_values = [recruits[companies.index('IBM')], recruits[companies.index('Amdocs')]]

plt.figure(figsize=(6, 4))
plt.bar(comp_names, comp_values, color=['blue', 'green'])
plt.title('Comparison: IBM vs Amdocs Recruitments')
plt.ylabel('Number of Recruits')
plt.show()
