from ticketbooking import movie_ticket

class Main:
    def execute(self,choice):
        if choice == 1:
            print("************************Show Seats*******************************")
            movie_ticket_obj.show_seat()
        if choice == 2:
            print("************************Buy Ticket*******************************")
            movie_ticket_obj.buy_ticket()
        if choice == 3:
            print("************************Statistics*******************************")
            movie_ticket_obj.statistics()
        if choice == 4:
            print("************************Booked User Details*****************************")
            movie_ticket_obj.user_info()
        if choice == 0:
            print("************************Thanks for connectiong! Have a Good Day! Visit us again :)***************************")
            exit()

if __name__ == "__main__":
    rows = int(input("Enter the row number you want to be seated ==> "))
    columns = int(input("Enter the column number you want to be seated ==> "))

    movie_ticket_obj = movie_ticket(rows,columns)
    obj = Main()

    while True:
        choice = int(input("Enter \n1. Show Seats \n2. Buy Ticket \n3.Statistics \n4.Booked User Details \n0. Exit \n"))
        obj.execute(choice)