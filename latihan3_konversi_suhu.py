# Konversi Celsius ke Fahrenheit dan Kelvin
def konversi_suhu(celsius):

    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15

    return fahrenheit, kelvin


if __name__ == "__main__":
    print("=== Program Konversi Suhu (Celsius) ===")
    try:
        celsius = float(input("Masukkan suhu dalam Celsius (°C): "))

        fahrenheit, kelvin = konversi_suhu(celsius)

        print(f"\nHasil Konversi untuk {celsius}°C:")
        print(f"1. Fahrenheit : {fahrenheit:.2f} °F")
        print(f"2. Kelvin     : {kelvin:.2f} K")

    except ValueError:
        print("Error: Harap masukkan angka yang valid!")