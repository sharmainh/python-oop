class ParkingGarage:
      current_ticket = {"paid": "False"}
      parking_amt = 20
      tickets = [20]
      parking_spaces = [20]
    
      # display an input that waits for an amount from the user 
      # store it in a variable
      # if the payment variable is not empty then 
      # (meaning the ticket has been paid) -> 
      # display a message to the user that their ticket has been paid and they
      # have 15mins to leave
      # This should update the "currentTicket" dictionary key "paid" to True

      def pay_for_parking():
        global customer_amt
        print( f'\nThe parking fee is ${ParkingGarage.parking_amt}')
        customer_amt = int(input("Deposit amount: $"))
        if customer_amt >= ParkingGarage.parking_amt:
          print("\nYour ticket has been paid!")
          print("You have 15 minutes to exit.")
          ParkingGarage.current_ticket['paid'] = "True"
      

      def take_ticket():
         
      # decrease the amount of tickets available by 1
         for i in ParkingGarage.tickets:
          ParkingGarage.tickets.remove(i)
          i -= 1
          ParkingGarage.tickets.append(i)
      # decrease the amount of parkingSpaces available by 1
         for i in ParkingGarage.parking_spaces:
            ParkingGarage.parking_spaces.remove(i)
            i -= 1
            ParkingGarage.parking_spaces.append(i)
      # test to see output
         print("___________________________")
         print(f"Parking Spaces Available: {ParkingGarage.parking_spaces}")
         print(f"Ticket Amount: {ParkingGarage.tickets}")

    # if ticket is paid, display a message of "Thank You, have a nice day"
    # if ticket is not paid, display an input prompt for payment
    # once paid, display message "Thank you, have a nice day!"
    # update parkingSpaces list to increase by 1 (add to the parkingSpaces list)
    # update tickets list to increase by 1 (add to the tickets list)
           
      def leave_garage():
          if ParkingGarage.current_ticket['paid'] == "True":
              print("Thank You. Have a nice day!")
          else: 
              total = ParkingGarage.parking_amt - customer_amt
              print("___________________________")
              remaining_balance = int(input(f"Please deposit the \
remaining balance of ${total}: "))
              if remaining_balance >= total:
                ParkingGarage.current_ticket['paid'] = "True"
                print("Thank you have a nice day!")
                for i in ParkingGarage.parking_spaces:
                    ParkingGarage.parking_spaces.remove(i)
                    i += 1
                    ParkingGarage.parking_spaces.append(i)
                for i in ParkingGarage.tickets:
                    ParkingGarage.tickets.remove(i)
                    i += 1
                    ParkingGarage.tickets.append(i)
          print("___________________________")
          print(f"Parking Spaces Available: {ParkingGarage.parking_spaces}")
          print(f"Ticket Amount: {ParkingGarage.tickets}")


   
      
ParkingGarage.pay_for_parking();
ParkingGarage.take_ticket();
ParkingGarage.leave_garage();
