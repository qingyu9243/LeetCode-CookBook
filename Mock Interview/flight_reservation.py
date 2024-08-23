from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from decimal import Decimal
import uuid

class Cabin(Enum):
    ECONOMY = "ECONOMY"
    PREMIUM_ECONOMY = "PREMIUM_ECONOMY"
    BUSINESS = "BUSINESS"
    FIRST = "FIRST"

@dataclass
class Flight:
    flight_number: str
    departure: datetime
    departure_airport: str
    arrival_airport: str
    airline_code: str
    cabin: Cabin
    price: Decimal

@dataclass
class User:
    uuid: uuid.UUID
    email: str

@dataclass
class Booking:
    flight: Flight
    user: User
    uuid: uuid.UUID

@dataclass
class CreditCard:
    uuid: uuid.UUID
    card_number: str
    ccv: str
    card_holder_first_name: str
    card_holder_last_name: str
    expiration_month_year: datetime

class FlightProvider(ABC):
    @abstractmethod
    def book_flight(self, flight: Flight, user: User):
        pass

    def is_valid_seat(self, flight: Flight) -> bool:
        # Stub method, should be implemented
        return True

    def is_valid_payment_info(self, credit_card: CreditCard, user: User) -> bool:
        # Stub method, should be implemented
        return True


class PaymentService(ABC):
    @abstractmethod
    def make_charge(self, price: Decimal, credit_card: CreditCard, user: User) -> bool:
        pass


class DatabaseService(ABC):
    @abstractmethod
    def record_booking(self, booking: Booking):
        pass


class FlightBookingService:
    def __init__(self, flight_provider: FlightProvider, payment_service: PaymentService, database_service: DatabaseService):
        self.flight_provider = flight_provider
        self.payment_service = payment_service
        self.database_service = database_service

    def book_flight(self, flight: Flight, credit_card: CreditCard, user: User) -> Booking:
        try:
            # Validate seat availability
            if not self.flight_provider.is_valid_seat(flight):
                raise ValueError("Invalid seat or flight is full")

            # Validate payment info
            if not self.flight_provider.is_valid_payment_info(credit_card, user):
                raise ValueError("Invalid payment information")

            # Charge the customer
            if not self.payment_service.make_charge(flight.price, credit_card, user):
                raise ValueError("Payment failed")

            # Book the flight with the provider
            self.flight_provider.book_flight(flight, user)

            # Create booking
            booking = Booking(flight=flight, user=user, uuid=uuid.uuid4())

            # Record booking in the database
            self.database_service.record_booking(booking)

            return booking

        except Exception as e:
            print(f"Failed to book flight: {str(e)}")
            raise

# Sample concrete classes implementing the abstract base classes
class ConcreteFlightProvider(FlightProvider):
    def book_flight(self, flight: Flight, user: User):
        print(f"Flight {flight.flight_number} booked for user {user.email}")

class ConcretePaymentService(PaymentService):
    def make_charge(self, price: Decimal, credit_card: CreditCard, user: User) -> bool:
        print(f"Charged {price} to card {credit_card.card_number} for user {user.email}")
        return True

class ConcreteDatabaseService(DatabaseService):
    def __init__(self):
        self.booked_flights = {}

    def record_booking(self, booking: Booking):
        self.booked_flights[str(booking.uuid)] = booking
        print(f"Booking {booking.uuid} recorded for flight {booking.flight.flight_number}")

# Example usage
flight_provider = ConcreteFlightProvider()
payment_service = ConcretePaymentService()
database_service = ConcreteDatabaseService()

flight_booking_service = FlightBookingService(flight_provider, payment_service, database_service)

flight = Flight(
    flight_number="AB123",
    departure=datetime.now(),
    departure_airport="JFK",
    arrival_airport="LAX",
    airline_code="AB",
    cabin=Cabin.ECONOMY,
    price=Decimal("199.99")
)

