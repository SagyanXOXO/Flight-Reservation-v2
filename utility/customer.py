import pickle
import pandas as pd
            
def get_customer_id(full_name, date_of_birth):
    return '{}_{}'.format(full_name, date_of_birth.replace('/', '_'))

def list_customer():
    with open('database/customers.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print('No customer record.')
        else:     
            print(pd.DataFrame(data))

def create_customer(full_name, date_of_birth, contact_number, email_address):
    with open('database/customers.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = dict()
        finally:
            customer_id = get_customer_id(full_name, date_of_birth)
            if customer_id in data:
                print('Customer already exists.')
            else:
                payload = {
                    customer_id: {
                        'full_name': full_name,
                        'date_of_birth': date_of_birth,
                        'contact_number': contact_number,
                        'email_address': email_address
                    }   
                }
                
                data.update(payload)
        
                with open ('database/customers.dat', 'wb') as f:
                    pickle.dump(data, f)
        
def update_customer(customer_id, full_name, date_of_birth, contact_number, email_address):
    delete_customer(customer_id)
    create_customer(full_name, date_of_birth, contact_number, email_address)
        
def search_customer(customer_id):
    with open('database/customers.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print('Customer record does not exist.')
        else:
            if customer_id in data:
                result = data[customer_id]
                for k, v in result.items():
                    print(f'{k} : {v}')
            else:
                print('Customer with the given ID does not exist.')

def delete_customer(customer_id):
    with open('database/customers.dat', 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            print('Customer with this ID does not exist.')
        else:
            if customer_id in data:
                del data[customer_id]
                
                with open('database/customers.dat', 'wb') as f:
                    pickle.dump(data, f)
            else:
                print('Customer with the given ID does not exist.')        