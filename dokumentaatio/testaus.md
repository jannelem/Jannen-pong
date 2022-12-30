# Testausdokumentti

Peliä on testattu sekä yksittäisten metodien tasolla että integraatiotasolla unittestillä. Järjestelmätason testaus on tehty manuaalisesti pelaamalla peliä ja luomalla eri skenaarioita.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Yksikkötason testejä on tehty etenkin objects-pakkauksen luokille ja metodeille, jotka vastaavat pelin tietosisällön ylläpitämisestä. Integraatiotasolla on testattu etenkin services-pakkauksen luokkia, jotka muokkaavat objects-pakkauksen luokista muodostettujen olioiden tietoja.

### Testikattavuus

Alla olevasta testikattavuusraportista nähdään, että sovelluslogiikka on testattu erittäin kattavasti. Käytännössä 100 % kattavuudesta jäävät puutteet koskevat yksittäisiä koodirivejä, mutta kaikkia luokkia ja metodeja on pyritty testaamaan mahdollisimman monipuolisesti.

![testikattavuusraportti](kuvat/kattavuus.png)

## Järjestelmätestaus

Koko pelin toimivuutta on testattu manuaalisesti. Asennuksessa ja käynnistämisessä ei havaittu ongelmia. Testaus olisi ollut haastavampaa, jos aika olisi riittänyt koodata peliin myös pistelistan pitkäaikaistallennus. Tässä versiossa pistelista luodaan uudestaan aina ohjelmaa suoritettaessa, joten se on tästäkin syystä oikeassa muodossa.

### Esimerkkejä järjestelmätestauksen myötä tehdyistä korjauksista

Peliä koodattaessa pelin toimintaa on testattu ajamalla erilaisia skenaarioita. Alla on esitetty esimerkkejä joistakin ongelmista, joita täten tehdyn testauksen myötä on korjattu

* Pallo jäi "kiinni" mailaan sovelluslogiikan hyödyntäessä satunnaisuutta kimpoamisen jälkeisen nopeuden määrittämisessä. Tämä korjattiin lisäämällä yksi rivi koodia ennen uuden nopeuden arpovaa kohtaa. Tällä rivillä pallo siirtyy sivusuunnassa yhden askeleen taaksepäin, jolloin riskiä "tarttumisesta" ei ole. Tämä ei kuitenkaan näy pelin toiminnassa minkäänlaisena nykimisenä.
* Käyttäjän syöttäessä nimeään päästyään pistelistalle havaittiin erilaisia ongelmia. Yksi ongelma oli se, että käyttöliittymä ei aina vastannut heti kirjainnäppäinten painalluksiin. Tämä korjattiin muuttamalla käyttöliittymämetodin silmukkarakennetta. Toinen haaste oli se, että käyttäjällä oli mahdollisuus kirjoittaa nimi, joka sisältää pilkun. Tämä olisi aiheuttanut ongelmia tiedon pitkäaikaistallennuksessa csv-muodossa. Pilkun syöttäminen estettiin käyttöliittymätasolla.
* Käyttäjän syöttäessä pistelistalle päästyään liian pitkän nimen (yli 15 merkkiä) pistelistan näyttö menee sekavan näköiseksi. Myös tämä korjaus tehtiin käyttöliittymään estämällä yli 15-merkkisten nimen syöttäminen siten, ettei käyttöliittymä reagoi uusiin merkkeihin 15 merkin tullessa täyteen, ellei käyttäjä ensin pyyhi syöttämiään merkkejä backspace-näppäimellä.

### Ohjelmaan jääneitä laatuongelmia

* Pistelistan pisteet eivät näy täysin oikein tasattuina.
* Pisteiden pitkäaikaistallennusta ja siihen liittyviä toiminnallisuuksia ei ehditty toteuttaa.
