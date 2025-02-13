import json

# Step 1: Write JSON data to a file
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
print("Data written to 'data.json'")

# Step 2: Read JSON data from the file
with open('data.json', 'r') as file:
    data = json.load(file)
print("Data read from 'data.json':", data)

# Step 3: Update JSON data (change age)
data['age'] = 26

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
print("Data updated.")

# Step 4: Delete data (remove city)
if 'city' in data:
    del data['city']

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
print("Data updated by removing 'city'.")
