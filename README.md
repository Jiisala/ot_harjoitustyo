# Ohjelmistotekniikka, harjoitustyö

## Boulder Pall 9000
 Boulder Pall 9000 on sovellus jonka avulla käyttäjä voi pitää kirjaa kiipeilyreiteiteistä (ohjelma käyttää englannin kielistä termiä "problem"), joita on jo kiivennyt,tai aikoo kiivetä.

 Tämän hetkinen versio on vielä keskeneräinen. Sisäänkirjautumisen (tai uuden käyttäjän luomisen) jälkeen aukeaa päänäkymä, joka on ihastuttavan epäestetttinen. Päänäkymässä näkyy, tervehdys käyttäjälle, kaikki tietokantaan lisätyt reitit ja kaksi nappia. Toisesta pääsee lisämään uuden reitin (oma näkymänsä) ja toisesta ei tapahdu mitään.

 Uuden käyttäjän luominen käyttäjäm ohjelman tiedontallennuksesta huolehtivaan tietokantaan. Uuden reitin luominen lisää sen tietokantaan, lisäksi juuri luotu ongelma ilmestyy näkyviin päänäkymään. Ohjelma tarkistaa sekä käyttäjää että ongelmaa luodessa että nimi on uniikki, eikä luo uutta mikäli saman niminen on jo olemassa. Tästä ei käyttäjä toistaiseksi saa mitäään palautetta. Reitille kuvan lisääminen ei myöskään vielä toimi, vaan sen virkaa toimittaa "placeholder" tekstikenttä.
 
 Lisätyt ongelmat lisätään myös uxb nimiseen tietokantaan jossa säilytetään tietoa siitä mitä reittejä käyttäjä on lisännyt itselleen ja onko ne jo merkitty kiivetyiksi. Tähän tietokantaan liittyvä toiminnallisuus kuitenkin vielä puuttuu. 
 
 Testikattavuus on kohtalainen, testit testaavat reitin ja käyttäjän luomisesta huolehtivia luokkia, varsinaista sovelluslogiikka-luokkaa ei vielä testata.

### HUOM! 
Sisään voi kirjautua joko luomalla uuden käyttäjän tai testikäyttäjänä

tunnus: testaaja

salasana: 0000

Ohjelman käynnistyessä ensimmäistä kertaa päänäkymässä ei näy reittejä, ennen kuin niitä on lisätty tietokantaan. 

### Dokumentaatio

Käyttöohje (tulossa)

[Vaatimusmäärittely](https://github.com/Jiisala/ot_harjoitustyo/tree/main/Dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Jiisala/ot_harjoitustyo/blob/main/Dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/Jiisala/ot_harjoitustyo/blob/main/Dokumentaatio/arkkitehtuuri.md)

### Asennus

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
