def celsius_to_fahrenheit(celsius):
    # Formula de conversie
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicităm utilizatorului să introducă temperatura în Celsius
try:
    celsius = float(input("Introduceți temperatura în grade Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C este echivalent cu {fahrenheit:.2f}°F.")
except ValueError:
    print("Vă rugăm să introduceți un număr valid!")