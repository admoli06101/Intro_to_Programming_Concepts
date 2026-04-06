total_rain = 0.0
total_wind = 0.0
count = 0

while True:
    data = input()
    values = data.split()

    rain = float(values[0])

    if rain == -1.0:
        break

    wind = float(values[1])

    total_rain = total_rain + rain
    total_wind = total_wind + wind
    count = count + 1

average_rain = total_rain / count
average_wind = total_wind / count

severity = (average_rain * 10) + average_wind

print("The average rain is", average_rain, "inches")
print("The average wind is", average_wind, "mph")
print("The weather severity for these", count, "readings is:", severity)

print("Aiden Molinary")