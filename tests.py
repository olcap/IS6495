import rooms as rdb
import room_inventory as ri_inv
import bookings as bookings

r = rdb.Rooms()
ri = ri_inv.RoomInventory()
b = bookings.Bookings()

#r.reset_database()
#ri.reset_database()
#b.reset_database()

from hotel_ui import *

main_menu()
