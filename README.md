# Micropython notes

## Commands

connection to REPL

```sh
mpremote connect list
mpremote connect port:/dev/ttyACM0
```

run single file

```sh
mpremote run blinker.py
```

soft-reset of the device (RAM stay untouched)

```sh
mpremote soft-reset
```

sharing files from host to device, for easier development

```sh
mpremote mount sensors_device/
```

and then running the code

```python
from main import main
```

eventually - copying files to device

```sh
mpremote fs cp -v sensors/*.py :
```

## DB queries

```sql
select readtime,regname,value from sensorsdata where regname="scd_co2_ppm_level";
```


## CO2

| Stężenie  CO2 | Wpływ na organizm człowieka                                                       |
|---------------|-----------------------------------------------------------------------------------|
| do  600 ppm   | Uczucie świeżości w pomieszczeniu, optymalne warunki                              |
| do 1000 ppm   | Maksymalny próg w pomieszczeniach, w których stale przebywają ludzie zgodny z WHO |
| do 1500 ppm   | Wyczuwalna duszność powietrza, wyraźny brak świeżości                             |
| do 10000 ppm  | Zwiększenie częstotliwości oddechu                                                |
