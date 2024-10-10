from collections import deque

# Stack for undoing trip bookings
undo_stack = []

# Queue for scheduling trips
trip_queue = deque()

# List to track destinations
destinations = []

# Function to book a trip
def book_trip(destination):
    destinations.append(destination)
    undo_stack.append(('book', destination))
    print(f"Trip to {destination} booked.")

# Function to undo the last trip booking
def undo_trip():
    if undo_stack:
        action, destination = undo_stack.pop()
        if action == 'book':
            destinations.remove(destination)
            print(f"Undo booking: Trip to {destination} has been removed.")
    else:
        print("No booking to undo.")

# Function to add a destination to the waiting queue
def add_to_queue(destination):
    trip_queue.append(destination)
    print(f"{destination} added to the waiting list.")

# Function to schedule the next trip from the queue
def schedule_next_trip():
    if trip_queue:
        destination = trip_queue.popleft()
        book_trip(destination)
    else:
        print("No destinations in the queue.")

# Function to display all booked trips
def display_trips():
    if destinations:
        print("Booked trips:")
        for destination in destinations:
            print(f"- {destination}")
    else:
        print("No trips booked yet.")

# booked equeue
book_trip("kigali")
book_trip("musanze")
book_trip("rubavu")
book_trip("nyamata")
display_trips()
undo_trip()
undo_trip() # Undo nyamata and rubavu booking by stack
display_trips()
add_to_queue("huye")
add_to_queue("muhanga")
schedule_next_trip()  # Schedule huye 
display_trips()#all booked trips