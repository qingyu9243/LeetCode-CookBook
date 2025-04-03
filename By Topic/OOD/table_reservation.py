from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class Table:
    def __init__(self, table_id: int, capacity: int):
        """Initialize a table with ID and seating capacity.
        
        Args:
            table_id: Unique identifier for the table
            capacity: Maximum number of people the table can seat
        """
        self.table_id = table_id
        self.capacity = capacity
        self.is_reserved = False


class Reservation:
    def __init__(self, reservation_id: int, customer_name: str, phone_number: str, 
                 party_size: int, table_id: int, date_time: datetime, duration: int = 2):
        """Initialize a reservation.
        
        Args:
            reservation_id: Unique identifier for the reservation
            customer_name: Name of the customer making the reservation
            phone_number: Customer's phone number
            party_size: Number of people in the party
            table_id: ID of the reserved table
            date_time: Date and time of the reservation
            duration: Expected duration in hours (default: 2 hours)
        """
        self.reservation_id = reservation_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.party_size = party_size
        self.table_id = table_id
        self.date_time = date_time
        self.duration = duration
        self.status = "Confirmed"  # Other statuses: "Canceled", "Completed"


class ReservationSystem:
    def __init__(self, restaurant_name: str, opening_time: int = 9, closing_time: int = 22):
        """Initialize the reservation system for a restaurant.
        
        Args:
            restaurant_name: Name of the restaurant
            opening_time: Hour when the restaurant opens (24-hour format)
            closing_time: Hour when the restaurant closes (24-hour format)
        """
        self.restaurant_name = restaurant_name
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.tables: Dict[int, Table] = {}
        self.reservations: Dict[int, Reservation] = {}
        self.reservation_counter = 1000
        
    def add_table(self, table_id: int, capacity: int) -> Table:
        """Add a new table to the restaurant.
        
        Args:
            table_id: Unique identifier for the table
            capacity: Maximum number of people the table can seat
            
        Returns:
            The newly created Table object
        """
        if table_id in self.tables:
            raise ValueError(f"Table with ID {table_id} already exists")
        
        table = Table(table_id, capacity)
        self.tables[table_id] = table
        return table
    
    def is_table_available(self, table_id: int, date_time: datetime, duration: int) -> bool:
        """Check if a table is available at the specified date and time.
        
        Args:
            table_id: ID of the table to check
            date_time: Date and time to check availability
            duration: Duration in hours
            
        Returns:
            True if table is available, False otherwise
        """
        if table_id not in self.tables:
            return False
        
        # Check if restaurant is open at that time
        hour = date_time.hour
        if hour < self.opening_time or hour >= self.closing_time:
            return False
        
        # Check if table is already reserved at that time
        requested_start = date_time
        requested_end = date_time + timedelta(hours=duration)
        
        for reservation in self.reservations.values():
            if reservation.status == "Canceled":
                continue
                
            if reservation.table_id == table_id:
                reserved_start = reservation.date_time
                reserved_end = reserved_start + timedelta(hours=reservation.duration)
                
                # Check for overlap
                if (requested_start < reserved_end and 
                    requested_end > reserved_start):
                    return False
        
        return True
    
    def find_available_table(self, party_size: int, date_time: datetime, 
                             duration: int = 2) -> Optional[int]:
        """Find an available table that can accommodate the party size.
        
        Args:
            party_size: Number of people in the party
            date_time: Date and time of the reservation
            duration: Expected duration in hours
            
        Returns:
            Table ID if available, None otherwise
        """
        suitable_tables = []
        
        for table_id, table in self.tables.items():
            if (table.capacity >= party_size and 
                self.is_table_available(table_id, date_time, duration)):
                suitable_tables.append((table_id, table.capacity))
        
        if not suitable_tables:
            return None
        
        # Find the table with the capacity closest to the party size
        suitable_tables.sort(key=lambda x: x[1])
        for table_id, capacity in suitable_tables:
            if capacity >= party_size:
                return table_id
        
        return None
    
    def make_reservation(self, customer_name: str, phone_number: str, party_size: int, 
                        date_time: datetime, duration: int = 2) -> Optional[Reservation]:
        """Make a new reservation.
        
        Args:
            customer_name: Name of the customer
            phone_number: Customer's phone number
            party_size: Number of people in the party
            date_time: Date and time of the reservation
            duration: Expected duration in hours
            
        Returns:
            Reservation object if successful, None otherwise
        """
        table_id = self.find_available_table(party_size, date_time, duration)
        if table_id is None:
            return None
        
        reservation_id = self.reservation_counter
        self.reservation_counter += 1
        
        reservation = Reservation(
            reservation_id=reservation_id,
            customer_name=customer_name,
            phone_number=phone_number,
            party_size=party_size,
            table_id=table_id,
            date_time=date_time,
            duration=duration
        )
        
        self.reservations[reservation_id] = reservation
        return reservation
    
    def cancel_reservation(self, reservation_id: int) -> bool:
        """Cancel an existing reservation.
        
        Args:
            reservation_id: ID of the reservation to cancel
            
        Returns:
            True if canceled successfully, False otherwise
        """
        if reservation_id not in self.reservations:
            return False
        
        reservation = self.reservations[reservation_id]
        reservation.status = "Canceled"
        return True
    
    def get_reservations_for_date(self, date: datetime.date) -> List[Reservation]:
        """Get all reservations for a specific date.
        
        Args:
            date: Date to get reservations for
            
        Returns:
            List of Reservation objects
        """
        return [
            reservation for reservation in self.reservations.values()
            if reservation.date_time.date() == date and reservation.status != "Canceled"
        ]
    
    def get_table_reservations(self, table_id: int, date: datetime.date) -> List[Reservation]:
        """Get reservations for a specific table on a specific date.
        
        Args:
            table_id: ID of the table
            date: Date to get reservations for
            
        Returns:
            List of Reservation objects
        """
        return [
            reservation for reservation in self.reservations.values()
            if reservation.table_id == table_id and 
            reservation.date_time.date() == date and 
            reservation.status != "Canceled"
        ]
    
    def get_available_time_slots(self, date: datetime.date, party_size: int, 
                               duration: int = 2) -> List[datetime]:
        """Get available time slots for a specific date and party size.
        
        Args:
            date: Date to check availability
            party_size: Number of people in the party
            duration: Expected duration in hours
            
        Returns:
            List of available datetime slots
        """
        available_slots = []
        
        # Check availability in 30-minute increments
        for hour in range(self.opening_time, self.closing_time):
            for minute in [0, 30]:
                time_slot = datetime.combine(date, datetime.min.time().replace(hour=hour, minute=minute))
                
                if self.find_available_table(party_size, time_slot, duration) is not None:
                    available_slots.append(time_slot)
        
        return available_slots


