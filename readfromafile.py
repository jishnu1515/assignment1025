import matplotlib.pyplot as plt
def quadratic_weather_model(time, pressure, windspeed, humidity):
 temperature = pressure * (time ** 2) + windspeed * time + humidity
 return temperature
def main():
 print("Quadratic Weather Modeling")
 print("==========================")
 try:
 with open('MultipleVariablesInput.txt', 'r') as file:
 lines = file.readlines()
 time_values = list(range(0, 11))
 plt.figure(figsize=(8, 6))
 for line in lines:
 variables = line.split()[:3] # Take only the first three values
 pressure, windspeed, humidity = map(float, variables)
 temperature_values = [quadratic_weather_model(t, pressure,
windspeed, humidity) for t in time_values]
 plt.plot(time_values, temperature_values, marker='o', linestyle='-',
label=f'Pressure={pressure}, Wind Speed={windspeed}, Humidity={humidity}')
 plt.title('Temperature Variation Over Time')
 plt.xlabel('Time')
 plt.ylabel('Temperature')
 plt.grid(True)
 plt.xlim(0, 10)
 plt.legend()
 plt.show()
 except FileNotFoundError:
 print("File not found. Please make sure 'MultipleVariablesInput.txt'
exists.")
if __name__ == "__main__":
 main()
