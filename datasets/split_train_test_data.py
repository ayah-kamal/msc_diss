from sklearn.model_selection import train_test_split
import json

with open('elsevier_data_alpaca_format.json', 'r') as f:
  data = json.load(f)

# Separate inputs, outputs, and instructions
inputs = [item["input"] for item in data]
outputs = [item["output"] for item in data]
instructions = [item["instruction"] for item in data]

# Split data based on unique output labels
unique_labels = list(set(outputs))
print(unique_labels)
train_data = []
test_data = []

for label in unique_labels:
    # Split data for labels with more than 1 instance
    label_indices = [i for i, x in enumerate(outputs) if x == label]
    if outputs.count(label) > 1:
        train_indices, test_indices = train_test_split(label_indices, test_size=0.2, random_state=42)
    else:
        train_indices, test_indices = label_indices, label_indices
    
    
    for idx in train_indices:
        train_data.append({"instruction": instructions[idx], "input": inputs[idx], "output": outputs[idx]})
    
    for idx in test_indices:
        test_data.append({"instruction": instructions[idx], "input": inputs[idx], "output": outputs[idx]})

# Save train data to a JSON file
with open('train_data_80.json', 'w') as json_file:
    json.dump(train_data, json_file, indent=4)

# Save test data to a JSON file
with open('test_data_20.json', 'w') as json_file:
    json.dump(test_data, json_file, indent=4)

print("Train data saved in 'train_data.json'")
print("Test data saved in 'test_data.json'")


