#v1.0, add user input, store data, and output response
print("=== Weather App v1.2 ===")

city = input("Enter a city: ").strip()

if city == "":
    print("You must enter a city")
else:
    print("\n--- Weather Report ---")
    print(f"fetching weather for: {city}")
    print("Temprature: 72°F")
    print("Condition: Partly cloudy")
    print("------------------------------")