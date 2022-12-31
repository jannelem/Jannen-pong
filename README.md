# Jannen Pong

Harjoitustyössä toteutettiin Pong-peli, jossa pelaaja pelaa Pongia tietokonetta vastaan. Peli tallentaa parhaat pisteet listalle suorituksen aikana. (Ajan puutteessa pistelistan pitkäaikaistallennus jäi tekemättä.) 

Vasemmalla sijaitsevaa pelaajan mailaa liikutetaan pystysuunnassa nuolinäppäimillä. Tietokoneen maila oikealla liikkuu pallon liikkeiden mukana silloin, kun pallo on tietokoneen puolella ruutua liikkumassa tietokoneen mailaa kohti. Pallo kimpoaa seinistä siten, että se saapuu ja lähtee seinästä yhtä suuressa kulmassa. Mailasta pallo kimpoaa satunnaiseen suuntaan satunnaisella nopeudella.

## Python-versio

Sovellus toimii Pythonin versiolla 3.8, mutta vanhemmilla versioilla toimivuutta ei voida taata.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
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
