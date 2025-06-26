import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

def create_parking_data():
    """Create sample parking data with check-in/check-out events"""
    parking_data = {
        "spots": [
            {"spot_id": "A1", "location": "North Section"},
            {"spot_id": "A2", "location": "North Section"},
            {"spot_id": "B1", "location": "South Section"},
            {"spot_id": "B2", "location": "South Section"}
        ],
        "events": [
            # Morning rush - 8-10 AM
            {"event_id": 1, "spot_id": "A1", "vehicle_id": "CAR001", "event_type": "check_in", "timestamp": "2024-01-15T08:00:00"},
            {"event_id": 2, "spot_id": "A2", "vehicle_id": "CAR002", "event_type": "check_in", "timestamp": "2024-01-15T08:15:00"},
            {"event_id": 3, "spot_id": "B1", "vehicle_id": "CAR003", "event_type": "check_in", "timestamp": "2024-01-15T08:30:00"},
            {"event_id": 4, "spot_id": "B2", "vehicle_id": "CAR004", "event_type": "check_in", "timestamp": "2024-01-15T08:45:00"},
            {"event_id": 5, "spot_id": "A1", "vehicle_id": "CAR005", "event_type": "check_in", "timestamp": "2024-01-15T09:00:00"},
            {"event_id": 6, "spot_id": "A2", "vehicle_id": "CAR006", "event_type": "check_in", "timestamp": "2024-01-15T09:15:00"},
            
            # First wave check-outs - 10-12 PM
            {"event_id": 7, "spot_id": "A1", "vehicle_id": "CAR001", "event_type": "check_out", "timestamp": "2024-01-15T10:30:00"},
            {"event_id": 8, "spot_id": "B1", "vehicle_id": "CAR003", "event_type": "check_out", "timestamp": "2024-01-15T11:00:00"},
            
            # Lunch rush - 12-2 PM
            {"event_id": 9, "spot_id": "A1", "vehicle_id": "CAR007", "event_type": "check_in", "timestamp": "2024-01-15T12:00:00"},
            {"event_id": 10, "spot_id": "B1", "vehicle_id": "CAR008", "event_type": "check_in", "timestamp": "2024-01-15T12:15:00"},
            {"event_id": 11, "spot_id": "A1", "vehicle_id": "CAR009", "event_type": "check_in", "timestamp": "2024-01-15T12:30:00"},
            {"event_id": 12, "spot_id": "B1", "vehicle_id": "CAR010", "event_type": "check_in", "timestamp": "2024-01-15T12:45:00"},
            {"event_id": 13, "spot_id": "A1", "vehicle_id": "CAR011", "event_type": "check_in", "timestamp": "2024-01-15T13:00:00"},
            {"event_id": 14, "spot_id": "B1", "vehicle_id": "CAR012", "event_type": "check_in", "timestamp": "2024-01-15T13:15:00"},
            {"event_id": 15, "spot_id": "A1", "vehicle_id": "CAR013", "event_type": "check_in", "timestamp": "2024-01-15T13:30:00"},
            
            # Afternoon check-outs - 2-4 PM
            {"event_id": 16, "spot_id": "A2", "vehicle_id": "CAR002", "event_type": "check_out", "timestamp": "2024-01-15T14:00:00"},
            {"event_id": 17, "spot_id": "B2", "vehicle_id": "CAR004", "event_type": "check_out", "timestamp": "2024-01-15T14:30:00"},
            {"event_id": 18, "spot_id": "A1", "vehicle_id": "CAR007", "event_type": "check_out", "timestamp": "2024-01-15T15:00:00"},
            
            # Evening rush - 5-7 PM
            {"event_id": 19, "spot_id": "A2", "vehicle_id": "CAR014", "event_type": "check_in", "timestamp": "2024-01-15T17:00:00"},
            {"event_id": 20, "spot_id": "B2", "vehicle_id": "CAR015", "event_type": "check_in", "timestamp": "2024-01-15T17:15:00"},
            {"event_id": 21, "spot_id": "A2", "vehicle_id": "CAR016", "event_type": "check_in", "timestamp": "2024-01-15T17:30:00"},
            {"event_id": 22, "spot_id": "B2", "vehicle_id": "CAR017", "event_type": "check_in", "timestamp": "2024-01-15T17:45:00"},
            {"event_id": 23, "spot_id": "A2", "vehicle_id": "CAR018", "event_type": "check_in", "timestamp": "2024-01-15T18:00:00"},
            
            # Late evening check-outs - 7-9 PM
            {"event_id": 24, "spot_id": "A1", "vehicle_id": "CAR005", "event_type": "check_out", "timestamp": "2024-01-15T19:00:00"},
            {"event_id": 25, "spot_id": "A2", "vehicle_id": "CAR006", "event_type": "check_out", "timestamp": "2024-01-15T19:30:00"}
        ]
    }
    
    with open("parking_data.json", "w") as f:
        json.dump(parking_data, f, indent=2)
    print("✅ Created parking_data.json with sample check-in/check-out data")

