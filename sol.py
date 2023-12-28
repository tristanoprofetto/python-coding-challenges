from queue import Queue
import random

# Constants
OPEN_TIME = 9 * 60  # 9:00 AM in minutes
CLOSE_TIME = 17 * 60  # 5:00 PM in minutes
CUT_TIME = 30  # Haircut duration in minutes
ARRIVAL_INTERVAL = 10  # Average arrival interval in minutes
STYLISTS = ['Anne', 'Ben', 'Carol', 'Derek']

# Initialize variables
current_time = OPEN_TIME
customer_count = 0
events = []
next_arrival_time = current_time + random.randint(0, ARRIVAL_INTERVAL)

# Stylists and customers data structure
stylists = {stylist: None for stylist in STYLISTS}  # Tracks which customer each stylist is working on
waiting_customers = Queue()

# Simulation loop
while current_time < CLOSE_TIME or not waiting_customers.empty() or any(stylists.values()):
    # Handle customer arrivals
    if current_time >= next_arrival_time and current_time < CLOSE_TIME:
        customer_count += 1
        customer_name = f"Customer-{customer_count}"
        events.append(f"[{current_time // 60:02d}:{current_time % 60:02d}] {customer_name} enters the salon")
        waiting_customers.put((customer_name, current_time))
        next_arrival_time = current_time + random.randint(0, ARRIVAL_INTERVAL)

    # Assign customers to free stylists
    for stylist in stylists:
        if stylists[stylist] is None and not waiting_customers.empty():
            customer_name, arrival_time = waiting_customers.get()
            stylists[stylist] = (customer_name, current_time + CUT_TIME)
            events.append(f"[{current_time // 60:02d}:{current_time % 60:02d}] {stylist} starts cutting {customer_name}'s hair")

    # Update stylists' status
    for stylist in stylists:
        if stylists[stylist] is not None and stylists[stylist][1] == current_time:
            customer_name, _ = stylists[stylist]
            stylists[stylist] = None
            events.append(f"[{current_time // 60:02d}:{current_time % 60:02d}] {stylist} finishes cutting {customer_name}'s hair")

    # Increment time
    current_time += 1

# Handle customers left after closing
while not waiting_customers.empty():
    customer_name, _ = waiting_customers.get()
    events.append(f"[17:00] {customer_name} is kicked out and leaves furious")

# Output the events
for event in events:
    print(event)
