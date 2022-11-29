# Pong

Pongia voi pelata tässä versiossa tietokonetta vastaan ilman pistelaskua. Vasemmalla sijaitsevaa pelaajan mailaa liikutetaan pystysuunnassa nuolinäppäimillä. Tietokoneen maila oikealla liikkuu pallon liikkeiden mukana. Pallo kimpoaa seinistä siten, pallon nopeuden seinää vastaan kohtisuora komponentti muuttuu vastakkaismerkkiseksi. Mailasta pallo kimpoaa siten, että nopeuden mailaa vastaan kohtisuora komponentti muuttuu vastakkaismerkkiseksi ja mailan suuntainen komponentti saa satunnaisen arvon.


## Python-versio

Sovellus toimii Pythonin versiolla 3.8, mutta vanhemmilla versioilla toimivuutta ei voida taata.

## Dokumentaatio

- Käyttöohje (tulossa )
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- Testausdokumentti (tulossa)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Sovelluksen asentaminen ja suoritus

1. Riippuvuudet asennetaan suorittamalla komento:

```bash
poetry install
```

2. Sovelluksen käynnistäminen:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

- Testit ajetaan komennolla

```bash
poetry run invoke test
```

- Testikattavuusraportti muodostetaan komennolla

```bash
poetry run invoke coverage-report
```

- Koodin automaattinen formatointi toimii komennolla

```bash
poetry run invoke format
```

- Koodin Pylint-analyysin saa nähtäväkseen komennolla

```bash
poetry run invoke lint
```
