def day_of_week(day: int):
    if( day == 0 ):
        print("It's Monday")
    elif( day == 2 ):
        print("It's Tuesday")
    elif( day == 3 ):
        print("It's Wednesday")
    elif( day == 4 ):
        print("It's Thursday")
    elif( day == 5 ):
        print("It's Friday")
    elif( day == 6 ):
        print("It's Saturday")
    elif( day == 7 ):
        print("It's Sunday")

day_of = int(input("Enter an integer for the day of the week"))
day_of_week(day_of)