user = User(uuid=uuid.uuid4(), email="user@example.com")
credit_card = CreditCard(
    uuid=uuid.uuid4(),
    card_number="1234567890123456",
    ccv="123",
    card_holder_first_name="John",
    card_holder_last_name="Doe",
    expiration_month_year=datetime(2025, 12, 1)
)

booking = flight_booking_service.book_flight(flight, credit_card, user)
print(f"Booking completed: {booking.uuid}")

######################################################
"""
Flight reservation(Need to book space by weight, allow overbooking) 

To begin implementing our booking system, we must first determine if orders can be fulfilled.
For now, each order consists of an origin and a destination. Given a network of flights,
create a function to determine if a booking order can be satisfied (a direct flight exists
between origin and destination.
How you choose to model orders, the flights, and the network is totally up to you.

"""
@dataclass
class Flight:
    flight_number: str
    departure: datetime
    departure_airport: str
    arrival_airport: str
    airline_code: str
    cabin: Cabin
    price: Decimal  

@dataclass
class FlightNetwork:
    network: dict #{ city1: 
                  #     {city2: number1, 
                  #     city3: number2}
                  # }
    
from collections import deque

class FlightReservationSystem:
    # task 1 direct flights
    def canDirectBook(self, origin, destination, flight_network):
        if origin in flight_network.network:
            if destination in flight_network.network[origin]:
                return True
        return False
    # task 2 connected flights
    def canConnectBook(self, origin, destination, flight_network):
        if origin not in flight_network.network:
            return False
        queue =deque([origin])
        visited = set()

        while queue:
            cur_start = queue.popleft()
            if cur_start == destination:
                return True
            if cur_start in flight_network.network:
                cur_possible_next = flight_network.network[cur_start].keys()
                for city in cur_possible_next:
                    if city not in visited:
                        queue.append(city)
                        visited.add(city)
        return False
    
    # task 3 fewest connection
    def fewestConnect(self, origin, destination, flight_network):
        if origin not in flight_network.network:
            return False
        queue =deque([origin])
        visited = set()
        reversed_path = {}
        while queue:
            cur_start = queue.popleft()
            if cur_start == destination:
                path = []
                while cur_start in reversed_path:
                    #print(cur_start, reversed_path)
                    path.append(cur_start)
                    pre_start = cur_start
                    cur_start = reversed_path[cur_start]
                    del reversed_path[pre_start]
                return path[::-1]
            if cur_start in flight_network.network:
                cur_possible_next = flight_network.network[cur_start].keys()
                for city in cur_possible_next:
                    if city not in visited:
                        queue.append(city)
                        visited.add(city)
                        reversed_path[city] = cur_start
        return []
    
    # task 4 lowest cost connection
    def lowestCostConnect(self, origin, destination, flight_network_cost):
        if origin not in flight_network.network:
            return False
        queue =deque([origin])
        visited = set()
        reversed_path = {}
        while queue:
            cur_start = queue.popleft()
            if cur_start == destination:
                path = []
                while cur_start in reversed_path:
                    #print(cur_start, reversed_path)
                    path.append(cur_start)
                    pre_start = cur_start
                    cur_start = reversed_path[cur_start]
                    del reversed_path[pre_start]
                return path[::-1]
            if cur_start in flight_network.network:
                cur_possible_next = flight_network.network[cur_start].keys()
                for city in cur_possible_next:
                    if city not in visited:
                        queue.append(city)
                        visited.add(city)
                        reversed_path[city] = cur_start
        return []    

flight_network = FlightNetwork(network={'sf': {'la':'a88', 'ny':'a5'}, 'la': {'sf':'a89', 'dc':'a6'}})
flight_network_cost = FlightNetwork(network={'sf': {'la':['a88', 100], 'ny':['a5',400]}, 'la': {'sf':['a89', 100], 'dc':['a6', 500]}})
flight_sys = FlightReservationSystem()
print(flight_sys.canDirectBook('sf', 'la', flight_network))
print(flight_sys.canConnectBook('sf', 'dc', flight_network))
print(flight_sys.fewestConnect('sf', 'dc', flight_network))


