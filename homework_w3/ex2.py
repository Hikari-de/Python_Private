scores = [8, 4, 9, 5]
total = 0
highest = scores[0]
passed_count = 0
for score in scores:
    total += score
    if score > highest:
        highest = score
    if score >= 5:
        passed_count += 1
average = total / len(scores)
print("Average:", average)
print("Highest:", highest)
print("Passed count:", passed_count)