from datetime import datetime, timedelta

first_lecture = datetime(2023, 3, 27, 19, 15)
lectures= [first_lecture+ timedelta(days=3*i) for i in range(32)]

for i, lectures_dates in enumerate(lectures):
    print(f"Lecture {i+1:2}: {lectures_dates.strftime('%d %b %Y %H:%M')}")
