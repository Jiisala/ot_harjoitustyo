# Ohjelmistotekniikka, harjoitustyö

## Boulder Pall 9000
Boulder Pall 9000 on sovellus jonka avulla käyttäjä voi pitää kirjaa kiipeilyreiteiteistä joita on jo kiivennyt,tai aikoo kiivetä.
Tämän hetkinen versio on vielä huomattavan keskeneräinen ja sisältää käytännössä vasta uuden käyttäjän luomisen ja sisäänkirjautumisen.
Sisäänkirjautuminen ei tarkista vielä oikeasti käyttäjänimeä, eikä päänäkymässä ole mitään järkevää näkemistä/toimintaa. Uuden käyttäjän luominen luo uuden käyttäjän ja lisää sen käyttäjiä ylläpitävän luokan sisäiseen listaan. Myöhemmässä vaiheessa lista korvautuu järkevämmällä tietokantarakenteella (SQL). Testikattavuus on toistaiseksi heikko, ohjelmassa on yksi testi joka testaa että uusi käyttäjä todellakin lisätään listalle.

### Dokumentaatio

Käyttöohje (tulossa)

[Vaatimusmäärittely](https://github.com/Jiisala/ot_harjoitustyo/tree/main/Dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Jiisala/ot_harjoitustyo/blob/main/Dokumentaatio/tuntikirjanpito.md)

### Asennus

- Asenna tarvittavat riippuvuudet komennolla:
```bash
poetry install
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
