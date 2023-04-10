import pickle
    
def add_seat(flight_number, seat, seat_type):
    with open('database/flights.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print('Flight record does not exist.')
        else:
            for item in data:
                if flight_number == item['flight']:
                    with open('database/seats.dat', 'rb') as f:
                        try:
                            data = pickle.load(f)
                        except EOFError:
                            data = dict()    
                            
                    if flight_number in data:
                        data[flight_number]['seats'].append({
                            'name': seat,
                            'reserved': 0,
                            'type': seat_type
                        })
                    else:
                        data.update({
                            flight_number: {
                                'seats': [{
                                    'name': seat,
                                    'reserved': 0, 
                                    'type': seat_type
                                }]
                            }
                        })
                        
                    with open('database/seats.dat', 'wb') as f:
                        data = pickle.dump(data, f)
                        
                    break


          