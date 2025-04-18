# Miinaharava

Miinaharava on klassikkopeli vielä 80-luvulta. Tässä projektissa pääsette pelaamaan uutta miinaharavan implementaatiota samoilla vanhoilla tominnalliskuuksilla.

## Viimeinen realease

* [Realease](https://github.com/acpeltol/ot-harjoitusty-/releases/tag/Viikko5)

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/vaatimusmaarittely.md)

* [Työaikakirjanpito](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/ty%C3%B6aikakirjanpito.md)
  
* [Changelog](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/changelog.md)
* [Arkkitehtuurikuvaus](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/arkkitehtuurikuvaus.md)

## Asennus 

1. Asenna riippuvuudet komennolla:

poetry Install

2. Suoria vaaditavat alustustoimet komennolla:

poetry run invoke build

3. Käyistä sovellus:

poetry run invoke start

## Komentorivitoiminnot

### Suoritus

Ohjelma suoritetaan komennolla:

poetry run invoke start

### Testaus

Ohjelmaa testataan komennolla:

poetry run invoke test

### Testikattavuus

Testikattavuus saadaan komennolla:

poetry run invoke coverage-report

### pylint

Saadaan pylint koodinlaatu komennolla:

poetry run invoke lint
