---
paginate: true
marp: true
---
# **Czujniki środowiskowe**

Jaroslaw Wencel

---
<!-- paginate: true -->

# Why

1. Żeby wiedzieć czym oddycham w moim gabinecie,
2. Potrzebuję przetestować proces gromadzenia danych z czujników,
3. Dla zabawy - no a jak...

---
<!-- paginate: true -->

# How

*Każdy głupi może kupić gotową stację meteo z prognozą ściąganą z internetu. Co innego budowa własnej, droższej – z tym poradzi sobie nie każdy głupi. Mi się udało.*

autor: Tomasz Zieliński, Informatyk Zakładowy.

źródło: https://informatykzakladowy.pl/pogodynka-zrob-to-sam/

---
<!-- paginate: true -->

# What

## Czyli założenia

1. dane z czujnika SCD41 (temperatura, wilgotność, CO2), później doszły DS1820 i DHT22,
2. oprogramowanie w Pythonie, zarówno część serwerowa jak i sprzętowa,
3. komunikacja po http, żebym mógł tą zabawkę zabrać *w pole*
4. zasilanie z kabla, dostęp do sieci po WiFi,
5. obudowa - może kiedyś.

---
<!-- paginate: true -->

# Baza sprzętowa

- [RaspberryPi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- [Ekspander wyprowadzeń](https://botland.com.pl/raspberry-pi-pico-hat-ekspandery-wyprowadzen/22967-ekspander-wyprowadzen-do-raspberry-pi-pico-zlacza-srubowe-sb-components-22967-5055652925688.html)
- [Czujnik CO2](https://botland.com.pl/gravity-czujniki-gazow-i-pylow/22673-gravity-czujnik-dwutlenku-wegla-co2-scd41-ir-i2c-400-5000-ppm-dfrobot-sen0536--6959420923137.html)
- [Czujnik temperatury i wilgotności](https://botland.com.pl/czujniki-multifunkcyjne/4920-czujnik-temperatury-i-wilgotnosci-dht22-am2302-modul-przewody-waveshare-11092-5904422366889.html)


---
<!-- paginate: true -->

# Oprogramowanie na uC

- [MicroPython jako core](https://micropython.org/)
- biblioteki zewnętrzne - tylko jeśli potrzeba (do SCD41 było trzeba)

---
<!-- paginate: true -->

# Oprogramowanie *serwerowe*

- oczywiście Python :)
- FastAPI + SQLModel + SQLite
- hosting typu cebula - w domu wiadomo, a jak bym miał zabrać urządzenie na świat to API na [mikr.usie](https://mikr.us/)


---
<!-- paginate: true -->

# Alternatywy, czyli co można inaczej

## Hardware

- Arduino Nano ESP32 - fajne, ale ta cena...
- ESP - raczej ESP32 - jest ok, potrzebuje troche więcej prądu niż RPi,
- Arduino *zwykłe* - masochizm w moim zastosowaniu...
- Raspberry Pi Zero - pewnie tak się to skończy...

---
<!-- paginate: true -->

# Alternatywy, czyli co można inaczej

## Software

- MQTT zamiast HTTP - pewnie tak się to śkończy dla szerszego spektrum zastosowań,
- Influx zamiast SQLite, może Promoetheus, albo jakaś inna baza do czasowych serii danych,
- jakaś wizualizacja
- pewnie i tak na Home Assistansie się to skończy


---

<!-- paginate: true -->

# Wnioski

- do programowania hardware'u potrzebna jest cierpliwość, dużo cierpliwości...
- da się coś w tym Pytonie na sprzęt napisać, ale czy ja bym to chciał uruchamiać długofalowo (niestabilność HTTP)?
- odwieczny problem debugowania sprzętu jakoś sam nie chce się rozwiązać,
- ORMy zaskakują, niby to wiedziałem, ale...
- Copilot mi coś nawet podpowiadał jak edytowałem kod MicroPythona...
- zrobić lepsze logi to API