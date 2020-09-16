import matplotlib.pyplot as plt
import pickle

with open('data.pkl', 'rb') as file:
    my_dict = pickle.load(file)

keys, values = zip(*my_dict.items())
keys,values=list(keys),list(values)

print(keys)
print(values)



plt.bar(keys,values)
plt.title("BAR PLOT")
plt.xticks(rotation=70)
plt.show()

plt.pie(values,labels=keys, autopct='%1.1f%%',shadow=True, startangle=90)
plt.axis('equal')
plt.title("PIE CHART")
plt.show()
