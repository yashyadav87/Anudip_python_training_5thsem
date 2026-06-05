#Wap to simulate lift movement
#Lift starts from floor 0
#User enters destination floors repeatedly
#Display floors travelled in each trip
#Display total floors travelled
#Stop when user enters -1

current_floor=0
total_travelled=0

#---------------------------------------------------
#accepting destination floors

while(True):

    print("Current Floor =",current_floor)

    destination=int(input("Enter Destination: "))

    #---------------------------------------------------
    #checking termination condition

    if(destination==-1):
        break

    #---------------------------------------------------
    #calculating floors travelled in current trip

    travelled=abs(destination-current_floor)

    #---------------------------------------------------
    #displaying trip details

    print("Travelled =",travelled,"floors")

    #---------------------------------------------------
    #updating total travel and current floor

    total_travelled+=travelled
    current_floor=destination

#---------------------------------------------------
#displaying total floors travelled

print("Total Travelled =",total_travelled,"floors")
