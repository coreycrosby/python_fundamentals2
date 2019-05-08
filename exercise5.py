print("Give me a temperature in Farenheit")
f = input()

def temp_in_farenheit(f):
    celsius = (int(f) - 32) * (5/9)
    return "Temperatue in Celsius is {} C".format(round(celsius))

print(temp_in_farenheit(f))
