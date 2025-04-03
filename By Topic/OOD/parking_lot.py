from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import Dict, List, Optional

class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    BUS = 3
    TRUCK = 4

class ParkingSpotType(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    REGULAR = 3
    LARGE = 4
    HANDICAPPED = 5


class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.parking_ticket = None

    def assign_ticket(self, ticket):
        self.parking_ticket = ticket

    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type


class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)


class Bus(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.BUS)


class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.TRUCK)


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: ParkingSpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_free = True
        self.vehicle = None

    def is_available(self) -> bool:
        return self.is_free

    def park(self, vehicle: Vehicle) -> bool:
        if self.is_free:
            self.vehicle = vehicle
            self.is_free = False
            return True
        return False

    def remove_vehicle(self) -> Vehicle:
        if not self.is_free:
            vehicle = self.vehicle
            self.vehicle = None
            self.is_free = True
            return vehicle
        return None

    def get_spot_type(self) -> ParkingSpotType:
        return self.spot_type


class ParkingTicket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: ParkingSpot, entry_time: datetime):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = entry_time
        self.exit_time = None
        self.amount = 0

    def update_exit_time(self, exit_time: datetime):
        self.exit_time = exit_time

    def calculate_fee(self, hourly_rate: float) -> float:
        if self.exit_time:
            duration_in_hours = (self.exit_time - self.entry_time).total_seconds() / 3600
            self.amount = duration_in_hours * hourly_rate
            return self.amount
        return 0


class ParkingRate:
    def __init__(self):
        self.rates = {}
        
    def set_rate(self, vehicle_type: VehicleType, hourly_rate: float):
        self.rates[vehicle_type] = hourly_rate
        
    def get_rate(self, vehicle_type: VehicleType) -> float:
        return self.rates.get(vehicle_type, 0)


class ParkingFloor:
    def __init__(self, floor_id: str):
        self.floor_id = floor_id
        self.parking_spots: Dict[ParkingSpotType, List[ParkingSpot]] = {
            spot_type: [] for spot_type in ParkingSpotType
        }
        self.display_board = DisplayBoard()

    def add_parking_spot(self, spot: ParkingSpot):
        self.parking_spots[spot.get_spot_type()].append(spot)
        self.display_board.update_display(spot.get_spot_type(), len(self.get_available_spots(spot.get_spot_type())))

    def get_available_spots(self, spot_type: ParkingSpotType) -> List[ParkingSpot]:
        return [spot for spot in self.parking_spots[spot_type] if spot.is_available()]

    def find_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        vehicle_type = vehicle.get_vehicle_type()
        
        # Map vehicle types to compatible parking spot types
        compatible_spots = {
            VehicleType.MOTORCYCLE: [ParkingSpotType.MOTORCYCLE, ParkingSpotType.COMPACT, ParkingSpotType.REGULAR, ParkingSpotType.LARGE],
            VehicleType.CAR: [ParkingSpotType.COMPACT, ParkingSpotType.REGULAR, ParkingSpotType.LARGE],
            VehicleType.BUS: [ParkingSpotType.LARGE],
            VehicleType.TRUCK: [ParkingSpotType.LARGE]
        }
        
        for spot_type in compatible_spots[vehicle_type]:
            available_spots = self.get_available_spots(spot_type)
            if available_spots:
                self.display_board.update_display(spot_type, len(available_spots) - 1)
                return available_spots[0]
                
        return None
        
    def free_spot(self, spot: ParkingSpot):
        spot_type = spot.get_spot_type()
        spot.remove_vehicle()
        self.display_board.update_display(spot_type, len(self.get_available_spots(spot_type)))


class DisplayBoard:
    def __init__(self):
        self.available_spots: Dict[ParkingSpotType, int] = {
            spot_type: 0 for spot_type in ParkingSpotType
        }

    def update_display(self, spot_type: ParkingSpotType, count: int):
        self.available_spots[spot_type] = count

    def show_display(self):
        for spot_type, count in self.available_spots.items():
            print(f"{spot_type.name}: {count} spots available")


class ParkingLot:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ParkingLot, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, name: str, address: str, max_floors: int = 5):
        if not hasattr(self, "initialized"):  # Avoid re-initialization of singleton
            self.name = name
            self.address = address
            self.floors: List[ParkingFloor] = []
            self.entrance_gate = EntranceGate("entrance")
            self.exit_gate = ExitGate("exit")
            self.parking_rate = ParkingRate()
            self.ticket_counter = 1  # For generating ticket IDs
            self.initialized = True
            
            # Set default rates
            self.parking_rate.set_rate(VehicleType.MOTORCYCLE, 1.0)
            self.parking_rate.set_rate(VehicleType.CAR, 2.0)
            self.parking_rate.set_rate(VehicleType.BUS, 5.0)
            self.parking_rate.set_rate(VehicleType.TRUCK, 5.0)
            
            # Initialize floors
            for i in range(max_floors):
                self.add_floor(ParkingFloor(f"Floor-{i+1}"))

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)
        
    def add_parking_spots_to_floor(self, floor_idx: int, spot_type: ParkingSpotType, count: int):
        if 0 <= floor_idx < len(self.floors):
            floor = self.floors[floor_idx]
            start_idx = len(floor.parking_spots[spot_type])
            for i in range(start_idx, start_idx + count):
                spot = ParkingSpot(f"{floor.floor_id}-{spot_type.name}-{i+1}", spot_type)
                floor.add_parking_spot(spot)
            
    def get_new_ticket_id(self) -> str:
        ticket_id = f"T-{self.ticket_counter}"
        self.ticket_counter += 1
        return ticket_id
    
    def get_entrance_gate(self):
        return self.entrance_gate
    
    def get_exit_gate(self):
        return self.exit_gate
    
    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for floor in self.floors:
            spot = floor.find_spot(vehicle)
            if spot:
                return spot
        return None

    def get_parking_rate(self, vehicle_type: VehicleType) -> float:
        return self.parking_rate.get_rate(vehicle_type)


