## Monopoli, alustava luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Pelilauta "1" -- Vankila
    Pelilauta "1" -- Aloitusruutu
    Ruutu "1" -- "1" Aloitusruutu
    Ruutu "1" -- "1" Vankila
    Ruutu "3" -- "1" Sattuma
    Ruutu "3" -- "1" Yhteismaa
    Ruutu "4" -- "1" Asema
    Ruutu "2" -- "1" Laitos
    Ruutu "22" -- "22" Katu : 
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula

    "
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
```