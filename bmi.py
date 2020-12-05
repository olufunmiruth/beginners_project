""" The BMI is a convenient rule of thumb used to broadly categorize a person as underweight,
normal weight, overweight, or obese based on tissue mass (muscle, fat, and bone) and height.
Commonly accepted BMI ranges are underweight (under 18.5 kg/m2), normal weight (18.5 to 25),
 overweight (25 to 30), and obese (over 30)
Write a program that continually reads in mass and height from the user and then outputs
 if the user is underweight, normal weight, overweight or obese. """

while True:
    mass_in_kg = float(input('Enter mass in kilogrammes: '))  # reads mass from the user and converts to float
    height_in_metres = float(input('Enter height in metres: '))  # reads height from the user and converts to float

    # calculation for bmi
    b_m_i = mass_in_kg / (height_in_metres * height_in_metres)

    if b_m_i < 18.5:  # the bmi category is underweight if the bmi is less than 18.5
        bmi_category = 'UNDER WEIGHT'
    elif b_m_i < 25:  # the bmi category is  normal weight if the bmi is less than 25 but greater than 18.5
        bmi_category = 'NORMAL WEIGHT'
    elif b_m_i < 30:  # the bmi category is over weight if the bmi is less than 30 but greater than 25
        bmi_category = 'OVER WEIGHT'
    else:  # the bmi category is obese if the bmi is greater than 35
        bmi_category = 'OBESE'

    # displays  the mass, height,bmi and bmi category to the use
    print('Mass is ' + str(mass_in_kg) + 'kg')
    print('Height is ' + str(height_in_metres) + 'm')
    print('BMI is ' + str(b_m_i) + ' kg/m^2')
    print('BMI category is: ' + bmi_category)
    print()

    # condition to continue or exit the loop
    exit_or_continue = int(input('press 0 to exit or 1 to continue: '))
    if exit_or_continue == 0:
        break
    if exit_or_continue == 1:
        continue
