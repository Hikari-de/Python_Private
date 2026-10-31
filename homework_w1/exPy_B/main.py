minutes_text = "185"

total_minutes = int(minutes_text)
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(hours, "hour", remaining_minutes, "minute")