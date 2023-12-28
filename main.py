import collections
import random
import numpy as np

STYLISTS = {
    'alex': [],
    'james': [],
    'jessica': [],
    'jennifer': []
}

def get_customer_arrivals(lambd, total_minutes):
    customers = []
    customer_count = 0
    current = 0
    while current <= total_minutes:
        current += int(random.expovariate(lambd))
        customer_count += 1
        customers.append((customer_count+1, current))
    return customers


def get_time(hour, minute):
    if hour <= 9:
        hour = f'0{hour}'
    minute = minute % 60
    if minute <= 9:
        minute = f'0{minute}'
    return f'{hour}:{minute}'


def check_stylist_availability(stylist):
    for k, v in zip(stylists.keys(), stylists.values()):
        if v == []:
            return True
    return False

def update_stylist_availability(stylist):
    pass

def main(customers, stylists, start, end):
    """
    Runs simulation for the customer arrivals and stylist availability

    Args:
        customers (list): list of tuples containing customer name and arrival time
        stylists (dict): dictionary of stylists and their availability
        start (int): start time of the simulation [0, 24]
        end (int): end time of the simulation [0, 24]
    """
    time = (end - start) * 60
    hour, minute = start, 0
    count = 0
    while count < time:
        timestamp = get_time(hour, minute)
        while customers[0][1] == count:
            customer, entered = customers.popleft()
            q.append(customer)
            print(f'[{timestamp}] - Customer: {customer} entered')
        
        for k, v in zip(stylists.keys(), stylists.values()):
            if not stylists[k] and q:
                customer = q.popleft()
                stylists[k].append([customer, 0])
                print(f'[{timestamp}] - {k} started cutting customer {customer}s hair')
             
        for k, v in zip(stylists.keys(), stylists.values()):
            if stylists[k]:
                stylists[k][0][1] += 1
                if stylists[k][0][1] % 30 == 0:
                    customer = stylists[k].pop()
                    print(f'[{timestamp}] - {k} finished cutting customer {customer[0]}s hair')
        count += 1
        if count % 60 == 0:
            hour += 1
    
    while q:
        customer = q.popleft()
        print(f'[{timestamp}] - Customer: {customer} left furious')

if __name__ == '__main__':
    import random
    customers = collections.deque([])
    q = collections.deque([])
    total_minutes = 8 * 60
    customers = get_customer_arrivals(1/6, total_minutes)
    customers = collections.deque(customers)
    stylists = {
        'alex': [],
        'james': [],
        'jessica': [],
        'jennifer': []
    }
    main(customers, stylists, 9, 17)
