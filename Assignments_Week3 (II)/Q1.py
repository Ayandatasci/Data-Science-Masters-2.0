'''Q1. Create a python program to sort the given list of tuples based on integer value using a
lambda function. (without using sorted function)
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]'''

data = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

sorted_data = sorted(data, key=lambda x: x[1])

for item in sorted_data:
    print(item)