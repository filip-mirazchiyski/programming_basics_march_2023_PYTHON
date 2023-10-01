exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_time_in_minutes = exam_hours * 60 + exam_minutes
arrival_time_in_minutes = arrival_hours * 60 + arrival_minutes

diff = abs(exam_time_in_minutes - arrival_time_in_minutes)
hours = diff // 60
minutes = diff % 60

if exam_time_in_minutes == arrival_time_in_minutes:
    print("On time")
elif exam_time_in_minutes > arrival_time_in_minutes:
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    elif 30 < diff <= 59:
        print("Early")
        print(f"{diff} minutes before the start")
    else:
        print("Early")
        print(f"{hours}:{minutes:02d} hours before the start")
else:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        print(f"{hours}:{minutes:02d} hours after the start")
