students = [
    {"name": "Lan", "group": "Python"},
    {"name": "Minh", "group": "Web"},
    {"name": "An", "group": "Python"},
]
counts = {}
for item in students:
    group = item["group"]
    counts[group] = counts.get(group, 0) + 1
print("Counts:", counts)