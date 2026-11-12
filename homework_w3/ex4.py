student = {"id": "SV01", "name": "Lan", "score": 7}
student["score"] = 8.5
student["city"] = "Thai Nguyen"
phone = student.get("phone", "Chua co")
print("Score:", student["score"])
print("City:", student["city"])
print("Phone:", phone)