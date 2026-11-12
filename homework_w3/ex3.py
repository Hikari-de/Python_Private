raw_names = [" Lan ", "Minh", "Lan", "  ", " An  "]
unique_names = []
for raw in raw_names:
    name = raw.strip()
    if name != "" and name not in unique_names:
        unique_names.append(name)
print("Unique names:", unique_names)
 