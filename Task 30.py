from datetime import datetime, timedelta
def lectures(start_date):
    lecture_dates = []
    lecture_date = start_date
    for i in range(32):
        while lecture_date.weekday() not in [0, 3]:
            lecture_date += timedelta(days=1)
        lecture_dates.append(lecture_date)
        lecture_date += timedelta(days=3)
    return lecture_dates
start_date = datetime(2023, 3, 27, 19, 15)
lectures = lectures(start_date)
for i, lecture_date in enumerate(lectures):
    print(f"Lecture {i+1:2}: {lecture_date.strftime('%d %b %Y %H:%M')}")

