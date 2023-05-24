import json
import random

def shuffle():
    # Load the JSON data
    with open('jobs.json', 'r') as f:
        data = json.load(f)

    # Group the data by priority level
    grouped_data = {}
    for item in data:
        priority = item['priority']
        if priority not in grouped_data:
            grouped_data[priority] = []
        grouped_data[priority].append(item)

    # Shuffle the data within each priority level
    for priority in grouped_data:
        random.shuffle(grouped_data[priority])

    # Flatten the data back into a list, sorted by priority
    sorted_data = []
    for priority in sorted(map(int, grouped_data.keys())):
        sorted_data += grouped_data[priority]
    with open('jobs.json', 'w') as f:
        json.dump(soted_data, f)
    # Print the sorted and shuffled data
    #print(sorted_data)
shuffle()
