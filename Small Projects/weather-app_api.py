#v1.0, add user input, store data, and output response
print("=== Weather App v1.3 ===")

city = input("Enter a city: ").strip().title()
#Version 1.3
if city == "":
    print("You must enter a city")
elif city == "Louisville":
    print("\n--- Weather Report ---")
    print(f"City: {city}")
    print("Temprature: 72°F")
    print("Condition: Sunny")
    print("----------------------")
elif city == "New Albany":
    print("\n--- Weather Report ---")
    print(f"City: {city}")
    print("Temperature: 68°F")
    print("Condition: Cloudy")
    print("----------------------")
elif city == "Indianapolis":
    print("\n--- Weather Report ---")
    print(f"City: {city}")
    print("Temperature: 65°F")
    print("Condition: Rainy")
    print("----------------------")
else:
    print(f"Sorry, no weather data available yet for {city}")