def speeding_ticket(speed, is_birthday):
    # Your code goes here
    # Implement the logic based on the driver's speed and birthday condition
    if is_birthday==True:
        if speed<=65:
            print("No Ticket")
        elif speed>65 and speed<=85:
            print("Small Ticket")
        else:
            print("Big Ticket")
    else:
        if speed<=60:
            print("No Ticket")
        elif speed>60 and speed<=80:
            print("Small Ticket")
        else:
            print("Big Ticket")
        


# Test cases
speeding_ticket(60, False)  # Expected output: "No Ticket"
speeding_ticket(75, False)  # Expected output: "Small Ticket"
speeding_ticket(85, False)  # Expected output: "Big Ticket"
speeding_ticket(65, True)  # Expected output: "No Ticket"
speeding_ticket(85, True)  # Expected output: "Small Ticket"
