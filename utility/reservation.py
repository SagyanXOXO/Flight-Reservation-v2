import pandas as pd
import pickle
import uuid

def list_reservation():
    with open('database/reservations.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print('Reservation record not found.')
        else:
            if len(data) == 0:
                print('Data not found.')
            else:
                print(pd.DataFrame(data))
        
def detail_reservation(id):
    with open('database/reservations.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print('Reservation record not found.')
        else:
            if id in data:
                for key, value in data[id].items():
                    print(f'{key} : {value}')
                    
def search_reservation(customer):
    result = dict()
    with open('database/reservations.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = dict()
    for k, v in data.items():
        if v['customer'] == customer:
            result.update({
                k: v
            })
            
    print(pd.DataFrame(result))
        
def create_reservation(flight, customer, seat_number, arrival_date):
    with open('database/reservations.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = dict()
            
    data.update({
        str(uuid.uuid4()): {
            'flight': flight,
            'customer': customer,
            'seat_number': seat_number,
            'arrival_date': arrival_date
        }
    })

    with open('database/reservations.dat', 'wb') as f:
        pickle.dump(data, f)
        
def update_reservation(id, flight_number, customer_name, seat_number, arrival_date):
    with open('database/reservations.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = dict()
            
    if id in data:
        data[id]['flight'] = flight_number
        data[id]['customer_name'] = customer_name
        data[id]['seat_number'] = seat_number
        data[id]['arrival_date'] = arrival_date

        with open('database/reservations.dat', 'wb') as f:
            pickle.dump(data, f)   
    else:
        print('No reservation found with the provided ID.')  
                
def delete_reservation(id):
    with open('database/reservations.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = dict()
            
    if id in data:
        del data[id]
    else:
        print('No reservation found with the provided ID.')

    with open('database/reservations.dat', 'wb') as f:
        pickle.dump(data, f)
