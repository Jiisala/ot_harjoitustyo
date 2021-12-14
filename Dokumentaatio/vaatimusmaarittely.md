# Vaatimusmäärittely

# Boulder Pal 9000

Sovellus on tarkoitettu kiivettyjen kiipeilyreittien kirjaamiseen. Sovellukseen voi myös listata valmiiksi reittejä jotka aikoo kiivetä tulevaisuudessa. Sovellus on tarkoitettu pääasiallisesti yhden ihmisen käyttöön, mutta siinä on joitakin ominaisuuksia jotka hyödyntävät myös useiden käyttäjien yhteistyötä. 

## Käyttäjät
Sovellukseen voi luoda useampia käyttäjiä. Käyttäjät voivat selata sovellukseen jo lisättyjä reittejä ja lisätä niitä omalle listalleen, mutta eivät saa tietoa siitä, onko joku toinen käyttäjä jo kiivennyt kyseisen reitin. 

## Käyttöliittymä

Sovelluksen käynnistyessä aukeaa kirjautumisnäkymä, siitä on mahdollista siirtyä käyttäjä luomiseen. Kirjautumisen jälkeen siirrytään käyttäjän omalle etusivulle. Oletusnäkymänä on listatut, mutta kiipeämättömät reitit. Kiivettyjen reittien listaaminen, reittien yksityikohtien tutkiminen ja reittien lisääminen toimivat omissa näkymissään.

## Toiminnallisuus 

### Ohjelman käynnistyessä 

*  voidaan joko luoda uusi käyttäjä tai kirjautua sisään jo olemassa olevalle tilille. 

### Sisäänkirjautumisen jälkeen

* [x] Näkymässä näkyvät reitit näkyvät oletusarvoisesti kiipeämättömät reitit lisäyspäivän mukaan järjestettyinä (uusin ylimpänä.
  * [x] järjestyksen voi halutessaan muuttaa myös niin että reitit järjestetään vaikeudenm tai nimen mukaan.
  * [x] jarjestyksen voi halutessaan kääntää laskevasti.

*  Voidaan vaihtaa näkymä näyttämään jo kiivetyt reitit
  * [x] samat järjestystoiminnot toimivat yhä

* voidaan vaihtaa näkymä näyttämään sovllukseen lisätyt mutta omalta listalta puuttuvat reitit
  * [x] samat järjestystoiminnot toimivat täälläkin

*  Näkymässä on nappi josta voidaan lisätä uusi reitti
  * reitin tiedot kysytään omassa ikkunassaan
   

#### Lisätystä reitistä tallennetaan ainakin: 

* lisääjän käyttäjänimi 
* reitin  nimi
* vaikeusaste 
  * käytetään boulderointiin sopivaa merkintätapaa joka alkaa numerosta 4 ja vaikeutuessaan kasvaa. 
  * Numeron perään voidaan lisätä kirjain a, b, tai c, ja sen jälkeen + tai -
* [ ] kuva reitistä
*  sijainti (vapaa tekstikenttä, ajankäytöllisistä syistä)
*  lyhyt kuvaus
 
 
## Mahdollisia laajennusideoita jos jää aikaa

* käyttäjätietojen hallinta
  * käyttäjä voi esim. vaihtaa nimensä ja salasanansa 
* reitin poistaminen
  * reitin voi poistaa vain sama käyttäjä joka sen on lisännytkin
  * reittiä ei voi enää lisätä omaan näkymäänsä ja se poistuu kaikki reitit listaavasta näkymästä. 
  * Poistettu reitti jää näkymään käyttäjille jotka ovat jo lisänneet sen omaan näkymäänsä, mutta siinä on merkintä poistumisesta.
* Karttalinkin lisääminen reitin sijainnin tallenntamiseksi, vapaan tekstikentän rinnalle
* Toiminto joka niputtaa lähekkäin olevat reitit yhteen
* sosiaaliset toiminnot, kuten reitin suositteleminen toiselle käyttäjälle, reitteihin lisätyt kommentit ja mahdollisuus lisätä omat saavutukset julkisiksi.
 
