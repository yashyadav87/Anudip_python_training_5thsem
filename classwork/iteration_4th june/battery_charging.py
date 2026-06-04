#program for display battery charging level
charging_level = 20
electricity_status = True
while(charging_level <= 100 ):
    if(charging_level):
        print("Battery charging level:", charging_level, "%")   
        charging_level += 10
    else:
        break
    #----------------------------------------------------
print("full charge")
