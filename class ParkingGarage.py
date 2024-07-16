class ParkingGarage:
    def __init__(self, tickets, parking_spaces):
        self.tickets = tickets  # list of available tickets
        self.parking_spaces = parking_spaces  # list of available parking spaces
        self.current_ticket = {}  # dictionary to track current ticket status

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)  # remove the first ticket from the list
            space = self.parking_spaces.pop(0)  # remove the first parking space
            self.current_ticket[ticket] = {'paid': False, 'space': space}
            print(f"Your ticket number is {ticket}. Please park in space {space}.")
        else:
            print("Sorry, the parking garage is full.")

    def payForParking(self):
        ticket = input("Enter your ticket number to pay: ")
        if ticket in self.current_ticket:
            if not self.current_ticket[ticket]['paid']:
                payment = input("Enter payment amount: ")
                if payment:
                    self.current_ticket[ticket]['paid'] = True
                    print("Payment successful. You have 15 minutes to leave.")
                else:
                    print("Payment cancelled.")
            else:
                print("Ticket already paid.")
        else:
            print("Invalid ticket number.")

    def leaveGarage(self):
        ticket = input("Enter your ticket number to leave: ")
        if ticket in self.current_ticket:
            if self.current_ticket[ticket]['paid']:
                space = self.current_ticket[ticket]['space']
                self.parking_spaces.append(space)
                self.tickets.append(ticket)
                del self.current_ticket[ticket]
                print("Thank you, have a nice day!")
            else:
                print("Payment required before leaving.")
        else:
            print("Invalid ticket number.")

    def displayStatus(self):
        print(f"\nTickets available: {self.tickets}")
        print(f"Parking spaces available: {self.parking_spaces}")
        print(f"Current tickets: {self.current_ticket}\n")


# Function to simulate the parking garage
def run_parking_garage():
    tickets = ['T1', 'T2', 'T3', 'T4', 'T5']  # Example tickets
    parking_spaces = ['P1', 'P2', 'P3', 'P4', 'P5']  # Example parking spaces
    garage = ParkingGarage(tickets, parking_spaces)

    while True:
        print("\nWelcome to the Parking Garage!")
        print("1. Take a ticket")
        print("2. Pay for parking")
        print("3. Leave the garage")
        print("4. Display garage status")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            garage.takeTicket()
        elif choice == '2':
            garage.payForParking()
        elif choice == '3':
            garage.leaveGarage()
        elif choice == '4':
            garage.displayStatus()
        elif choice == '5':
            print("Thank you for using the parking garage. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Run the parking garage simulation
if __name__ == "__main__":
    run_parking_garage()
