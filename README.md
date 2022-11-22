# Pong

Kurssilla toteutettava Pong-peli on lastenkengissään, eikä mitään liikettä näytölle ole saatu aikaan. Tarkoitus on, että pelin seuraava versio toimii ja sisältää enemmän ominaisuuksia.


## Python-versio

Sovellus toimii Pythonin versiolla 3.8, mutta vanhemmilla versioilla toimivuutta ei voida taata.

## Dokumentaatio

- Käyttöohje (tulossa )
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- Arkkitehtuurikuvaus (tulossa)
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