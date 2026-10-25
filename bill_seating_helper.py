def total_calc(total_cost,tip_percent):
    total=total_cost*(1+0.01*tip_percent)
    new_total=round(total,2)
    print("your total with tip is",new_total)

total_calc(150,20)

def seating_arrangement(guests):
    '''This is a recursive function to find the number of seating arrangements for guests.'''
    if guests==0 or guests == 1:
        return 1
    else:
        return guests*seating_arrangement(guests-1)

print(seating_arrangement.__doc__)

print("The number of seating arrangements for 1 guests is",seating_arrangement(1))
print("The number of seating arrangements for 2 guests is",seating_arrangement(2))
print("The number of seating arrangements for 3 guests is",seating_arrangement(3))
print("The number of seating arrangements for 5 guests is",seating_arrangement(5))
