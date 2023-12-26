import matplotlib.pyplot as plt
def quadratic_weather_model(time, pressure, windspeed, humidity):
 temperature = pressure * (time ** 2) + windspeed * time + humidity
 return temperature
def main():
 pressure = float(input("Enter the value of pressure: "))
 windSpeed = float(input("Enter the value of windSpeed: "))
 humidity = float(input("Enter the value of humidity: "))
 time_values = list(range(0, 11))
 temperature_values = [quadratic_weather_model(t, pressure, windSpeed,
humidity) for t in time_values]
 plt.figure(figsize=(8, 6))
 plt.plot(time_values, temperature_values, marker='o', linestyle='-')
 plt.title('Temperature Variation Over Time')
 plt.xlabel('Time')
 plt.ylabel('Temperature')
 plt.grid(True)
 plt.xlim(0, 10)
 plt.ylim(min(temperature_values) - 5, max(temperature_values) + 5)
 plt.show()
if __name__ == "__main__":
 main()
