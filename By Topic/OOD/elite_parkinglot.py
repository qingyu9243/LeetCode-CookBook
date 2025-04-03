from datetime import datetime, time
from typing import List


class ParkingLot:
    def __init__(self, capacity: int, working_hour_rate: float, after_hour_rate: float):
        """Initialize the parking lot with given capacity and rates.
        
        Args:
            capacity: Total number of parking spaces
            working_hour_rate: Hourly rate during working hours (9AM-5PM)
            after_hour_rate: Hourly rate outside of working hours
        """
        self.capacity = capacity
        self.available_spaces = capacity
        self.working_hour_rate = working_hour_rate
        self.after_hour_rate = after_hour_rate
        self.tickets = {}  # Dictionary to store tickets: {ticket_id: Ticket object}
        self.ticket_counter = 1000  # Starting ticket number
        
    def get_available_spaces(self) -> int:
        """Return the number of available parking spaces."""
        return self.available_spaces
    
    def is_full(self) -> bool:
        """Check if the parking lot is full."""
        return self.available_spaces == 0
    
    def is_working_hour(self, current_time: datetime) -> bool:
        """Check if the given time is during working hours (9AM-5PM)."""
        working_start = time(9, 0)  # 9 AM
        working_end = time(17, 0)  # 5 PM
        current_time_only = current_time.time()
        return working_start <= current_time_only < working_end and current_time.weekday() < 5  # Weekdays only
    
    def get_rate(self, current_time: datetime) -> float:
        """Get the hourly rate based on the current time."""
        if self.is_working_hour(current_time):
            return self.working_hour_rate
        return self.after_hour_rate
    
    def issue_ticket(self) -> 'Ticket':
        """Issue a ticket for a car entering the parking lot."""
        if self.is_full():
            raise Exception("Parking lot is full")
        
        self.available_spaces -= 1
        ticket_id = f"T{self.ticket_counter}"
        self.ticket_counter += 1
        entry_time = datetime.now()
        
        ticket = Ticket(ticket_id, entry_time)
        self.tickets[ticket_id] = ticket
        
        # Update display board
        self.update_display_board()
        
        return ticket
    
    def calculate_fee(self, ticket_id: str) -> float:
        """Calculate the parking fee for a given ticket."""
        if ticket_id not in self.tickets:
            raise Exception("Invalid ticket")
        
        ticket = self.tickets[ticket_id]
        if ticket.exit_time is None:
            ticket.exit_time = datetime.now()
        
        # Calculate duration in hours
        duration = (ticket.exit_time - ticket.entry_time).total_seconds() / 3600
        
        # Calculate fee based on the hourly rates during different periods
        fee = 0
        current_time = ticket.entry_time
        
        while current_time < ticket.exit_time:
            # Check the rate for the current hour
            hourly_rate = self.get_rate(current_time)
            
            # Calculate how much of the hour to charge
            next_hour = datetime(
                current_time.year, current_time.month, current_time.day,
                current_time.hour + 1, 0, 0
            )
            
            if next_hour > ticket.exit_time:
                next_hour = ticket.exit_time
            
            hour_fraction = (next_hour - current_time).total_seconds() / 3600
            fee += hourly_rate * hour_fraction
            
            current_time = next_hour
        
        return round(fee, 2)
    
    def process_payment(self, ticket_id: str) -> float:
        """Process payment for a ticket and release the parking space."""
        fee = self.calculate_fee(ticket_id)
        
        # Mark the ticket as paid
        self.tickets[ticket_id].is_paid = True
        
        # Release the parking space
        self.available_spaces += 1
        
        # Update display board
        self.update_display_board()
        
        return fee
    
    def update_display_board(self):
        """Update the display board with current available spaces."""
        # In a real implementation, this might interface with hardware
        # For this example, we'll just print to console
        print(f"Display Board: {self.available_spaces} parking spaces available")


class Ticket:
    def __init__(self, ticket_id: str, entry_time: datetime):
        """Initialize a new ticket.
        
        Args:
            ticket_id: Unique identifier for the ticket
            entry_time: Time when the ticket was issued
        """
        self.ticket_id = ticket_id
        self.entry_time = entry_time
        self.exit_time = None
        self.is_paid = False
    
    def __str__(self):
        return f"Ticket {self.ticket_id}, Entry: {self.entry_time}"


class DisplayBoard:
    def __init__(self, parking_lot: ParkingLot):
        """Initialize the display board for a parking lot.
        
        Args:
            parking_lot: The parking lot to display information for
        """
        self.parking_lot = parking_lot
    
    def display(self):
        """Display the current available spaces."""
        available = self.parking_lot.get_available_spaces()
        print(f"PARKING LOT STATUS: {available}/{self.parking_lot.capacity} spaces available")


class ParkingAttendant:
    def __init__(self, parking_lot: ParkingLot):
        """Initialize a parking attendant for a parking lot.
        
        Args:
            parking_lot: The parking lot the attendant works for
        """
        self.parking_lot = parking_lot
    
    def issue_ticket(self) -> Ticket:
        """Issue a ticket for a car entering the parking lot."""
        return self.parking_lot.issue_ticket()
    
    def process_payment(self, ticket_id: str) -> float:
        """Process payment for a ticket."""
        return self.parking_lot.process_payment(ticket_id)


# Example usage
if __name__ == "__main__":
    # Create a parking lot with 10 spaces, $5/hr during working hours, $2/hr after hours
    parking_lot = ParkingLot(10, 5.0, 2.0)
    
    # Create a display board and parking attendant
    display_board = DisplayBoard(parking_lot)
    attendant = ParkingAttendant(parking_lot)
    
    # Display initial status
    display_board.display()
    
    # Simulate car entry
    print("\n--- Car 1 enters ---")
    ticket1 = attendant.issue_ticket()
    print(f"Ticket issued: {ticket1}")
    
    # Display updated status
    display_board.display()
    
    # Simulate another car entry
    print("\n--- Car 2 enters ---")
    ticket2 = attendant.issue_ticket()
    print(f"Ticket issued: {ticket2}")
    
    # Display updated status
    display_board.display()
    
    # Simulate car exit and payment
    print("\n--- Car 1 exits ---")
    # For demonstration, we'll manipulate the entry time to show fee calculation
    parking_lot.tickets[ticket1.ticket_id].entry_time = datetime.now().replace(
        hour=datetime.now().hour - 3  # Car was parked for 3 hours
    )
    fee = attendant.process_payment(ticket1.ticket_id)
    print(f"Fee charged: ${fee}")
    
    # Display final status
    display_board.display()