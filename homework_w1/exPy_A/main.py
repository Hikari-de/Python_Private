
math_score = float(input("Enter math score: "))
english_score = float(input("Enter english score: "))
python_score = float(input("Enter python score: "))

average_score = (math_score + english_score + python_score) / 3.0

report = f"Average score : {average_score:.2f}"

print(report)