class Gate(ABC):
    def __init__(self, gate_id: str):
        self.gate_id = gate_id
        self.parking_lot = None
    
    def set_parking_lot(self, parking_lot: ParkingLot):
        self.parking_lot = parking_lot
    
    @abstractmethod
    def process_vehicle(self, vehicle: Vehicle):
        pass


class EntranceGate(Gate):
    def process_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        if not self.parking_lot:
            raise Exception("Entrance gate not connected to parking lot")
            
        # Find available spot
        spot = self.parking_lot.find_available_spot(vehicle)
        if not spot:
            print(f"No available spot for {vehicle.vehicle_type.name} with license plate {vehicle.license_plate}")
            return None
            
        # Park vehicle
        if spot.park(vehicle):
            # Create ticket
            ticket_id = self.parking_lot.get_new_ticket_id()
            ticket = ParkingTicket(ticket_id, vehicle, spot, datetime.now())
            vehicle.assign_ticket(ticket)
            print(f"Vehicle {vehicle.license_plate} parked at spot {spot.spot_id}")
            return ticket
        
        return None


class ExitGate(Gate):
    def process_vehicle(self, ticket: ParkingTicket) -> float:
        if not self.parking_lot:
            raise Exception("Exit gate not connected to parking lot")
            
        # Update exit time
        ticket.update_exit_time(datetime.now())
        
        # Calculate fee
        hourly_rate = self.parking_lot.get_parking_rate(ticket.vehicle.vehicle_type)
        fee = ticket.calculate_fee(hourly_rate)
        
        # Remove vehicle from spot
        for floor in self.parking_lot.floors:
            if ticket.spot in floor.parking_spots[ticket.spot.spot_type]:
                floor.free_spot(ticket.spot)
                break
        
        print(f"Vehicle {ticket.vehicle.license_plate} exited. Fee charged: ${fee:.2f}")
        return fee


class ParkingSystem:
    def __init__(self, name: str, address: str):
        self.parking_lot = ParkingLot(name, address)
        self.configure_default_layout()
        
        # Connect gates to parking lot
        entrance_gate = self.parking_lot.get_entrance_gate()
        exit_gate = self.parking_lot.get_exit_gate()
        
        entrance_gate.set_parking_lot(self.parking_lot)
        exit_gate.set_parking_lot(self.parking_lot)
    
    def configure_default_layout(self):
        # Floor 0: Mostly motorcycle and compact spots
        self.parking_lot.add_parking_spots_to_floor(0, ParkingSpotType.MOTORCYCLE, 20)
        self.parking_lot.add_parking_spots_to_floor(0, ParkingSpotType.COMPACT, 30)
        self.parking_lot.add_parking_spots_to_floor(0, ParkingSpotType.REGULAR, 10)
        self.parking_lot.add_parking_spots_to_floor(0, ParkingSpotType.HANDICAPPED, 5)
        
        # Floor 1: Regular and compact spots
        self.parking_lot.add_parking_spots_to_floor(1, ParkingSpotType.REGULAR, 50)
        self.parking_lot.add_parking_spots_to_floor(1, ParkingSpotType.COMPACT, 20)
        self.parking_lot.add_parking_spots_to_floor(1, ParkingSpotType.HANDICAPPED, 5)
        
        # Floor 2: Regular spots and some large spots
        self.parking_lot.add_parking_spots_to_floor(2, ParkingSpotType.REGULAR, 40)
        self.parking_lot.add_parking_spots_to_floor(2, ParkingSpotType.LARGE, 10)
        
        # Floor 3 and 4: Mostly large spots for buses and trucks
        self.parking_lot.add_parking_spots_to_floor(3, ParkingSpotType.LARGE, 30)
        self.parking_lot.add_parking_spots_to_floor(4, ParkingSpotType.LARGE, 30)
    
    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        entrance_gate = self.parking_lot.get_entrance_gate()
        return entrance_gate.process_vehicle(vehicle)
    
    def exit_vehicle(self, ticket: ParkingTicket) -> float:
        exit_gate = self.parking_lot.get_exit_gate()
        return exit_gate.process_vehicle(ticket)
    
    def display_available_spots(self):
        print(f"\nAvailable spots at {self.parking_lot.name}:")
        for i, floor in enumerate(self.parking_lot.floors):
            print(f"\nFloor {i+1}:")
            floor.display_board.show_display()


# Example usage
if __name__ == "__main__":
    # Initialize parking system
    parking_system = ParkingSystem("Downtown Parking", "123 Main St")
    
    # Create vehicles
    car1 = Car("CAR-1234")
    car2 = Car("CAR-5678")
    motorcycle1 = Motorcycle("MOTO-1234")
    bus1 = Bus("BUS-1234")
    
    # Park vehicles
    print("\nParking vehicles:")
    car1_ticket = parking_system.park_vehicle(car1)
    car2_ticket = parking_system.park_vehicle(car2)
    motorcycle1_ticket = parking_system.park_vehicle(motorcycle1)
    bus1_ticket = parking_system.park_vehicle(bus1)
    
    # Display available spots
    parking_system.display_available_spots()
    
    # Exit vehicles
    print("\nExiting vehicles:")
    parking_system.exit_vehicle(car1_ticket)
    parking_system.exit_vehicle(motorcycle1_ticket)
    
    # Display available spots after exits
    parking_system.display_available_spots()