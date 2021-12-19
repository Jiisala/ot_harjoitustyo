# Ohjelmistotekniikka, harjoitustyö

## Boulder Pall 9000
 Boulder Pall 9000 on sovellus jonka avulla käyttäjä voi pitää kirjaa kiipeilyreiteiteistä (ohjelma käyttää englannin kielistä termiä "problem"), joita on jo kiivennyt,tai aikoo kiivetä.

 Tämä versio on viimeinen Ohjelmistotekniikka kurssin puitteissa toteututtetu versio. Mikäli jatkokehitystä tulevaisuudessa tapahtuu, julkaistaan seuraavat versiot omassa repositiossaan. Sisäänkirjautumisen (tai uuden käyttäjän luomisen) jälkeen aukeaa päänäkymä, joka on ihastuttavan epäestetttinen. Päänäkymässä näkyy, tervehdys käyttäjälle, kaikki käyttäjän itselleen "tagaamat" reitit ja kolme nappia. Ensimmäisestä pääsee lisämään uuden reitin, toisesta selaamaan kaikkia ohjelmaan lisättyjä reittejä, sekä tagaamaan niitä istelleen (tai pois itseltään), kolmas palaa takaisin kirjautumisnäkymään. Päänäkymässä voi myös merkitä reitin kiivetyksi painamalla solved/unsolved nappia. Reitille lisätty kuva näkyy pienennettynä thumbnailina, sitä klikkaamalla aukeaa alkuperäinen kuva käyttöjärjestelmän oletus kuvienkatselu ohjelmassa.

 Uuden käyttäjän luominen lisää käyttäjän ohjelman tiedontallennuksesta huolehtivaan tietokantaan. Uuden reitin luominen lisää vastaavasti sen tietokantaan, lisäksi juuri luotu reitti ilmestyy näkyviin päänäkymään, sekä näkymään joka näyttää kaikki reitit. Ohjelma tarkistaa sekä käyttäjää että ongelmaa luodessa että nimi on uniikki, eikä luo uutta mikäli saman niminen on jo olemassa. Tästä ei käyttäjä toistaiseksi saa mitäään palautetta.
 
 Sekä päänäkymässä että reittien tarkasteluun tarkoitetussa näkymässä voi reitit järjestää useammall eri tavalla, joko nousevaan tai laskevaan järjestykseen.
 
 Lisätyt ongelmat lisätään myös uxb nimiseen tietokantaan jossa säilytetään tietoa siitä mitä reittejä käyttäjä on lisännyt itselleen ja onko ne jo merkitty kiivetyiksi. Myös reitin tagaaminen lisää sen samaiseen tietokantaan. Tagin poistaminen poistaa reitin tietokannasta, samalla reitti poistuu käyttäjän päänäkymästä ja tieto reitin kiipeämisestä häviää. 
 
 Uutta reittiä luodessa voi reitille valita kuvan, painamalla Select image-nappia. Nappia painamalla avautuu käyttöjärjestelman oma tiedostonvalinta näkymä. Kun kuva on valittu, ohjelma tarkistaa että se on jossakin ohjelman sallimassa tiedostomuodossa (tarkistamalla päätteen). Sallitut päätteet ovat jpg, jpeg, gif, png ja bmp. Ohjelma kopioi valitun kuvan ohjelman juuresta löytyvään ```.data/img/``` kansioon ja luo siitä thumbnailin, joka talletetaan samaan kansioon. mikäli kuvaa ei valita käyttää ohjelma oletuskuvaa.
 
 Testikattavuus on hyvä, testit testaavat reitin ja käyttäjän luomisesta huolehtivia luokkia sekä varsinaista sovelluslogiikkaa.

### HUOM! 
Sisään voi kirjautua joko luomalla uuden käyttäjän tai testikäyttäjänä

tunnus: testi

salasana: 0000

Ohjelman käynnistyessä ensimmäistä kertaa päänäkymässä ei näy reittejä, ennen kuin niitä on lisätty tietokantaan. 

### Dokumentaatio

[Käyttöohje](https://github.com/Jiisala/ot_harjoitustyo/blob/main/Dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/Jiisala/ot_harjoitustyo/tree/main/Dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Jiisala/ot_harjoitustyo/blob/main/Dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/Jiisala/ot_harjoitustyo/blob/main/Dokumentaatio/arkkitehtuuri.md)

### Asennus
- lataa sovelluksen uusin release:
  [Release](https://github.com/Jiisala/ot_harjoitustyo/releases/tag/Viikko5)

- Asenna tarvittavat riippuvuudet komennolla:
```bash
poetry install
```
- Alusta tietokannat komennolla (ennen ensimmäistä käynnistystä tai jos haluat tyhjentää tietokannat)
```bash
poetry run invoke dbinit
```
- Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```
### Komentorivitoiminnot

- Käynnistys:
```bash
poetry run invoke start
```
- testaus:
```bash
poetry run invoke tests
```
- testikattavuusraportti:
```bash
poetry run coverage-report
```
Raportti tulostetaan konsoliin, sekä kansioon /htmlcov 
