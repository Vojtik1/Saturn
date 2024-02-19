import matplotlib.pyplot as plt
from scipy.stats import linregress

class TemperatureAnalytics:
    def __init__(self, data):
        self.data = data

    def get_average_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        return yearly_data['T-AVG'].mean()

    def get_max_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        max_temp = yearly_data['TMA'].max()
        date_of_max_temp = yearly_data[yearly_data['TMA'] == max_temp][['rok', 'měsíc', 'den']].iloc[0]
        return max_temp, date_of_max_temp

    def get_min_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        min_temp = yearly_data['TMI'].min()
        date_of_min_temp = yearly_data[yearly_data['TMI'] == min_temp][['rok', 'měsíc', 'den']].iloc[0]
        return min_temp, date_of_min_temp

    def get_monthly_averages(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        return yearly_data.groupby('měsíc')['T-AVG'].mean()

    def analyze_temperature_trends(self, start_year, end_year):
        trend_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        annual_average_temperatures = trend_data.groupby('rok')['T-AVG'].mean()
        return annual_average_temperatures

    def plot_annual_temperature_averages(self, start_year, end_year, plot_type='line'):
        filtered_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]

        annual_avg_temps = filtered_data.groupby('rok')['T-AVG'].mean()
        plt.figure(figsize=(10, 6))

        if plot_type == 'line':
            plt.plot(annual_avg_temps.index, annual_avg_temps.values, marker='o', linestyle='-', color='b')
        elif plot_type == 'bar':
            plt.bar(annual_avg_temps.index, annual_avg_temps.values, color='skyblue')
        elif plot_type == 'pie':
            plt.pie(annual_avg_temps.values, labels=annual_avg_temps.index, autopct='%1.1f%%', startangle=140)
            plt.title(f'Podíl průměrných ročních teplot mezi lety {start_year} - {end_year}')
            plt.axis('equal')  # Zajištění, aby byl kruhový
            plt.show()
            return
        else:
            raise ValueError("Neplatný typ grafu. Zvolte 'line', 'bar' nebo 'pie'.")

        plt.title(f'Průměrné roční teploty mezi lety {start_year} - {end_year}')
        plt.xlabel('Rok')
        plt.ylabel('Průměrná teplota (°C)')
        plt.grid(True)
        plt.show()

    def plot_monthly_average_temperatures(self, year, plot_type='line'):
        yearly_data = self.data[self.data['rok'] == year]
        monthly_avg_temps = yearly_data.groupby('měsíc')['T-AVG'].mean()

        plt.figure(figsize=(10, 6))

        if plot_type == 'line':
            plt.plot(monthly_avg_temps.index, monthly_avg_temps.values, marker='o', linestyle='-', color='g')
        elif plot_type == 'bar':
            plt.bar(monthly_avg_temps.index, monthly_avg_temps.values, color='lightgreen')
        elif plot_type == 'pie':
            labels = [f'Měsíc {i}' for i in range(1, 13)]
            plt.pie(monthly_avg_temps.values, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title(f'Podíl průměrných měsíčních teplot v roce {year}')
            plt.axis('equal')  # Zajištění, aby byl kruhový
            plt.show()
            return
        else:
            raise ValueError("Neplatný typ grafu. Zvolte 'line', 'bar' nebo 'pie'.")

        plt.title(f'Průměrné měsíční teploty v roce {year}')
        plt.xlabel('Měsíc')
        plt.ylabel('Průměrná teplota (°C)')
        plt.grid(True)
        plt.xticks(range(1, 13))  # Nastavení měsíčních značek na x-ové ose
        plt.show()

    def plot_temperature_distribution(self, year, plot_type='hist'):
        yearly_data = self.data[self.data['rok'] == year]

        plt.figure(figsize=(10, 6))

        if plot_type == 'hist':
            plt.hist(yearly_data['T-AVG'], bins=20, color='orange', edgecolor='black')
        elif plot_type == 'box':
            plt.boxplot(yearly_data['T-AVG'], vert=False)
        else:
            raise ValueError("Neplatný typ grafu. Zvolte 'hist' nebo 'box'.")

        plt.title(f'Rozložení teplot v roce {year}')
        plt.xlabel('Teplota (°C)')
        plt.ylabel('Počet dnů')
        plt.grid(True)
        plt.show()

    def compare_temperature_trends(self, start_year1, end_year1, start_year2, end_year2, plot_type='line'):
        trend_data1 = self.data[(self.data['rok'] >= start_year1) & (self.data['rok'] <= end_year1)]
        trend_data2 = self.data[(self.data['rok'] >= start_year2) & (self.data['rok'] <= end_year2)]

        annual_avg_temps1 = trend_data1.groupby('rok')['T-AVG'].mean()
        annual_avg_temps2 = trend_data2.groupby('rok')['T-AVG'].mean()

        plt.figure(figsize=(10, 6))

        if plot_type == 'line':
            plt.plot(annual_avg_temps1.index, annual_avg_temps1.values, marker='o', linestyle='-', color='b',
                     label=f'Trend {start_year1}-{end_year1}')
            plt.plot(annual_avg_temps2.index, annual_avg_temps2.values, marker='s', linestyle='-', color='r',
                     label=f'Trend {start_year2}-{end_year2}')
        elif plot_type == 'bar':
            plt.bar(annual_avg_temps1.index - 0.2, annual_avg_temps1.values, width=0.4, color='b',
                    label=f'Trend {start_year1}-{end_year1}')
            plt.bar(annual_avg_temps2.index + 0.2, annual_avg_temps2.values, width=0.4, color='r',
                    label=f'Trend {start_year2}-{end_year2}')
        elif plot_type == 'box':
            plt.boxplot([annual_avg_temps1.values, annual_avg_temps2.values],
                        labels=[f'{start_year1}-{end_year1}', f'{start_year2}-{end_year2}'])
        elif plot_type == 'scatter':
            plt.scatter(annual_avg_temps1.index, annual_avg_temps1.values, color='b',
                        label=f'Trend {start_year1}-{end_year1}')
            plt.scatter(annual_avg_temps2.index, annual_avg_temps2.values, color='r',
                        label=f'Trend {start_year2}-{end_year2}')
        else:
            raise ValueError("Neplatný typ grafu. Zvolte 'line', 'bar', 'box' nebo 'scatter'.")

        plt.title('Porovnání průměrných teplotních trendů')
        plt.xlabel('Rok')
        plt.ylabel('Průměrná teplota (°C)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def analyze_temperature_precipitation_relationship(self, year, plot_type='scatter'):
        yearly_data = self.data[self.data['rok'] == year]

        plt.figure(figsize=(10, 6))

        if plot_type == 'scatter':
            plt.scatter(yearly_data['T-AVG'], yearly_data['SRA'], color='green')
            plt.title(f'Vztah mezi průměrnou teplotou a srážkami v roce {year}')
            plt.xlabel('Průměrná teplota (°C)')
            plt.ylabel('Průměrné srážky (mm)')
        elif plot_type == 'hexbin':
            plt.hexbin(yearly_data['T-AVG'], yearly_data['SRA'], gridsize=20, cmap='Greens', mincnt=1)
            plt.colorbar(label='Počet dnů')
            plt.title(f'Vztah mezi průměrnou teplotou a srážkami v roce {year}')
            plt.xlabel('Průměrná teplota (°C)')
            plt.ylabel('Průměrné srážky (mm)')
        else:
            raise ValueError("Neplatný typ grafu. Zvolte 'scatter' nebo 'hexbin'.")

        plt.grid(True)
        plt.show()

    def analyze_seasonal_temperature_trends(self, start_year, end_year):
        trend_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        trend_data['season'] = (trend_data['měsíc'] % 12 + 3) // 3  # Vytvoření sezónních kategorií

        seasonal_avg_temps = trend_data.groupby(['rok', 'season'])['T-AVG'].mean()
        seasonal_avg_temps = seasonal_avg_temps.unstack()  # Převod na přehlednější formát pro graf

        plt.figure(figsize=(12, 6))
        seasonal_avg_temps.plot(marker='o', linestyle='-', markerfacecolor='w')  # Každá sezóna na samostatném sloupci
        plt.title('Sezónní trendy průměrných teplot')
        plt.xlabel('Rok')
        plt.ylabel('Průměrná teplota (°C)')
        plt.legend(['Jaro', 'Léto', 'Podzim', 'Zima'], loc='upper right')
        plt.grid(True)
        plt.show()

    def analyze_temperature_trend_regression(self, start_year, end_year, plot_type='line'):
        trend_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]

        x_values = trend_data['rok'].values  # Použijeme sloupec s roky
        y_values = trend_data['T-AVG'].values

        slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)

        plt.figure(figsize=(10, 6))

        if plot_type == 'line':
            plt.plot(x_values, y_values, marker='o', linestyle='', color='b', label='Průměrné teploty')
            plt.plot(x_values, slope * x_values + intercept, color='r', label='Lineární trend')
        elif plot_type == 'scatter':
            plt.scatter(x_values, y_values, color='g', label='Průměrné teploty')
            plt.plot(x_values, slope * x_values + intercept, color='r', label='Lineární trend')
        else:
            raise ValueError("Neplatný typ grafu. Zvolte 'line' nebo 'scatter'.")

        plt.title('Lineární trend průměrných teplot')
        plt.xlabel('Rok')
        plt.ylabel('Průměrná teplota (°C)')
        plt.legend()
        plt.grid(True)
        plt.show()

        print(f'Lineární trend: {slope:.4f} °C/rok')
        print(f'Korelace (R-value): {r_value:.4f}')
        print(f'P-hodnota: {p_value:.4f}')
        print(f'Standardní chyba odhadu: {std_err:.4f}')




