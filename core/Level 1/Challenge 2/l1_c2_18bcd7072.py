#creating a ditionary
dictionary = {'Fruits' : ['Mango', 'Apple', 'Orange'], 'Colours' : ['Blue', 'Green', 'Red']}

#saving it as pickle file
with open('output.pkl', 'wb') as file:
    pickle.dump(dictionary,file)

#reading the pickle file with dictionary
with open('output.pkl', 'rb') as file:
    my_dict = pickle.load(file)

print(my_dict)
#updating a list in it
my_dict['Fruits'].append("Banana")

#saving it again
with open('output.pkl', 'wb') as file:
    pickle.dump(my_dict, file)

#updation verification
with open('output.pkl', 'rb') as file:
    my_dict = pickle.load(file)
my_dict