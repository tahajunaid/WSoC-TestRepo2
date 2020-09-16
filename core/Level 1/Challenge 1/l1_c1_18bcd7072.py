import pickle

with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

display(data)