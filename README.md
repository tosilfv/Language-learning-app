# Language Learning App

## Video

![Video](video_3.gif)

## Description

This is a [tkinter](https://docs.python.org/3/library/tkinter.html) app.<br />
You can use the app to learn foreign words.<br />

## Background

Program is developed with VSCode and written in Python.<br />
Install VSCode, Python 3.13.5 and required libraries.<br />
Run main.py from the root folder to start the program.<br />

## Instructions

Start by selecting a JSON file using the Eject Button (Top Left).<br />
A starting file is included in the files folder.<br />

Word (Top Center):<br />
Shows word from the language file dictionary.<br />

User Input Field (Bottom Center):<br />
Here you can type the translation of the Word.<br />

Eject Button (Top Left):<br />
Opens a language file of JSON type.<br />

Play Button (Bottom Right):<br />
Shows next word.<br />

Random Button (Top Right):<br />
Shows random word.<br />

Stop Button (Bottom Left):<br />
Holds current word.<br />

## Ohjeet

Aloita avaamalla kielitiedosto Avaa-painikkeella (Ylhäällä vasemmalla).<br />

Sana (Ylhäällä keskellä):<br />
Näyttää sanan kielitiedoston sisältämästä sanakirjasta.<br />

Syötekenttä (Alhaalla keskellä):<br />
Tänne voit kirjoittaa käännöksen.<br />

Avaa-painike (Ylhäällä vasemmalla):<br />
Avaa JSON-tyyppisen kielitiedoston.<br />

Seuraava-painike (Alhaalla oikealla):<br />
Näyttää seuraavan sanan.<br />

Satunnainen-painike (Ylhäällä oikealla):<br />
Näyttää satunnaisen sanan.<br />

Pysäytä-painike (Alhaalla vasemmalla):<br />
Pysyy kyseisessä sanassa.<br />

## N.B.

The language file should be a JSON dictionary of *.txt type.<br />
Enter key press will activate Play button.<br />
Stop button will turn to DISABLED after click and to NORMAL after<br />
Eject, Play or Random button click.<br />
Do not leave a trailing comma to the last key value pair of the language<br />
file, as this would not be valid JSON.<br />

## Testing

You can run [mypy](https://www.mypy-lang.org/) type check tests from<br />
root folder in the terminal with:<br />
mypy .\main.py<br />
mypy .\utils\helpers.py <br />

## Changelog

**[v0.0.1] - Oct 6. 2025:**<br />
_- Completed application core functions._<br />

**[v1.0.0] - Oct 10. 2025:**<br />
_- Initial release._<br />
