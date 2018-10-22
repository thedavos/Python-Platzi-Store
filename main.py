# -*- coding: utf-8 -*-
import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'job': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'job': 'Data engineer',
    }
]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print("Client already is in the client's list")


def list_clients():
    global clients

    if len(clients) > 0:
        for idx, client in enumerate(clients):
            print('{uid} | {name} | {company} | {email} | {job}'.format(
                uid = idx,
                name = client['name'],
                company = client['company'],
                email = client['email'],
                job = client['job'],
            ))
    else:
        print('Client list is empty')


def update_client(updated_client_fields, index):
    global clients

    if index is not None:
        clients[index].update(updated_client_fields)
    else:
        _message_to(client_name, False)


def delete_client(index):
    global clients
    client = clients[index]

    if index is not None:    
        clients.remove(client)
        print('Client deleted')
    else:
        _message_to(client_name, False)


def search_client(client_name):
    global clients

    for client in clients:
        if client == client_name:
            return True


def _message_to(client_name, status):
    if status is True:
        print("The client: {} is in the client's list".format(client_name))
    else:
        print("the client: {} is not in our client's list".format(client_name))


def _print_welcome():
    print('WELCOME TO PLATZI SALES')
    print('*' * 100)
    print('What would you like to do today')
    print('[C]reate Client')
    print('[L]ist Client')
    print('[U]pdate Client')
    print('[D]elete Client')
    print('[S]earch Client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?: '.format(field_name))

    return field

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name?: ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _set_update_fields():
    updates = False
    updated_client_fields = {}

    while not updates:
        field = input('What field do you want to update?: ').lower()
        
        if field == 'exit':
            updates = True
            continue
        
        field_value = input('What is the new {}?: '.format(field)).capitalize()

        updated_client_fields.setdefault(field, field_value)

    return updated_client_fields


def _get_index(client_name):
    global clients

    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            return idx


if __name__ == '__main__':
    _print_welcome()

    command = input().upper()


    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'job': _get_client_field('job'),
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = input('Who do you want to update?: ')
        updated_client_fields = _set_update_fields()
        index = _get_index(client_name)
        update_client(updated_client_fields, index)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        index = _get_index(client_name)
        delete_client(index)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            _message_to(client_name, True)
        else:
            _message_to(client_name, False)
    else:
        print('Invalid command')
