"""
Imagine you want to schedule a meeting with a co-worker. You have access 
to your free time slots and your co-worker's free time slots, both given 
in the form of [startTime, endTime].

Write a function that takes in your free time slots, your co-worker's free 
time slots, and the duration of the meeting that you want to schedule, and 
returns a list of all the overlapping free time blocks (in the form of 
[startTime, endTime]) during which you could schedule the meeting, ordered 
from the earliest time block to the latest.

Sample Input
myFreeTime = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
coworkerFreeTime = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
duration = 30

Sample Output
[["10:00", "10:30"], ["12:30", "13:00"], ["16:00", "17:00"]]
"""
def convert_to_minutes(time_str):
    # Converts time string in "HH:MM" format to minutes since midnight
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def convert_to_time_str(minutes):
    # Converts minutes since midnight to time string in "HH:MM" format
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02d}:{minutes:02d}"

def find_meeting_slots(myFreeTime, coworkerFreeTime, duration):
    # Convert all time strings to minutes
    myFreeTime = [[convert_to_minutes(start), convert_to_minutes(end)] for start, end in myFreeTime]
    coworkerFreeTime = [[convert_to_minutes(start), convert_to_minutes(end)] for start, end in coworkerFreeTime]

    # Merge and sort the free time slots
    mergedFreeTime = sorted(myFreeTime + coworkerFreeTime)
    
    # Find overlapping free time slots
    overlaps = []
    prev_start, prev_end = mergedFreeTime[0]
    
    for start, end in mergedFreeTime[1:]:
        if start <= prev_end:  # There's an overlap
            overlap_start = max(prev_start, start)
            overlap_end = min(prev_end, end)
            if overlap_end - overlap_start >= duration:
                overlaps.append([overlap_start, overlap_end])
            prev_end = max(prev_end, end)  # Extend the end time to the latest end time
        else:
            prev_start, prev_end = start, end
    
    # Convert time back to "HH:MM" format
    return [[convert_to_time_str(start), convert_to_time_str(end)] for start, end in overlaps]

# Sample Input
myFreeTime = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
coworkerFreeTime = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
duration = 30

# Find and print meeting slots
print(find_meeting_slots(myFreeTime, coworkerFreeTime, duration))
print(find_meeting_slots(myFreeTime, coworkerFreeTime, 60))