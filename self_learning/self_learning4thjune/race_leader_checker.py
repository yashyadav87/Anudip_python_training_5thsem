#Wap to track race leaders based on lap times
#Input lap times of N racers
#Display fastest racer position
#Display slowest racer position
#Display difference between fastest and slowest lap time

n=int(input("Enter the number of racers: "))

#validate number of racers
if(n<=0):
    exit("Number of racers should be positive")

#---------------------------------------------------
#input lap time of first racer

lap_time=float(input("Enter lap time of racer 1: "))

#initialize fastest and slowest values

fastest_time=lap_time
slowest_time=lap_time

fastest_position=1
slowest_position=1

#---------------------------------------------------
#input lap times of remaining racers

for i in range(2,n+1):

    lap_time=float(input("Enter lap time of racer "+str(i)+": "))

    #checking fastest racer

    if(lap_time<fastest_time):
        fastest_time=lap_time
        fastest_position=i

    #checking slowest racer

    if(lap_time>slowest_time):
        slowest_time=lap_time
        slowest_position=i

#---------------------------------------------------
#calculating time difference

difference=slowest_time-fastest_time

#---------------------------------------------------
#displaying results

print("Fastest Racer Position =",fastest_position)
print("Slowest Racer Position =",slowest_position)
print("Difference Between Fastest And Slowest Lap Time =",difference)
