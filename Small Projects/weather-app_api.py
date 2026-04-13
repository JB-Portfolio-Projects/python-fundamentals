#v1.0, add user input, store data, and output response
print("=== Weather App v1.0 ===")

city = input("Enter a city: ")

if city.strip() == "":
    print("You must enter a city")
else:
    print(f"fetching weather for: {city}")
    print("Weather data coming soon...")