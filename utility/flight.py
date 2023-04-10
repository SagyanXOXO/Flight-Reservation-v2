import pandas as pd
import pickle

def search_flight(departure_location, arrival_location):
    temp = []
    
    with open('database/flights.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print('Flight record does not exist.')
        else:
            for d in data:
                if (d['departure_location'] == departure_location) and (d['arrival_location'] == arrival_location):
                    temp.append(d)
                    
            if len(temp) == 0:
                print('No results.')
            else:
                print(pd.DataFrame(temp)) 

def list_flight():
    with open('database/flights.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print('Flight record does not exist.')
        else: 
            print(pd.DataFrame(data))
        
def create_flight(flight, airline_name, departure_location, arrival_location, scheduled_departure, scheduled_arrival):
    flight_exists = False
    
    with open('database/flights.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = []
            
    for d in data:
        if d['flight'] == flight:
            flight_exists = True
            
    if flight_exists:
        print('Flight record already exists.')
    else:
        data.append(
            {
                'flight': flight,
                'airline_name': airline_name,
                'departure_location': departure_location,
                'arrival_location': arrival_location,
                'scheduled_departure': scheduled_departure,
                'scheduled_arrival': scheduled_arrival
            }
        )

        with open('database/flights.dat', 'wb') as f:
            pickle.dump(data, f)
        
def update_flight(old, flight, airline_name, departure_location, arrival_location, scheduled_departure, scheduled_arrival):
    with open('database/flights.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = []
            
    for item in data:
        if old in item['flight']: 
            item['flight'] = flight
            item['airline_name'] = airline_name
            item['departure_location'] = departure_location
            item['arrival_location'] = arrival_location
            item['scheduled_departure'] = scheduled_departure
            item['scheduled_arrival'] = scheduled_arrival
        else:    
            print('Flight record not found.')

    with open('database/flights.dat', 'wb') as f:
        pickle.dump(data, f)  

def detail_flight(flight):
    with open('database/flights.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print("Flight record does not exist.")
        else:
            for item in data:
                if 'flight' in item and item['flight'] == flight:
                    print(pd.DataFrame([item]))
                    
                    print('Seats:')
                    with open('database/seats.dat', 'rb') as f:
                        try:
                            data = pickle.load(f)
                        except EOFError:
                            print("No seats allocated.")
                        else:
                            if flight in data:
                                for seat in data[flight]['seats']:
                                    for key, value in seat.items():
                                        print(f'{key} : {value}')
                    break
                
def delete_flight(flight):
    with open('database/flights.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = []
            
    for item in data:
        if flight in item['flight']: 
            del item
        else:
            print('Flight record does not exist.')

    with open('database/flights.dat', 'wb') as f:
        pickle.dump(data, f)