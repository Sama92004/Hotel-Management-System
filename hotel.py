# ===============================================================================================================
#                               Central Manager Class (HotelSystem)
# ===============================================================================================================
from rooms import Room



class HotelSystem:
    def __init__(self):
        self.employees = []
        self.guests = []
        self.rooms = []
        self.reservations = []
        self.payments = []

    def addGuest(self, guest):
        self.guests.append(guest)
        print(f"Guest {guest.get_name()} added successfully.")

    def addRoom(self, room):
        self.rooms.append(room)
        print(f"Room {room.get_room_number()} added successfully.")

    def addEmployee(self, emp):
        self.employees.append(emp)
        print(f"Employee {emp.get_name()} added successfully.")

    def displayAvailableRooms(self):
        print('\n----  Available Rooms   ----')
        found = False 
        # check if room in list or rooms or not
        for room in self.rooms:
            if room.is_available():
                print(room)
                found = True
        if not found:
            print("No available rooms Now.")

    def createReservation(self, res):
        # check if room available or not
        if res.room.is_available():
            res.room.mark_as_booked()  # change status of room to book
            self.reservations.append(res)
            res.guest.add_reservation(res)  # added reservation to guest
            print(f"Reservation created successfully for Guest: {res.guest.get_name()}.")
        else:
            print(f"Room {res.room.get_room_number()} isn't available.\n You can book from these : ")
            self.displayAvailableRooms()

    def cancelReservation(self, res):
        if res in self.reservations:
            self.reservations.remove(res)
            res.room.mark_as_available()  # return room available 
            res.guest.remove_reservation(res)  
            print("Reservation cancelled successfully.")
        else:
            print('Reservation not found.')

    def searchGuest(self, guestName):
        for guest in self.guests:
            if guest.get_name() == guestName:
                print(f'Guest found: {guest.get_name()} (ID: {guest.get_id()})')
                return guest
        print(f'Guest: {guestName} not found.')
        return None

    def addPayment(self, payment):
        self.payments.append(payment)
        print("Payment recorded successfully.")

    def displayReservations(self):
        print("\n----  All Reservations  ----")
        if not self.reservations:
            print("No reservations in the system.")
        for res in self.reservations:
           res.display_info()
           print("-"*40)

