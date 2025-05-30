'''
Requirements:
1. Search for flights based on source, destination and departure date
2. Booking management
    - Book Flight
    - Cancellation    
    - Seat selection
3. Passenger details

'''

Core entities:

1. Flight
2. Booking
3. Passenger
4. Seat, PassengerSeat
5. User
6. FlightStatus (Enum)
7. BookingStatus (Enum)

Design:

enums/
class FlightStatus(Enum):
    SCHEDULED='SCHEDULED'
    CANCELLED='CANCELLED'
    DELAYED='DELAYED'
    
class BookingStatus(Enum):
    CONFIRMED='CONFIRMED'
    PENDING='PENDING'
    CANCELLED='CANCELLED'
    
class SeatStatus(Enum):
    RESERVED='RESERVED'
    AVAILABLE='AVAILABLE'
    CONFIRMED='CONFIRMED'
    
models/    
class Seat:
    def __init__(self, seat_no: str, seat_name: str, seat_status='AVAILABLE'):
        self.seat_no = seat_no
        self.seat_name = seat_name
        self.status = seat_status
       
    def update_status(self, status):
        self.status = status     

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

from threading import Lock
class Flight:
    def __init__(self, flight_number: str, source: str, destination: str, departure_time: datetime, arrival_time: datetime, seats: List[Seat]):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

        self.seats = defaultdict() # seat_no -> Seat
        for seat in seats:
            self.seats[seat.seat_no] = seat

        self.seat_locks = defaultdict(Lock)

        self.reservation_timeout = timedelta(minutes=15)
        self.seat_reservations = dict() # seat_no -> (user_id, timestamp)
    
    def update_status(self, status):
        self.status = status

    def __release_expired_reservations(self, seat: Seat):                
        _, start_time = self.seat_reservations[seat.seat_no]
        if datetime.now() - start_time > self.reservation_timeout:
            del self.seat_reservations[seat.seat_no]
            seat.update_status(SeatStatus.AVAILABLE)
        
    def reserve_seat(self, user: User, seat: Seat):
        with self.seat_locks[seat.seat_no]:
            if seat.seat_no not in self.seats:
                raise Exception("Invalid seat")
            
            if seat.status == SeatStatus.CONFIRMED:
                print("Seat not available")
                return False
            
            if seat.status == SeatStatus.RESERVED:
                self.__release_expired_reservations(seat)

            if seat.status == SeatStatus.AVAILABLE:
                seat.update_status(SeatStatus.RESERVED)
                self.seat_reservations[seat.seat_no] = ( user.user_id, datetime.now() )
                return True
            
            return False
        
    def confirm_seat(self, user: User, seat: Seat):
        with self.seat_locks[seat.seat_no]:
            self.__release_expired_reservations(seat)
            user_id, _ = self.seat_reservations[seat.seat_no]
            if user_id == user.user_id:
                seat.update_status(SeatStatus.CONFIRMED)
                del self.seat_reservations[seat.seat_no]
                return True
            return False


class Passenger:
    def __init__(self, name: str, dob: datetime):
        self.name = name
        self.dob = dob

class PassengerSeat:
    def __init__(self, passenger, seat=None):
        self.passenger = passenger
        self.seat = None

    def update_seat(self):
        pass

class User:
    user_id

import uuid
class Booking:
    def __init__(self, user: User, flight: Flight, status=BookingStatus.PENDING):
        self.id = uuid.uuid4()
        self.user = user
        self.flight = flight
        self.passengers = []
        self.status = status
        self.amount = None
        
    def update_status(self, status):
        self.status = status
        
    def add_passenger_seat(self, seat: PassengerSeat):
        self.seats.append(seat)

    def update_amount(self, amount):
        self.amount = amount
        
services/        
from datetime import datetime, timedelta
class FlightSearch:
    def __init__(self, flights: List[Flight]):
        self.flights = flights
        
    def search(self, source: str, destination: str, departure_time: datetime):
        
        flights = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination and departure_time.date() == flight.departure_time.date():
                flights.append(flight)
        return flights

from collections import defaultdict
class BookingService:
    
    def __init__(self):
        self.bookings = defaultdict() # booking_id -> Booking
        
    def reserve_seat(self, flight, seat):
        return flight.reserve_seat(seat)
        
    def create_booking(self, flight: Flight):
        booking = Booking(
            flight
        )
        
        self.bookings[booking.id] = booking
        return booking.id
        
    def select_seat(self, booking_id: str, seat: Seat, passenger: Passenger):
        booking = self.bookings[booking_id]
        if self.reserve_seat(booking.flight, seat):
            passenger_seat = PassengerSeat(
                passenger,
                seat
            )

            booking.add_passenger_seat(passenger_seat)
        else:
            raise Exception("Error selecting seat")
            
    def confirm_booking(self, user: User, booking: Booking):
        if booking.status == BookingStatus.CANCELLED:
            raise Exception("Cannot confirm a cancelled booking")
        
        confirmed_seats = 0
        for passenger_seat in booking.passengers:
            if booking.flight.confirm_seat(user, passenger_seat.seat):
                confirmed_seats += 1
            else:
                break

        if confirmed_seats == len(booking.passengers):
            booking.update_status(BookingStatus.CONFIRMED)
        else:
            for passenger_seat in booking.passengers:
                passenger_seat.seat.update_status(SeatStatus.RESERVED)
            raise Exception("Failed to confirm booking")

    def cancel_booking(self, booking: Booking):
        if booking.status == BookingStatus.CANCELLED:
            raise Exception("Cannot cancel already canclled booking")
        booking.update_status(BookingStatus.CANCELLED)