# Example usage
if __name__ == "__main__":
    # Create a reservation system for a restaurant
    restaurant = ReservationSystem("Delicious Bites", opening_time=11, closing_time=22)
    
    # Add tables
    restaurant.add_table(1, 2)  # Table 1 seats 2 people
    restaurant.add_table(2, 2)  # Table 2 seats 2 people
    restaurant.add_table(3, 4)  # Table 3 seats 4 people
    restaurant.add_table(4, 4)  # Table 4 seats 4 people
    restaurant.add_table(5, 6)  # Table 5 seats 6 people
    restaurant.add_table(6, 8)  # Table 6 seats 8 people
    
    # Set a date for reservations
    tomorrow = datetime.now().date() + timedelta(days=1)
    
    # Make some reservations
    reservation1 = restaurant.make_reservation(
        "John Smith", "555-1234", 2,
        datetime.combine(tomorrow, datetime.min.time().replace(hour=18, minute=0))
    )
    
    reservation2 = restaurant.make_reservation(
        "Jane Doe", "555-5678", 4,
        datetime.combine(tomorrow, datetime.min.time().replace(hour=19, minute=0))
    )
    
    # Check available time slots for a party of 4
    available_slots = restaurant.get_available_time_slots(tomorrow, 4)
    print(f"Available time slots for a party of 4 tomorrow:")
    for slot in available_slots:
        print(f"  {slot.strftime('%I:%M %p')}")
    
    # Cancel a reservation
    if reservation1:
        restaurant.cancel_reservation(reservation1.reservation_id)
        print(f"Canceled reservation for {reservation1.customer_name}")
    
    # Get reservations for tomorrow
    tomorrow_reservations = restaurant.get_reservations_for_date(tomorrow)
    print(f"\nReservations for tomorrow:")
    for reservation in tomorrow_reservations:
        print(f"  {reservation.customer_name} - Table {reservation.table_id} - "
              f"{reservation.date_time.strftime('%I:%M %p')} - Party of {reservation.party_size}")