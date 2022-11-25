def get_int():
    correctInt = False
    while correctInt == False:
        intval = (input("please enter an integer value "))
        try:
            intval = int(intval)

            print(intval)
            break
        except ValueError:
            print('The provided value is not a int')
            

def get_float():
    correctFloat = False
    while correctFloat == False:
        floatval = (input("please enter a float value "))
        try:
            floatval = float(floatval)

            print(floatval)
            break
        except ValueError:
            print('The provided value is not a float')

get_int()
get_float()