class PeakParkingAnalyzer:
    def __init__(self, filename="parking_data.json"):
        # Create sample data if file doesn't exist
        if not os.path.exists(filename):
            print("hehe")
            print(f"📝 Creating {filename}...")
            create_parking_data()
        
        # Load the data
        with open(filename, 'r') as f:
            self.data = json.load(f)
        
        self.events = self.data["events"]
        self.spots = self.data["spots"]
        print(f"✅ Loaded {len(self.events)} parking events")
    
    def find_peak_hours(self):
        """Find peak parking hours based on check-in activity"""
        print("\n⏰ PEAK HOURS ANALYSIS")
        
        hourly_checkins = defaultdict(int)
        hourly_checkouts = defaultdict(int)
        hourly_activity = defaultdict(int)
        
        for event in self.events:
            # Parse timestamp to get hour
            timestamp = event["timestamp"]
            dt = datetime.fromisoformat(timestamp)
            hour = dt.hour
            
            if event["event_type"] == "check_in":
                hourly_checkins[hour] += 1
            elif event["event_type"] == "check_out":
                hourly_checkouts[hour] += 1
            
            # Total activity (both check-ins and check-outs)
            hourly_activity[hour] += 1
        
        # Find peak hours
        peak_checkin_hour = max(hourly_checkins.items(), key=lambda x: x[1]) if hourly_checkins else (None, 0)
        peak_activity_hour = max(hourly_activity.items(), key=lambda x: x[1]) if hourly_activity else (None, 0)
        
        print(f"🔥 Peak check-in hour: {peak_checkin_hour[0]:02d}:00 ({peak_checkin_hour[1]} check-ins)")
        print(f"🔥 Peak activity hour: {peak_activity_hour[0]:02d}:00 ({peak_activity_hour[1]} total events)")
        
        # Show hourly breakdown
        print("\n📊 Hourly Activity Breakdown:")
        print("Hour    | Check-ins | Check-outs | Total")
        print("-" * 40)
        
        all_hours = sorted(set(list(hourly_checkins.keys()) + list(hourly_checkouts.keys())))
        for hour in all_hours:
            checkins = hourly_checkins.get(hour, 0)
            checkouts = hourly_checkouts.get(hour, 0)
            total = checkins + checkouts
            print(f"{hour:02d}:00   |     {checkins:2d}    |     {checkouts:2d}     |   {total:2d}")
        
        return peak_checkin_hour, peak_activity_hour
    
    def find_peak_spots(self):
        """Find which parking spots are most popular"""
        print("\n🅿️ SPOT POPULARITY ANALYSIS")
        
        spot_checkins = defaultdict(int)
        spot_activity = defaultdict(int)
        
        for event in self.events:
            spot_id = event["spot_id"]
            spot_activity[spot_id] += 1
            
            if event["event_type"] == "check_in":
                spot_checkins[spot_id] += 1
        
        # Find most popular spot
        most_popular_spot = max(spot_checkins.items(), key=lambda x: x[1]) if spot_checkins else (None, 0)
        print(f"🏆 Most popular spot: {most_popular_spot[0]} ({most_popular_spot[1]} check-ins)")
        
        # Show all spots
        print("\nSpot Activity:")
        for spot_id in sorted(spot_activity.keys()):
            checkins = spot_checkins.get(spot_id, 0)
            total = spot_activity[spot_id]
            print(f"  {spot_id}: {checkins} check-ins, {total} total events")
        
        return most_popular_spot
    
    def calculate_occupancy_over_time(self):
        """Calculate how many spots are occupied at each hour"""
        print("\n📈 OCCUPANCY OVER TIME")
        
        # Track occupancy changes throughout the day
        occupancy_timeline = []
        
        # Sort events by timestamp
        sorted_events = sorted(self.events, key=lambda x: x["timestamp"])
        
        current_occupancy = 0
        for event in sorted_events:
            dt = datetime.fromisoformat(event["timestamp"])
            
            if event["event_type"] == "check_in":
                current_occupancy += 1
            elif event["event_type"] == "check_out":
                current_occupancy = max(0, current_occupancy - 1)
            
            occupancy_timeline.append({
                "time": dt.strftime("%H:%M"),
                "occupancy": current_occupancy,
                "event": f"{event['event_type']} at {event['spot_id']}"
            })
        
        # Find peak occupancy
        max_occupancy = max(item["occupancy"] for item in occupancy_timeline)
        peak_times = [item for item in occupancy_timeline if item["occupancy"] == max_occupancy]
        
        print(f"🔝 Maximum occupancy: {max_occupancy} spots")
        print(f"🕐 Peak occupancy times:")
        for peak in peak_times[:3]:  # Show first 3 peak times
            print(f"   {peak['time']} - {peak['occupancy']} spots occupied ({peak['event']})")
        
        # Show occupancy timeline
        print("\n📋 Occupancy Timeline (key moments):")
        for i, item in enumerate(occupancy_timeline):
            if i % 3 == 0 or item["occupancy"] == max_occupancy:  # Show every 3rd event or peak moments
                print(f"   {item['time']}: {item['occupancy']} spots occupied")
        
        return max_occupancy, peak_times
    
    def answer_interview_questions(self):
        """Answer common interview questions about peak times"""
        print("\n" + "="*60)
        print("🎯 INTERVIEW QUESTIONS & ANSWERS")
        print("="*60)
        
        # Question 1: When is the busiest time?
        peak_checkin, peak_activity = self.find_peak_hours()
        print(f"\nQ1: When is the busiest time for parking?")
        print(f"A1: {peak_activity[0]:02d}:00 with {peak_activity[1]} parking events")
        
        # Question 2: Which spot is most in demand?
        popular_spot = self.find_peak_spots()
        print(f"\nQ2: Which parking spot is most popular?")
        print(f"A2: Spot {popular_spot[0]} with {popular_spot[1]} check-ins")
        
        # Question 3: What's the maximum occupancy?
        max_occ, peak_times = self.calculate_occupancy_over_time()
        print(f"\nQ3: What's the highest number of occupied spots at once?")
        print(f"A3: {max_occ} spots, first reached at {peak_times[0]['time']}")
        
        # Question 4: When should maintenance be scheduled?
        hourly_activity = defaultdict(int)
        for event in self.events:
            dt = datetime.fromisoformat(event["timestamp"])
            hourly_activity[dt.hour] += 1
        
        if hourly_activity:
            avg_activity = sum(hourly_activity.values()) / len(hourly_activity)
            quiet_hours = [hour for hour, count in hourly_activity.items() if count < avg_activity * 0.5]
            print(f"\nQ4: When should we schedule maintenance?")
            if quiet_hours:
                print(f"A4: During low-activity hours: {', '.join([f'{h:02d}:00' for h in sorted(quiet_hours)])}")
            else:
                print(f"A4: Early morning or late evening when no events recorded")

def main():
    print("🚗 Peak Parking Time Analyzer")
    print("=" * 50)
    print("Problem: Find peak parking times from check-in/check-out data")
    
    # Create analyzer (will auto-create JSON if needed)
    analyzer = PeakParkingAnalyzer()
    
    # Run the analysis
    analyzer.answer_interview_questions()
    
    print(f"\n✅ Analysis complete!")
    print(f"📁 Data file: parking_data.json")
    print(f"💡 This demonstrates: JSON parsing, time analysis, peak detection")

if __name__ == "__main__":
    main()