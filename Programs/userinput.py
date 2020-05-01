def weather_check(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter Temperature:-"))
print(type(user_input), weather_check(user_input)) 