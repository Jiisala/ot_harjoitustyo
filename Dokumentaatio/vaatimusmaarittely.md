# Vaatimusmäärittely

# Boulder Pal 9000

Sovellus on tarkoitettu kiivettyjen kiipeilyreittien kirjaamiseen. Sovellukseen voi myös listata valmiiksi reittejä jotka aikoo kiivetä tulevaisuudessa. Sovellus on tarkoitettu pääasiallisesti yhden ihmisen käyttöön, mutta siinä on joitakin ominaisuuksia jotka hyödyntävät myös useiden käyttäjien yhteistyötä. 

## Käyttäjät
Sovellukseen voi luoda useampia käyttäjiä. Käyttäjät voivat selata sovellukseen jo lisättyjä reittejä ja lisätä niitä omalle listalleen, mutta eivät saa tietoa siitä, onko joku toinen käyttäjä jo kiivennyt kyseisen reitin. 

## Käyttöliittymä

Sovelluksen käynnistyessä aukeaa kirjautumisnäkymä, siitä on mahdollista siirtyä käyttäjä luomiseen. Kirjautumisen jälkeen siirrytään käyttäjän omalle etusivulle. Etusivulla on listattu käyttäjän valitsemat reitit. Reittien lisääminen ja kaikkien käyttäjien lisäämien reittien selaaminen toimivat omissa näkymissään.

## Toiminnallisuus 

### Ohjelman käynnistyessä 

*  voidaan joko luoda uusi käyttäjä tai kirjautua sisään jo olemassa olevalle tilille. 

### Sisäänkirjautumisen jälkeen

* Näkymässä näkyvät reitit näkyvät käyttäjän valitsemat reitit, oletusarvoisesti järjestettynä nimen mukaan, kiipeämättömät reitit ensin.
  * järjestyksen voi halutessaan muuttaa myös niin että reitit järjestetään vaikeuden, lisääjän käyttäjänimen tai sijainnin mukaan.
  * jarjestyksen voi halutessaan kääntää laskevasti.


* voidaan vaihtaa näkymä näyttämään kaikki sovllukseen lisätyt reitit
  * samat järjestystoiminnot toimivat täälläkin

*  Näkymässä on nappi josta voidaan lisätä uusi reitti
  * reitin tiedot kysytään omassa ikkunassaan
   

#### Lisätystä reitistä tallennetaan: 

* lisääjän käyttäjänimi 
* reitin  nimi
* vaikeusaste 
  * käytetään boulderointiin sopivaa merkintätapaa joka alkaa numerosta 4 ja vaikeutuessaan kasvaa. 
  * Numeron perään voidaan lisätä kirjain a, b, tai c, ja sen jälkeen + tai -
* kuva reitistä
*  sijainti (vapaa tekstikenttä, ajankäytöllisistä syistä)
*  lyhyt kuvaus
 
 
## Ohjelmaan jääneet puutteet, sisältäen hieman itsereflektiota

* Käyttöliittymä on erittäin epäesteettinen, esteellinen ja kaipaisi paljon työstöä. Tämän kurssin puitteissa se on kuitenkin käsittääkseni riittävä ja ajankäytöllisistä syistä päätin jättää sen kuten se on. 
* Ohjelman tietoturva on myös retuperällä, esimerkiksi salasanat tallennetaan salaamattomana tekstinä avoimeen tietokantaan.
* Kuvien käsittelyn voisi refaktoroida omaksi luokakseen, nyt se tapahtuu mielestäni heieman kömpelösti sovelluslogiikka luokassa, ketjutetuissa funktioissa. 
Aikataulusyistä myös tämä jää tuonnemmaksi.
* Käyttöliittymässä, on useissa luokissa runsaasti toisteista koodia, tämän ongelman voisis varmasti korvata.
* Lisäksi näkymien luomisesta vastaavissa luokissa on järjestämiseen liittyvää toiminnallisuutta jonka voisi siirtää myös sovelluslogiikkaan. Annoin asian olla koska sitä käytetään hieman erilailla eri näkymissä ja sen siirtäminen olisi vaatinut enemmän refaktorointia, kuin koin järkeväksi sen eteen tehdä.
* Täysikokoisteh kuvien näyttämiseen käytetään järjestelmän oletusohjelmaa. Mikäli käyttöliittymän päivitys tapahtuu joskus, tämä toiminnallisuus siirtynee ohjelman sisäiseksi toteutukseksi.
* Repositorioluokat Problems ja Users olisi voinut nimetä paremmin, kuten myös vertaisarvioija huomautti. Luokkia nimetessäni ne tuntuivat järkeviltä, olen sittemmin tullut toisiin aatoksiin, mutta en rohkene enää projektin tässä vaiheessa muuttaa niitä.

## Mahdollisia laajennusideoita 

* käyttäjätietojen hallinta
  * käyttäjä voi esim. vaihtaa nimensä ja salasanansa 
* reitin poistaminen
  * reitin voi poistaa vain sama käyttäjä joka sen on lisännytkin
  * reittiä ei voi enää lisätä omaan näkymäänsä ja se poistuu kaikki reitit listaavasta näkymästä. 
  * Poistettu reitti jää näkymään käyttäjille jotka ovat jo lisänneet sen omaan näkymäänsä, mutta siinä on merkintä poistumisesta.
* Karttalinkin lisääminen reitin sijainnin tallenntamiseksi, vapaan tekstikentän rinnalle
* Toiminto joka niputtaa lähekkäin olevat reitit yhteen
* sosiaaliset toiminnot, kuten reitin suositteleminen toiselle käyttäjälle, reitteihin lisätyt kommentit ja mahdollisuus lisätä omat saavutukset julkisiksi.
 
