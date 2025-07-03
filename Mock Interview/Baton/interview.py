import json
import os


class JsonAnalyzer:
    def __init__(self) -> None:
        with open("Mock Interview/Baton/test.json", 'r') as f:
            self.json_data = json.load(f)
    
    def returnAnswer(self):
        print('question 1')
        print(self.json_data[])
        return

def main():
    print("Begin the json file parse analysis")
    analyzer = JsonAnalyzer()
    analyzer.returnAnswer()

if __name__ == "__main__":
    main()