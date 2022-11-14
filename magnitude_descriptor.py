magnitude_number = float(input("Enter your predicted magnitude range in figures: "))

if magnitude_number < 2.0:
    print(f"A magnitude of {magnitude_number} is considered to be micro")
elif magnitude_number >=2.0 and magnitude_number <3.0:
    print(f"A magnitude of {magnitude_number} is considered to be very minor")
elif magnitude_number >=3.0 and magnitude_number <4.0:
    print(f"A magnitude of {magnitude_number} is considered to be minor")
elif magnitude_number >=4.0 and magnitude_number <5.0:
    print(f"A magnitude of {magnitude_number} is considered to be light")
elif magnitude_number >=5.0 and magnitude_number <6.0:
    print(f"A magnitude of {magnitude_number} is considered to be moderate")
elif magnitude_number >=6.0 and magnitude_number <7.0:
    print(f"A magnitude of {magnitude_number} is considered to be strong")
elif magnitude_number >=7.0 and magnitude_number <8.0:
    print(f"A magnitude of {magnitude_number} is considered to be major")
elif magnitude_number >=8.0 and magnitude_number <10.0:
    print(f"A magnitude of {magnitude_number} is considered to be great")
elif magnitude_number >=10.0:
    print(f"A magnitude of {magnitude_number} is considered to be meteoric")
    