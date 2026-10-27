minutes_text = "185"

total_minutes = int(minutes_text)
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(hours, "hour", remaining_minutes, "minute")

if any(x is None for x in [total_minutes, hours, remaining_minutes]):
    print("Chua hoan thanh Bai B.")
else:
    assert isinstance(total_minutes, int)
    assert (hours, remaining_minutes) == (3, 5)
    print("Dat Bai B: 3 gio 5 phut.")