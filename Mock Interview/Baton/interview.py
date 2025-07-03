import json

class JsonAnalyzer:
    def __init__(self) -> None:
        with open("Mock Interview/Baton/test.json", 'r') as f:
            self.json_data = json.load(f)
    
    def uniqueSpot(self):
        spots = self.json_data['spots']
        unique_locations = set()
        for spot in spots:
            unique_locations.add(spot['location'])
        return unique_locations

def main():
    print("Begin the json file parse analysis")
    analyzer = JsonAnalyzer()
    print(analyzer.uniqueSpot())

if __name__ == "__main__":
    main()