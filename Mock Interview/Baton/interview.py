import json
from datetime import datetime

class JsonAnalyzer:
    def __init__(self) -> None:
        with open("Mock Interview/Baton/test.json", 'r') as f:
            self.json_data = json.load(f)
    
    def convertToDatetime(self):
        for entry in self.json_data:
            # get entrance and exit timestamp
            entrance_time = entry['entrance_time']
            exit_time = entry['exit_time']
            date_formate = "%Y-%m-%d %H:%M:%S"
            py_dt_entrance = py_dt_exit = None
            if entrance_time:
                py_dt_entrance = datetime.strptime(entrance_time, date_formate)
            if exit_time:
                py_dt_exit = datetime.strptime(exit_time, date_formate)
            # change the formate
            entry['entrance_time'] = py_dt_entrance
            entry['exit_time'] = py_dt_exit

        return self.json_data
    
    def getEventByFacilityAndDate(self, facility_id, date):
        filtered_events = []
        for entry in self.json_data:
            print(type(entry))
            entrance_date = entry['entrance_time']
            if not entrance_date:
                entrance_date = datetime.today()
            exit_date = entry['exit_time']
            if not exit_date:
                exit_date = datetime.today()
            facility = entry['facility_id']
            if date.date() >= entrance_date.date() and date.date() <= exit_date.date() and facility == facility_id:
                filtered_events.append(entry)
        return len(filtered_events)

def main():
    print("Begin the json file parse analysis")
    analyzer = JsonAnalyzer()
    #print(analyzer.json_data[0])
    # part -zero
    analyzer.convertToDatetime()
    # part - one
    filter_date = datetime.strptime("2022-01-18 00:00:00", "%Y-%m-%d %H:%M:%S") # 2022-01-18 10:00:00
    print(analyzer.getEventByFacilityAndDate(1, filter_date))

if __name__ == "__main__":
    main()