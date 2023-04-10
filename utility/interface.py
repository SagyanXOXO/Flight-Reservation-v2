from utility.flight import *
from utility.seat import *
from utility.reservation import *
from utility.customer import *

class Interface:
    def run(self):
        pass
    
    def list(self):
        pass
    
    def create(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass

class FlightInterface:
    def run(self):
        print('Enter L to list all flights.')
        print('Enter C to create a flight record.')
        print('Enter U to update a flight record.')
        print('Enter D to delete a flight record.')
        print('Enter S to search a flight record.')
        print('Enter V to view detailed flight record.')
        
        choose = input('Choose a valid option: ')
        choose = choose.upper()
        
        if choose == 'L':
            self.list()
        elif choose == 'C':
            self.create()
        elif choose == 'U':
            self.update()
        elif choose == 'D':
            self.delete()
        elif choose == 'S':
            self.search()
        elif choose == 'V':
            self.detail()
        
    def list(self):
        list_flight()   
        
    def detail(self):
        flight = input('Enter flight number to view details : ')
        detail_flight(flight)   
          
    def create(self):
        flight = input('Enter flight : ')
        airline_name = input('Enter airline name : ')
        departure_location = input('Enter Departure location : ')
        arrival_location = input('Enter Arrival location : ')
        scheduled_departure = input('Enter departure time (YYYY/MM/DD) : ')
        scheduled_arrival = input('Enter arrival time (YYYY/MM/DD) : ')
        create_flight(flight, airline_name, departure_location, arrival_location, scheduled_departure, scheduled_arrival)
        
    def update(self):
        old = input('Enter a Flight number to update :')
        flight = input('Enter Flight Number : ')
        airline_name = input('Enter Airline Name : ')
        departure_location = input('Enter Departure location : ')
        arrival_location = input('Enter Arrival location : ')
        scheduled_departure = input('Enter departure time (YYYY/MM/DD) : ')
        scheduled_arrival = input('Enter arrival time (YYYY/MM/DD) : ')
        update_flight(old, flight, airline_name, departure_location, arrival_location, scheduled_departure, scheduled_arrival)
        
    def delete(self):
        old = input('Enter a Flight number to delete :')
        delete_flight(old)
        
    def search(self):
        departure_location = input('Enter departure_location : ')
        arrival_location = input('Enter arrival_location : ')
        search_flight(departure_location, arrival_location)

class ReservationInterface:
    def run(self):
        print('Enter L to list reservation records.')
        print('Enter C to create a reservation record.')
        print('Enter U to update a reservation record.')
        print('Enter D to delete a reservation record.')
        
        choose = input('Choose : ')
        choose = choose.upper()
        
        if choose == 'L':
            self.list()
        elif choose == 'C':
            self.create()
        elif choose == 'U':
            self.update()
        elif choose == 'D':
            self.delete()
        elif choose == 'S':
            self.search()
        elif choose == 'R':
            self.detail()
    
    def list(self):
        list_reservation()
        
    def create(self):
        flight = input('Enter flight number : ')
        customer_id = input('Enter customer ID : ')
        seat_number = input('Enter seat number : ')
        arrival_date = input('Enter arrival date (YYYY/MM/DD) : ')
        create_reservation(flight, customer_id, seat_number, arrival_date)
        
    def update(self):
        id = input('Enter reservation ID:')
        flight = input('Enter flight number : ')
        customer_id = input('Enter customer ID : ')
        seat_number = input('Enter seat number : ')
        arrival_date = input('Enter arrival date (YYYY/MM/DD) : ')
        update_reservation(id, flight, customer_id, seat_number, arrival_date)
        
    def delete(self):
        id = input('Enter reservation ID :')
        delete_reservation(id) 
    
    def search(self):
        customer_name = input('Enter customer name : ')
        search_reservation(customer_name)
        
    def detail(self):
        id = input('Enter reservation ID : ')
        detail_reservation(id)

class SeatInterface:
    def run(self):
        self.main()
        
    def main(self):
        print('Enter C to create a seat.')
        print('Enter E to exit.')
        
        choose = input('Choose : ')
        choose = choose.upper()
        
        if choose == 'C':
            self.create() 
          
    def create(self):
        flight = input('Enter flight : ')
        seat_name = input('Enter seat : ')
        seat_type = input('Enter seat type : ')
        add_seat(flight, seat_name, seat_type)

class CustomerInterface:
    def run(self):
        print('Enter L to list customers.')
        print('Enter C to create a customer.')
        print('Enter U to update a customer.')
        print('Enter D to delete a customer.')
        print('Enter S to search a customer.')
        print('Enter B to go back.')
        
        choose = input('Choose : ')
        choose = choose.upper()
        
        if choose == 'L':
            self.list()
        elif choose == 'C':
            self.create()
        elif choose == 'U':
            self.update()
        elif choose == 'D':
            self.delete()
        elif choose == 'S':
            self.search()
        else:
            print('Invalid choice.')

    def list(self):
        list_customer()
        
    def create(self):
        full_name = input("Enter Full Name : ")
        date_of_birth = input("Enter Date of Birth (YYYY/MM/DD) : ")
        contact_number = input("Enter Phone Number : ")
        email_address = input("Enter Email : ")
        create_customer(full_name, date_of_birth, contact_number, email_address)
        
    def update(self):
        id = input('Enter customer id : ')
        full_name = input("Enter Full Name : ")
        date_of_birth = input("Enter Date of Birth (YYYY/MM/DD) : ")
        contact_number = input("Enter Phone Number : ")
        email_address = input("Enter Email : ")
        update_customer(id, full_name, date_of_birth, contact_number, email_address)
        
    def delete(self):
        id = input('Enter customer ID : ')
        delete_customer(id)
    
    def search(self):
        id = input('Enter customer ID : ')
        search_customer(id)

class User:
    def run(self):
        self.main()  

    def main(self):
        print('Welcome to the convenient Flight Booking Service.\n')
        print('Enter S for search flights.')
        print('Enter D for flight details.')
        
        choose = input('choose : ')
        choose = choose.upper()
        
        if choose == 'S':
            self.search()
        elif choose == 'D':
            self.detail()

    def search(self):
        departure_location = input('Enter departure location = ')
        arrival_location = input('Enter arrival location = ')
        search_flight(departure_location, arrival_location)

    def detail(self):
        flight_number = input('Enter flight number : ')
        detail_flight(flight_number)


class Admin:  
    def run(self):
        self.main()
    
    def main(self):
        print('Welcome to the convenient Flight Booking Service.')
        print('Enter F for Flights.')
        print('Enter S for Seats.')
        print('Enter C for Customers.')
        print('Enter R for Reservations.')
        
        choose = input('Choose: ')
        choose = choose.upper()
        
        if choose == 'F':
            fi = FlightInterface()
            fi.run()   
        elif choose == 'S':
            si = SeatInterface()
            si.run()
        elif choose == 'C':
            ci = CustomerInterface()
            ci.run()
        elif choose == 'R':
            ri = ReservationInterface()
            ri.run()        
        else:
            print('Incorrect input. Please try again with a valid choice.')

def engine(option):
    if option == 'user':
        user = User()
        user.run()
    elif option == 'admin':
        admin = Admin()
        admin.run()
    else:
        raise Exception("Invalid user type.")
