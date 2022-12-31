# Arkkitehtuurikuvaus

## Ohjelman rakenne

Ohjelman rakenne on kaksitasoinen, mikä ilmenee alla olevasta pakkauskaaviosta. Käyttöliittymän sisältävät luokat ovat pakkauksessa *ui*. Sovelluslogiikan muodostavat pakkaukset *services* ja *entities*, joista jälkimmäinen sisältää sovelluksen tietosisällön ja ensin mainittu tietosisältöä muokkaavan koodin. Käyttöliittymästä kutsutana ainoastaan *services*-pakkauksen luokkia.

![pakkauskaavio](kuvat/pakkauskaavio.png)

## Käyttöliittymä

Käyttöliittymä on toteutettu pygame-kirjaston avulla. Käyttäjä ohjaa sovellusta näppäimistöllä. Sovelluksen käyttöliittymässä on neljä erilaista näkymää:

* päävalikko
* varsinainen pelinäkymä
* pelin lopetusnäkymä
* pistelista

Käyttöliittymä kutsuu ainoastaan *services*-pakkauksen luokkien *PongService* ja *HiScoreService* Jokainen käyttöliittymän näkymä on toteutettu omana luokkanaan, johon perustuva olio luodaan näkymää käynnistettäessä. Käyttöliittymän päävalikosta vastaava MenuView-olio vastaa muiden näkymien olioiden luomisesta, ja muiden olioiden metodien suorituksen jälkeen ohjelman suoritus palautuu päävalikkoon. Päävalikosta käynnistettäessä peliä siirrytään pelinäkymään. Pelinäkymästä poistuttaessa siirrytään pelin lopetusnäkymään, josta edelleen palataan päävalikkoon. Päävalikosta pääsee myös pistelistanäkymään, josta palataan päävalikkoon.

## Käyttöliittymän ja sovelluslogiikan luokkien suhde

Ohjelman valikko ja muut näkymät on toteutettu omina luokkinaan. Pelin tietosisältö on luokissa Pong, Paddle ja Ball, joiden tietoja luokka PongService lukee ja muokkaa. PongService-luokka tarjoaa metodit, joilla käyttöliittymäluokasta GameView ohjataan pelaajan mailaa sekä haetaan tiedot pelin tilasta. PongService-luokka huolehtii myös tietokoneen mailan ja pallon liikuttamisesta. HiScoreService-luokka huolehtii HiScoreList-luokan sisältämän pistelistan tallentamisesta ohjelman suorituksen aikana.

Alla on esitetty ohjelman luokkakaavio karkealla tasolla.

```mermaid
classDiagram
MenuView -- GameView
MenuView -- HiScoreView
HiScoreView "1" -- "1" HiScoreService 
HiScoreService "1" -- "1" HiScoreList
MenuView "1" -- "1" HiScoreService
GameView "1" -- "1" HiScoreService
GameView "1" -- "1" PongService
PongService "1" -- "1" HiScoreService
GameView "1" -- "1" GameOverView
GameOverView "1" -- "1" HiScoreService
GameOverView "1" -- "1" PongService
PongService "1" -- "1" Pong
Pong "1" -- "2" Paddle
Pong "1" -- "1" Ball
```

## Toiminnallisuudet

### Pelaaminen

Alla oleva sekvenssikaavio kuvaa pelin käynnistämistä ja pelaamista yhden pelisilmukan suorituksen aikana. Pelaaja siirtää mailaansa ylöspäin ja PongService-olio huolehtii tietokoneen mailan siirtämisestä ja pallon liikuttamisesta. Pelin mailojen ja pallon luomisen yksityiskohdat on jätetty kaaviosta luettavuuden parantamiseksi pois.

![pelaamisen sekvenssikaavio](kuvat/sekvenssikaavio_pelaaminen.png)

### Pelin lopettaminen ja pisteiden tallentaminen

Tämän sekvenssikaavion alkutilanteessa peli on jo käynnissä ja pelaaja saa pisteen, mikä päättää pelin. Pelaajan pisteet tallennetaan listalle pelaajan nimen kanssa. Tämän jälkeen ohjelma palaa päävalikkoon.

![pisteiden tallennuksen sekvenssikaavio](kuvat/sekvenssikaavio_pelin_lopetus.png)

### Pistelistan tarkastelu

Seuraavassa sekvenssikaaviossa esitetään ohjelman käynnistäminen ja pistelistan tarkastelu, jonka jälkeen palataan päävalikkoon ja ohjelma suljetana.

![pistelistan sekvenssikaavio](kuvat/sekvenssikaavio_pistelista.png)