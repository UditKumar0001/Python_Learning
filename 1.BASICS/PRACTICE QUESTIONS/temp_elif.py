temp = float(input("Enter temperature in degree celcius: "))

if temp <= 0:
    print("Freezing Cold")

elif temp > 0 and temp <= 10:
    print("Very Cold")

elif temp > 10 and temp <= 20:
    print("Cold")

elif temp > 20 and temp <= 30:
    print("Pleasant")

elif temp > 30 and temp <= 40:
    print("Hot")

else:
    print("Very Hot")