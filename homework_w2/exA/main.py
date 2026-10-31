score = int(input("Enter your valid score: "))
classification = "Exellent"
if(score >= 8):
    print(classification)
elif(score >= 5):
    classification = "Good"
    print(classification)
else:
    classification = "Need more hardworking!"
    print(classification)
