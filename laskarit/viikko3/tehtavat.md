# Viikon 3 tehtävät

## Tehtävä 1

```mermaid

classDiagram
  Monopoli "1" -- "1" Pelilauta
  Monopoli "1" -- "2" Noppa
  Pelilauta "1" -- "40" Ruutu
  Monopoli "1" -- "2..8" Pelaaja
  class Ruutu {
    Ruutu seuraava
    }
```

## Tehtävä 2

```mermaid

classDiagram
  Monopoli "1" -- "1" Pelilauta
  Monopoli "1" -- "2" Noppa
  Pelilauta "1" -- "40" Ruutu
  Aloitusruutu --|> Ruutu
  Vankila --|> Ruutu
  Sattuma --|> Ruutu
  Yhteismaa --|> Ruutu
  Asema --|> Ruutu
  Laitos --|> Ruutu
  Katu --|> Ruutu
  Sattuma "*" -- "*" Kortti
  Yhteismaa "*" -- "*" Kortti
  Pelaaja "1" -- "*" Katu
  Monopoli "1" -- "2..8" Pelaaja
  class Ruutu {
    Ruutu seuraava
    }
  class Pelilauta {
    Ruutu aloitus
    Ruutu vankila
    toiminto()
  }
  class Kortti {
    toiminto()
  }
  class Pelaaja {
    int rahaa
  }
  class Katu {
  int talot
  boolean hotelli
  }
```

Huom.! En löytänyt konstia saada Mermaid-syntaksissa aikaan onttoa nuolta kuvaamaan perintää, joten tämän kaavion mustapäiset nuolet tulisi tulkita perinnäksi.

## Tehtävä 3

![tehtävän 3 sekvenssikaavio](teht3.png)

## Tehtävä 4

![tehtävän 4 sekvenssikaavio](teht4.png)
