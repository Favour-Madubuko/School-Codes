age = float(input('What is your age? '))
weight = float(input('What is your weight? '))

def BMI_Calc():
    x = age ** 2
    y = weight 
    z = x / y
    return z

def Height():
    z=BMI_Calc()
    right_height = z ** 2
    final_height =(right_height/4)
    total_height = round(final_height,2)
    print(total_height)
Height()
