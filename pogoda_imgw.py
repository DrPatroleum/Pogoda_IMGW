import requests
import json
from tkinter import *
from tkinter import ttk

miasta = {"Białystok": 12295, "Bielsko Biała": 12600, "Chojnice": 12235, "Częstochowa": 12550, "Elbląg": 12160, "Gdańsk": 12155, "Gorzów": 12300,
          "Hel": 12135, "Jelenia Góra": 12500, "Kalisz": 12435, "Kasprowy Wierch": 12650, "Katowice": 12560, "Kętrzyn": 12185, "Kielce": 12570, "Kłodzko": 12520,
          "Koło": 12345, "Kołobrzeg": 12100, "Koszalin": 12105, "Kozienice": 12488, "Kraków": 12566, "Krosno": 12670, "Legnica": 12415, "Lesko": 12690, "Leszno": 12418,
          "Lębork": 12125, "Lublin": 12495, "Łeba": 12120, "Łódź": 12465, "Mikołajki": 12280, "Mława": 12270, "Nowy Sącz": 12660, "Olsztyn": 12272, "Opole": 12530,
          "Ostrołęka": 12285, "Piła": 12230, "Platforma Baltic Beta": 12001, "Płock": 12360, "Poznań": 12330, "Przemyśl": 12695, "Racibórz": 12540, "Resko": 12210,
          "Rzeszów": 12580, "Sandomierz": 12585, "Siedlce": 12385, "Słubice": 12310, "Sulejów": 12469, "Suwałki": 12195, "Szczecin": 12205, "Szczecinek": 12215,
          "Śnieżka": 12510, "Świnoujście": 12200, "Tarnów": 12575, "Terespol": 12399, "Toruń": 12250, "Ustka": 12115, "Warszawa": 12375, "Wieluń": 12455, "Włodawa": 12497,
          "Wrocław": 12424, "Zakopane": 12625, "Zamość": 12595, "Zielona Góra": 12400}

opcje_miast = sorted(miasta.keys())

sila_wiatru = {"cisza": (0, 0.2), "powiew": (0.2, 1.5), "słaby wiatr": (1.6, 3.3), "łagodny wiatr": (3.4, 5.4), "umiarkowany wiatr": (5.5, 7.9), "dość silny wiatr": (8, 10.7),
               "silny wiatr": (10.8, 13.8), "bardzo silny wiatr": (13.9, 17.1), "sztorm": (17.2, 20.7), "silny sztorm": (20.8, 24.4), "bardzo silny sztorm": (24.5, 28.4),
               "gwałtowny sztorm": (28.5, 32.6), "huragan": (32.7, 100)}
kierunki = {"północny": (337.6, 22.5), "północno-wschodni": (22.6, 67.5), "wschodni": (67.6, 112.5), "południowo-wschodni": (112.6, 157.5),
            "południowy": (157.6, 202.5), "południowo-zachodni": (202.6, 247.5), "zachodni": (247.6, 292.5), "północno-zachodni": (292.6, 337.5)}


def pokaz_pogode():
    miasto = str(option_var.get())
    id_stacji = miasta[miasto]

    link = ("https://danepubliczne.imgw.pl/api/data/synop/id/xyz")
    link_test = (
        "https://danepubliczne.imgw.pl/api/data/synop/station/warszawa")
    response = requests.get(link_test)

    if response.status_code == 200:
        req = requests.get(link.replace("xyz", str(id_stacji)))
        json_data = req.text
        data = json.loads(json_data)

        stacja = data["stacja"]
        data_pomiaru = data["data_pomiaru"]
        godzina_pomiaru = data["godzina_pomiaru"]
        temperatura = data["temperatura"]
        predkosc_wiatru = data["predkosc_wiatru"]
        kierunek_wiatru = data["kierunek_wiatru"]
        wilgotnosc_wzgledna = data["wilgotnosc_wzgledna"]
        suma_opadu = data["suma_opadu"]
        cisnienie = data["cisnienie"]
        
        for zwrot, (min_wartosc, max_wartosc) in sila_wiatru.items():
            if min_wartosc <= int(predkosc_wiatru) <= max_wartosc:
                x = zwrot
        
        for kierunek, (min_wartosc, max_wartosc) in kierunki.items():
            if min_wartosc <= int(kierunek_wiatru) <= max_wartosc:
                y = kierunek

        info = (f"""
                Pomiar z dnia {data_pomiaru} 
                z godz. {godzina_pomiaru}:00 ze stacji {stacja}
                Temperatura powietrza {temperatura} ℃
                Wiatr o prędkości {predkosc_wiatru} m/s 
                ({y} {x})
                Wilgotność powietrza: {wilgotnosc_wzgledna}%
                Suma opadów: {suma_opadu} mm
                Ciśnienie atmosferyczne: {cisnienie} hPa
                """)
        label1.config(text=info)
    else:
        info = (f"Wystąpił problem z połączeniem z Internetem!")
        label1.config(text=info)


window = Tk()
window.title("Pogoda")
window.resizable(True, True)

top_frame = Frame(window, relief="raised", bd=2)
top_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

label_start = Label(top_frame, text="Warunki atmosferyczne\n dla wybranej stacji pomiarowej IMGW")
label_start.grid(row=1, column=0, padx=5, pady=5, sticky=EW, columnspan=3)

option_var = StringVar(top_frame)
max_length = max(len(option) for option in opcje_miast)

option_menu = OptionMenu(top_frame, option_var, *opcje_miast)
option_menu.grid(row=2, column=1, sticky=NS)
option_menu.config(width=max_length + 2)
option_var.set("Wybierz lokalizację")

button = Button(top_frame, text='Pokaż', command=pokaz_pogode)
button.grid(row=2, column=2, sticky=NS, padx=5, pady=5)

label1 = Label(top_frame)
label1.grid(row=3, column=0, sticky=NS, columnspan=2)

window.mainloop()
