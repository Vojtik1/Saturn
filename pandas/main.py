import pandas as pd
from tempan import TemperatureAnalytics


data_path = '.\klementinum.xlsx'  # Upravte cestu k vašemu souboru
data_sheet_name = 'data'
temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)




def main():
    # Set matplotlib backend
    import matplotlib
    matplotlib.use('TkAgg')  # Use TkAgg backend

    temperature_analytics = TemperatureAnalytics(temperature_data)

    while True:
        print("0. Ukončit aplikaci")
        print("1. Průměrná teplota v zadaném roce")
        print("2. Maximální teplota v zadaném roce")
        print("3. Minimální teplota v zadaném roce")
        print("4. GRAF Průměrné roční teploty mezi zadanými lety")
        print("5. GRAF Průměrné měsíční teploty v zadaném roce")
        print("6. GRAF Rozložení teplot v roce podle dnů")
        print("7. GRAF Porovnávání teplot")
        print("8. GRAF Vztah mezi průměrnou teplotou a srážkami")
        print("9. GRAF Sezónní trendy průměrných teplot")
        print("10.GRAF Lineární trend průměrných teplot")

        choice = input("Zvolte možnost (0-10): ")

        if choice == '1':
            year = int(input("Zadejte rok: "))
            print(f"Průměrná teplota v roce {year}: {temperature_analytics.get_average_temperature(year)}°C")
        elif choice == '2':
            year = int(input("Zadejte rok: "))
            max_temp, date_of_max_temp = temperature_analytics.get_max_temperature(year)
            print(
                f"Maximální teplota v roce {year}: {max_temp}°C, datum: {date_of_max_temp['den']}.{date_of_max_temp['měsíc']}.{date_of_max_temp['rok']}")
        elif choice == '3':
            year = int(input("Zadejte rok: "))
            min_temp, date_of_min_temp = temperature_analytics.get_min_temperature(year)
            print(
                f"Minimální teplota v roce {year}: {min_temp}°C, datum: {date_of_min_temp['den']}.{date_of_min_temp['měsíc']}.{date_of_min_temp['rok']}")
        elif choice == '4':
            start_year = int(input("Zadejte počáteční rok: "))
            end_year = int(input("Zadejte koncový rok: "))
            plot_type = input("Zadejte typ grafu ('line', 'bar' nebo 'pie'): ")
            temperature_analytics.plot_annual_temperature_averages(start_year, end_year, plot_type)
        elif choice == '5':
            year = int(input("Zadejte rok: "))
            plot_type = input("Zadejte typ grafu ('line', 'bar' nebo 'pie'): ")
            temperature_analytics.plot_monthly_average_temperatures(year, plot_type)
        elif choice == '6':
            year = int(input("Zadejte rok: "))
            plot_type = input("Zadejte typ grafu ('hist' nebo 'box'): ")
            temperature_analytics.plot_temperature_distribution(year, plot_type)
        elif choice == '7':
            start_year1 = int(input("Zadejte počáteční rok prvního období: "))
            end_year1 = int(input("Zadejte koncový rok prvního období: "))
            start_year2 = int(input("Zadejte počáteční rok druhého období: "))
            end_year2 = int(input("Zadejte koncový rok druhého období: "))
            plot_type = input("Zvolte 'line', 'bar', 'box' nebo 'scatter':")
            temperature_analytics.compare_temperature_trends(start_year1, end_year1, start_year2, end_year2, plot_type)
        elif choice == '8':
            year = int(input("Zadejte rok: "))
            plot_type = input("Zvolte 'hexbin' nebo 'scatter':")
            temperature_analytics.analyze_temperature_precipitation_relationship(year, plot_type)
        elif choice == '9':
            start_year = int(input("Zadejte počáteční rok: "))
            end_year = int(input("Zadejte koncový rok: "))
            temperature_analytics.analyze_seasonal_temperature_trends(start_year, end_year)

        elif choice == '10':
            start_year = int(input("Zadejte počáteční rok: "))
            end_year = int(input("Zadejte koncový rok: "))
            plot_type = input("Zvolte 'line' nebo 'scatter': ")
            temperature_analytics.analyze_temperature_trend_regression(start_year, end_year, plot_type)
        elif choice == '0':
            print("Ukončuji program.")
            break
    else:
        print("Neplatná volba. Zadejte číslo od 0 do 10.")


if __name__ == '__main__':
    main()
