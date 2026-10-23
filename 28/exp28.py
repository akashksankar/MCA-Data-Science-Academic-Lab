import matplotlib.pyplot as plt
import numpy as np
languages=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7,]
#(i) Bar chart of popularity
plt.figure(figsize=(8,5))
plt.bar(languages,popularity,color='skyblue')
plt.title('popularity of programming languages')
plt.xlabel('programing languages')
plt.ylabel('popularity(%)')
plt.show()

#(ii)Horizontal Barchart of popularity
plt.figure(figsize=(8,5))
plt.barh(languages,popularity,color='red')
plt.title('popularity of programming languages(horizonatal)')
plt.xlabel('popularity(%)')
plt.ylabel('programing languages')
plt.show()


#(iii) bar chart with different color for each bar
colors=['blue','orange','green','red','purple','cyan']
plt.figure(figsize=(8,5))
plt.bar(languages,popularity,color=colors)
plt.title('popularity of programming languages(different colors)')
plt.xlabel('programming languages')
plt.ylabel('popularity(%)')

plt.show()


#(iv) pie chart of  popularity
plt.figure(figsize=(8,5))
plt.pie(popularity,labels=languages,autopct='%1.1f%%',startangle=140)
plt.title('popularity of programming languages(pie chart)')
plt.axis('equal')#equal aspect ratio ensures that pie chart is circle
plt.show()

