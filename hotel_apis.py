import rooms as rooms
import room_inventory as room_inv
import bookings as bookings

r = rooms.Rooms()
ri = room_inv.RoomInventory()
b = bookings.Bookings()

def add_rooms():
    #basically call the CRUD routine
    print("*** Add a room ***")
    room_desc = input("Enter a description of the room: ")
    room_type = input("Enter the type of room: ")
    room_price = input("Enter the price of the room: ")
    r.add(room_type,room_desc,room_price)
    list_rooms()  # should list all

def update_rooms():
    #basically call the CRUD routine
    print("*** Update a room ***")
    list_rooms()
    _id = input("Enter the room Id: ")
    #show them what the record currently is
    list_rooms(room_id=_id)
    room_desc = input("Enter a description of the room: ")
    room_type = input("Enter the type of room: ")
    room_price = input("Enter the price of the room: ")

    r.update(_id,room_type,room_desc,room_price)
    list_rooms()

def delete_rooms():
    #basically call the CRUD routine
    list_rooms()
    _id = input("Enter the room Id you wish to delete: ")
    list_rooms(room_id=_id)
    response = input("This will delete the listed room. Continue (y/n) ? ").lower()
    if response == "y":
        r.delete(_id)
        list_rooms()

def list_rooms(room_id=None, room_type=None):
    #basically call the CRUD routine fetch
    print("*** Room Listing ***")
    for item in r.fetch(room_id=None, room_type=None):
        print(item)

######################################################################################################################

def add_room_to_inventory(inv_id=None, floor=None):
    #basically call the CRUD routine
    print("*** Add an inventory ***")
    inv_id = input("Enter the inventory Id: ")
    floor = input("Enter the floor of the room: ")
    ri.add(inv_id,floor)
    list_rooms_in_inventory()  # should list all

def update_room_in_inventory():
    #basically call the CRUD routine
    print("*** Update inventory ***")
    list_rooms_in_inventory()
    _id = input("Enter the inventory Id: ")
    #show them what the record currently is
    list_rooms_in_inventory(inv_id=_id)
    inv_id = input("Enter the room Id: ")
    floor = input("Enter the floor of the rooms: ")

    ri.update(_id,inv_id,floor)
    list_rooms_in_inventory()

def delete_room_in_inventory():
    #basically call the CRUD routine
    list_rooms_in_inventory()
    _id = input("Enter the inventory Id you wish to delete: ")
    list_rooms_in_inventory(inv_id=_id)
    response = input("This will delete the listed inventory. Continue (y/n) ? ").lower()
    if response == "y":
        ri.delete(_id)
        list_rooms_in_inventory()

def list_rooms_in_inventory(inv_id=None, floor=None):
    #basically call the CRUD routine fetch
    print("*** Room Inventory ***")
    for item in ri.fetch(inv_id=None, floor=None):
        print(item)

#####################################################################################################################################

def check_room_availability(inv_id, start_date, end_date):
    existing_bookings = b.fetch(inv_id=inv_id)
    # logic to check if the room is available
    for booking in existing_bookings:
        booked_start, booked_end = booking['start_date'], booking['end_date']
        booked_start = datetime.strptime(booked_start, '%Y-%m-%d').date()
        booked_end = datetime.strptime(booked_end, '%Y-%m-%d').date()
        requested_start = datetime.strptime(start_date, '%Y-%m-%d').date()
        requested_end = datetime.strptime(end_date, '%Y-%m-%d').date()
        if (booked_start <= requested_end) and (requested_start <= booked_end):
            return False # overlap
    return True  # room is available

def book_room():
    #need to find a way to list available rooms based on date
    start_date = input("Enter the start date for booking (YYYY-MM-DD): ")
    end_date = input("Enter the end date for booking (YYYY-MM-DD): ")
    #list_rooms()
    #list_rooms_in_inventory()
    #list_bookings()
    inv_id = input("Enter the ID of the room you wish to book: ")
    if check_room_availability(inv_id, start_date, end_date):
        status = "Booked"
        b.add_booking(inv_id, start_date, end_date, status)
        print("Room booked successfully.")
    else:
        print("Sorry, the room is not available for the selected dates.")

def update_booking():
    booking_id = input("Enter the booking ID to update: ")
    current_booking = b.fetch_bookings(booking_id=booking_id)
    if current_booking is None:
        print(f"No booking found with ID: {booking_id}")
        return
    print(f"Current booking details: {current_booking}")
    new_inv_id = input("Enter the new room ID (current: {}): ".format(current_booking['inv_id']))
    new_start_date = input("Enter the new start date (YYYY-MM-DD) (current: {}): ".format(current_booking['start_date']))
    new_end_date = input("Enter the new end date (YYYY-MM-DD) (current: {}): ".format(current_booking['end_date']))
    new_status = input("Enter the new status (current: {}): ".format(current_booking['status']))
    if new_inv_id != current_booking['inv_id'] or new_start_date != current_booking['start_date'] or new_end_date != current_booking['end_date']:
        if not check_room_availability(new_inv_id, new_start_date, new_end_date):
            print("The new room is not available for the selected dates.")
            return
    updated = b.update_booking(booking_id, new_inv_id, new_start_date, new_end_date, new_status)
    if updated:
        print("Booking updated successfully.")
    else:
        print("Failed to update the booking.")

def cancel_booking():
    booking_id = input("Enter the booking ID to cancel: ")
    current_booking = b.fetch_bookings(booking_id=booking_id)
    if current_booking is None:
        print(f"No booking found with ID: {booking_id}")
        return
    print(f"Current booking details: {current_booking}")
    confirm = input("Are you sure you want to cancel this booking? (y/n): ").lower()
    if confirm != 'y':
        print("Cancellation aborted.")
        return
    cancelled = b.update_booking_status(booking_id, "Cancelled")
    if cancelled:
        print("Booking cancelled successfully.")
    else:
        print("Failed to cancel the booking.")

def list_bookings(booking_id=None, inv_id=None):
    #basically call the CRUD routine fetch
    print("*** Booking List ***")
    for item in b.fetch(booking_id=None, inv_id=None):
        print(item)
    
def list_inventory():
    pass

