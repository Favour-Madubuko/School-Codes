Amount = int(input('How much do you have?\n '))

Amount_of_one_Nintendo = 250

def Amount_Needed():
    if Amount >= Amount_of_one_Nintendo:
        Number_to_purchase = Amount//Amount_of_one_Nintendo 
        Amount_rem = Number_to_purchase * Amount_of_one_Nintendo
        print(f"You can purchase {Number_to_purchase} Nintendo(s)")
        if Amount > Amount_rem:
            All = Amount - Amount_rem
            Every = All // Amount_of_one_Nintendos
        print(f"You have ${All} left and you can purchase {Every} Nintendos")

    elif Amount < Amount_of_one_Nintendo:
        Total = Amount_of_one_Nintendo - Amount
        print(f"You will need ${Total} to afford the Nintendo")       
Amount_Needed()