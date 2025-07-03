import json
import os


class PeakParkingAnalyzer:
    def __init__(self) -> None:
        with open("Mock Interview/Baton/test.json", 'r') as f:
            json_data = json.load(f)
        print(type(json_data))
    
    def returnAnswer(self):
        print('question 1')

def main():
    print("Peak Parking analysis")

    analyzer = PeakParkingAnalyzer()
    analyzer.returnAnswer()

if __name__ == "__main__":
    main()