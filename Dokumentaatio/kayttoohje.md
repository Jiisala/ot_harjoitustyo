# Käyttöohje

Ladattuasi projektin uusimman releasen koneellesi:

## Konfigurointi 

Mikäli tietokannan nimi ei miellytä sinua voit muuttaa sitä editoimalla projektin juurihakemistossa sijaitsevaa .env tiedostoa.

## Ohjelman käynnistäminen

Ennen ensimmäistä käynnistystä suorita projektin juurihakemistossa komento: 

```bash
poetry install
```
Tämä asentaa tarvittavat riippuvuudet

Sen jälkeen alusta tietokanta komennolla:

```bash
poetry run invoke dbinit
```
Jos myöhemmin haluat tyhjentää tietokannat aja sama komento uudelleen

Käynnistä ohjelma komennolla:

```
poetry run invoke start
```

## Käyttäminen

Sovellus käynnistyy kirjautumisnäkymään, kirjaudu syöttämällä olemassa oleva käyttäjänimi ja siihen kuuluva salasana ja painamalla sign in nappia.
Voit myös luoda uuden käyttäjän siirtymällä uuden käyttäjän luomis näkymään, painamalla create new user nappia.
Uuden käyttäjän luodaksesi anna käyttäjänimi ja salasana, käyttäjänimen on oltava ohjelmassa uniikki. Mikäli nimi on jo käytössä keksi uusi ja omaperäisempi nimi.
Luotuasi uuden käyttäjän ohjelma kirjaa sinut sisään automaattisesti.

Päänäkymässä näet itsellesi tagaamasi reitit, tai mikäli niitä ei ole tyhjän näkymän jossa on muutama nappi.
Uuden reitin pääset lisäämään painamalla New problem nappia. Uusi reitti lisätään omassa näkymässään. Lisää reitisä tiedot joita näkymässä pyydetään ja paina Create nappia. Uusi reitti luodaan ja lisätään automaattisesti listallesi kiipeämättömänä.
Kaikkien käyttäjien lisäämiä reittejä, mikäli niitä on, pääset tarkastelemaan päänäkymän Browse problems-nappia paimalla. 
Reittien tarkastelu aukeaa myös omaan näkymäänsä, painamalla tässä näkymässä tag/untag nappia lisätään reitti omalle listallesi, tai poistetaan sieltä.
Päänäkymässä nappi Solved/unsolved merkitsee reitin kiivetyksi tai poistaa merkinnän.
Sekä päänäkymässä että ongelmien selaus näkymässä on valikko josta voi valita järjestelyperusteen. order ^ / order v-nappi vaihtaa järjestyksen joko nousevaksi tai laskevaksi. 
Sign out nappi palauttaa sinut sisäänkirjautumis ruutuun.


