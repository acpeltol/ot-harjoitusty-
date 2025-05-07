# Miinaharava

Miinaharava on klassikkopeli vielä 80-luvulta. Tässä projektissa pääsette pelaamaan uutta miinaharavan implementaatiota samoilla vanhoilla tominnalliskuuksilla.

## Releaset

* [Realease Viikko5](https://github.com/acpeltol/ot-harjoitusty-/releases/tag/Viikko5)

* [Realease Viikko6](https://github.com/acpeltol/ot-harjoitusty-/releases/tag/Viikko6)
* [Realease Viikko7](https://github.com/acpeltol/ot-harjoitusty-/releases/tag/Viikko7)

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/vaatimusmaarittely.md)

* [Työaikakirjanpito](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/ty%C3%B6aikakirjanpito.md)
* [Käyttöohje](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)
  
* [Changelog](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/changelog.md)
* [Arkkitehtuurikuvaus](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/arkkitehtuurikuvaus.md)
* [Testikattavuus](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/testi.md)
* [Tekoälyn käyttö](https://github.com/acpeltol/ot-harjoitusty-/blob/main/miinaharava/dokumentaatio/teko%C3%A4lyk%C3%A4ytt%C3%B6.md)

## Asennus 

1. Siirry miinaharava hakemistoon ja asenna riippuvuudet komennolla:

poetry Install

2. Suoria vaaditavat alustustoimet komennolla:

poetry run invoke build

3. Käyistä sovellus:

poetry run invoke start

## Komentorivitoiminnot

Kaikki komennot suoritetaan miinaharava hakemistossa!

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
