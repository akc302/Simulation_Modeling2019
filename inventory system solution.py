import random
counter = 1

b_inventory = 3
e_inventory=0
ord_quantity = 8
#short_quantity = int(0)
short_quantity=0
b_order=0
demand=0
days=1
average_end=0
averageOfshortage=0
days_until=1
r_lead=0
sum_short_quantity=0

def daily_demand(r_demand):
  
  if r_demand in range(1,11):
    
    return 1
  if r_demand in range(11,36):
    
    return 2
  if r_demand in range(36,71):
    
    return 3
  if r_demand in range(71,92):
    
    return 4
  if r_demand in range(92,101):
    
    return 5



def lead_time(r_lead):
  if r_lead in range(1,7): 
    return 1
  if r_lead in range(7,11): 
    return 2
  if r_lead==0:
    return 3
for i in range(1,6):
        
    for j in range(1,6):
        #global short_quantity
        print("\n******\ncycle:",i,",days", days,",beginning inventory:",b_inventory)
        r_demand=random.randint(1,100)
        demand=daily_demand(r_demand)
        
        



        if b_inventory-demand>=0:
            e_inventory=b_inventory-demand
            
        else:
           
            e_inventory=0
            
            short_quantity=demand-b_inventory  
            sum_short_quantity=  sum_short_quantity+short_quantity
            averageOfshortage=averageOfshortage+1
        print('Shortage quantity:',short_quantity)      
        b_inventory=e_inventory
          

        
        if days==5:
            ord_quantity=11-e_inventory
            #updated ord quant
            print("order quantity", ord_quantity)
            r_lead=random.randint(1,10)

            print("random digit for the lead time:",r_lead)
            days_until=lead_time(r_lead)  
            print("days until order:",days_until)
            days_until=days_until-1
            days=1
        else:
            print("days until order:",days_until)
            if days_until==0:
                b_inventory=b_inventory+ord_quantity-sum_short_quantity  
                sum_short_quantity=0
                ord_quantity=0
                short_quantity=0
                days_until=days_until-1
            else:
                if days_until>0:
                    days_until=days_until-1
                else:
                    days_until=-1    
            days=days+1
            #change of update quantity
            print("order quantity:",ord_quantity)
        average_end=average_end+e_inventory  
        print("Random digit for demand:",r_demand,"Demand:",demand)  
        print("End inventory",e_inventory)
        
print("\naverage ending inventory:",average_end/25)
print("\naverage number of days when shortage occurs:",averageOfshortage/25)
          

        