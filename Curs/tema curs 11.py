import pandas as pd
import matplotlib.pyplot as plt

# EXERCIȚIUL 1: Analiza și Vizualizarea Datelor Meteo

print("Exercițiul 1: Introducerea și analiza datelor meteo")
data_meteo = pd.DataFrame(columns=['Data', 'Temperatura', 'Umiditate', 'Viteza Vantului'])

nr_zile_meteo = int(input("Introduceți numărul de zile pentru care doriți să adăugați date meteo: "))

for i in range(nr_zile_meteo):
    data = input(f"Introduceți data pentru ziua {i + 1} (format YYYY-MM-DD): ")
    temperatura = float(input("Introduceți temperatura (°C): "))
    umiditate = float(input("Introduceți umiditatea (%): "))
    viteza_vantului = float(input("Introduceți viteza vântului (km/h): "))

    data_meteo = pd.concat([data_meteo, pd.DataFrame({
        'Data': [data],
        'Temperatura': [temperatura],
        'Umiditate': [umiditate],
        'Viteza Vantului': [viteza_vantului]
    })], ignore_index=True)

data_meteo['Data'] = pd.to_datetime(data_meteo['Data'])
data_meteo['Temperatura Resimtita'] = data_meteo['Temperatura'] - 0.7 * (data_meteo['Umiditate'] / 100)

zi_cu_temp_max = data_meteo.loc[data_meteo['Temperatura Resimtita'].idxmax()]
zi_cu_temp_min = data_meteo.loc[data_meteo['Temperatura Resimtita'].idxmin()]

print("\nZiua cu cea mai mare temperatură resimțită:")
print(zi_cu_temp_max)
print("\nZiua cu cea mai mică temperatură resimțită:")
print(zi_cu_temp_min)

plt.figure(figsize=(12, 6))
plt.plot(data_meteo['Data'], data_meteo['Temperatura'], label='Temperatura')
plt.plot(data_meteo['Data'], data_meteo['Temperatura Resimtita'], label='Temperatura Resimțită', linestyle='--')
plt.legend()
plt.title('Temperatura și Temperatura Resimțită pe parcursul perioadei introduse')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.show()


# EXERCIȚIUL 2: Simularea și Analiza Pieței de Acțiuni

print("\nExercițiul 2: Introducerea și analiza datelor despre acțiuni")
data_actiuni = pd.DataFrame(columns=['Data', 'Schimbare Zilnica (%)', 'Pret Inchidere'])

nr_zile_actiuni = int(input("Introduceți numărul de zile pentru care doriți să adăugați date despre acțiuni: "))

for i in range(nr_zile_actiuni):
    data = input(f"Introduceți data pentru ziua {i + 1} (format YYYY-MM-DD): ")
    schimbare_pct = float(input("Introduceți schimbarea zilnică (%) a prețului: "))
    pret_inchidere = float(input("Introduceți prețul de închidere ($): "))

    data_actiuni = pd.concat([data_actiuni, pd.DataFrame({
        'Data': [data],
        'Schimbare Zilnica (%)': [schimbare_pct],
        'Pret Inchidere': [pret_inchidere]
    })], ignore_index=True)

data_actiuni['Data'] = pd.to_datetime(data_actiuni['Data'])
data_actiuni['Media Mobila 30 zile'] = data_actiuni['Pret Inchidere'].rolling(window=30).mean()
data_actiuni['Media Mobila 100 zile'] = data_actiuni['Pret Inchidere'].rolling(window=100).mean()

plt.figure(figsize=(14, 7))
plt.plot(data_actiuni['Data'], data_actiuni['Pret Inchidere'], label='Pret Inchidere', color='blue')
plt.plot(data_actiuni['Data'], data_actiuni['Media Mobila 30 zile'], label='Media Mobila 30 zile', color='orange')
plt.plot(data_actiuni['Data'], data_actiuni['Media Mobila 100 zile'], label='Media Mobila 100 zile', color='green')
plt.fill_between(data_actiuni['Data'], data_actiuni['Media Mobila 100 zile'], data_actiuni['Pret Inchidere'],
                 where=(data_actiuni['Pret Inchidere'] > data_actiuni['Media Mobila 100 zile']), color='lightgreen', alpha=0.5, label='Peste Media Mobila 100 zile')
plt.legend()
plt.title('Pretul Actiunilor si Mediile Mobile')
plt.xlabel('Data')
plt.ylabel('Pret ($)')
plt.show()


# EXERCIȚIUL 3: Analiza Datelor de Rating ale Filmelor

print("\nExercițiul 3: Introducerea și analiza datelor despre ratingurile filmelor")
data_ratinguri = pd.DataFrame(columns=['ID Utilizator', 'ID Film', 'Rating'])

nr_evaluari = int(input("Introduceți numărul de evaluări: "))

for i in range(nr_evaluari):
    id_utilizator = int(input(f"Introduceți ID-ul utilizatorului pentru evaluarea {i + 1}: "))
    id_film = int(input("Introduceți ID-ul filmului: "))
    rating = int(input("Introduceți ratingul (1-5): "))

    data_ratinguri = pd.concat([data_ratinguri, pd.DataFrame({
        'ID Utilizator': [id_utilizator],
        'ID Film': [id_film],
        'Rating': [rating]
    })], ignore_index=True)

rating_med_film = data_ratinguri.groupby('ID Film')['Rating'].mean()
numar_evaluari = data_ratinguri.groupby('ID Film')['Rating'].count()

cele_mai_bune_5 = rating_med_film.nlargest(5)

print("\nTop 5 filme cu cel mai mare rating mediu:")
print(cele_mai_bune_5)

plt.figure(figsize=(10, 6))
plt.hist(data_ratinguri['Rating'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribuția Ratingurilor')
plt.xlabel('Rating')
plt.ylabel('Frecvență')
plt.show()

cele_mai_bune_5.plot(kind='bar', color='green', figsize=(10, 6))
plt.title('Top 5 Filme cu Cel Mai Mare Rating Mediu')
plt.xlabel('ID Film')
plt.ylabel('Rating Mediu')
plt.show()
