#!/usr/bin/env python3
"""
Math Exercise Generator for 8th Grade (Realschule)
Generates geometry exercises (area, perimeter, linear equations) as PDF
Uses Typst for professional mathematical typesetting
With geometric sketches (CeTZ)
"""

import json
import random
import subprocess
import sys
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Annotated, Optional

import typer
import typst

app = typer.Typer(
    help="Generiert Mathematik-Übungsaufgaben für die 8. Klasse als PDF",
    invoke_without_command=True,
    no_args_is_help=False,
)


class ExerciseType(str, Enum):
    """Available exercise types."""
    rechteck_flaeche = "rechteck-flaeche"
    rechteck_umfang = "rechteck-umfang"
    rechteck_umstellung = "rechteck-umstellung"
    quadrat_flaeche = "quadrat-flaeche"
    quadrat_umfang = "quadrat-umfang"
    quadrat_umstellung = "quadrat-umstellung"
    dreieck_flaeche = "dreieck-flaeche"
    dreieck_umfang = "dreieck-umfang"
    dreieck_umstellung = "dreieck-umstellung"
    parallelogramm_flaeche = "parallelogramm-flaeche"
    parallelogramm_umfang = "parallelogramm-umfang"
    parallelogramm_umstellung = "parallelogramm-umstellung"
    tabelle_rechteck = "tabelle-rechteck"
    tabelle_quadrat = "tabelle-quadrat"
    tabelle_dreieck = "tabelle-dreieck"
    tabelle_parallelogramm = "tabelle-parallelogramm"
    koordinaten_rechteck = "koordinaten-rechteck"
    koordinaten_quadrat = "koordinaten-quadrat"
    koordinaten_dreieck = "koordinaten-dreieck"
    koordinaten_parallelogramm = "koordinaten-parallelogramm"
    textaufgabe = "textaufgabe"

PROMPT = r"""Du bist ein Mathematiklehrer für die 8. Klasse Realschule.
Erstelle genau 10 Mathematik-Aufgaben zum Thema Geometrie.

Die Aufgaben sollen folgende Bereiche abdecken:
1. Flächenberechnung von Dreiecken, Quadraten, Rechtecken und Parallelogrammen
2. Umfangberechnung dieser Figuren
3. Umstellen von Formeln (z.B. gegeben: Fläche A und Höhe h, gesucht: Grundseite a)
4. TABELLENAUFGABE (Aufgabe 8): Fehlende Größen in einer Tabelle berechnen
5. KOORDINATENAUFGABE (Aufgabe 9): Figur im Koordinatensystem einzeichnen und berechnen

Anforderungen:
- KRITISCH - ZUFÄLLIGE ZAHLEN: Jede Aufgabe braucht KOMPLETT ANDERE Zahlen!
  * Würfle gedanklich für jede Aufgabe NEUE Zahlen aus!
  * NIEMALS dieselben Zahlenkombinationen wie in den Beispielen verwenden!
  * Nutze die VOLLE Bandbreite: 3, 7, 9, 11, 13, 14, 17, 19, 21, 23, 27, 31, 35, 42, 48, 53, 67, 78, 85, 93, 120, 145, 180, 225, 340
  * Mische: kleine (3-15), mittlere (16-50), große (51-200) Zahlen
  * Mische: gerade UND ungerade Zahlen
  * Bei Dezimalzahlen: 2,5 / 3,7 / 4,8 / 6,3 / 7,2 / 8,5 usw.
  * VERMEIDE: 4, 5, 6, 8, 10, 12, 20, 100 - diese sind zu häufig!
- Mische verschiedene Schwierigkeitsgrade
- Bei Umstellungsaufgaben: Gib zwei Werte vor und lass den dritten berechnen
- Verwende verschiedene Einheiten (cm, m, mm) - aber abwechselnd, nicht immer dieselbe!
- WICHTIG: Vermeide Aufgaben, bei denen Wurzeln (sqrt) zur Lösung benötigt werden!
  * NICHT: Gegeben A bei Quadrat, gesucht a (da a = sqrt(A) Wurzel erfordert)
  * Stattdessen: Gegeben a, gesucht A oder U (keine Wurzel nötig)
  * KEINE Aufgaben mit Pythagoras oder Diagonalberechnungen!
  * Alle Lösungen sollen nur Grundrechenarten (Addition, Subtraktion, Multiplikation, Division) erfordern

- WICHTIG: Aufgabe 8 muss eine TABELLENAUFGABE sein (typ="tabelle"):
  - Eine Tabelle mit 4 Zeilen (4 verschiedene Figuren desselben Typs, z.B. 4 Rechtecke)
  - VERSCHIEDENE EINHEITEN pro Zeile mischen (cm, m, mm)! NIEMALS dm verwenden!
  - Spalten je nach Figur: Rechteck (a, b, U, A), Dreieck (g, h, A), Quadrat (a, U, A)
  - Manche Werte gegeben, andere mit "?" markiert - der Schüler berechnet die fehlenden
  - "tabelle" enthält: "spalten", "zeilen" (mit "?"), "loesungen" (alle Werte ausgefüllt)
  - "loesung" enthält ausführliche Berechnung für JEDE Zeile

- WICHTIG: Aufgabe 9 muss eine KOORDINATENAUFGABE sein (typ="koordinaten"):
  - Der Schüler soll eine Figur (Rechteck, Quadrat, Dreieck oder Parallelogramm) im Koordinatensystem einzeichnen
  - Punkte werden als Koordinaten vorgegeben: A(x|y), B(x|y), C(x|y), ...
  - KRITISCH: Wähle ZUFÄLLIGE Koordinaten! NICHT immer dieselben wie im Beispiel!
  - Variiere: Startpunkt (nicht immer bei 1|1), Größe der Figur, Position im Koordinatensystem
  - GANZZAHLIGE Koordinaten zwischen 1 und 10 verwenden!
  - Die Figur soll gut lesbar sein: Seitenlängen mindestens 3, maximal 8 Einheiten
  - max_x und max_y: Wähle passend zur Figur (2-3 Einheiten größer als größte Koordinate), MAXIMAL 10!
  - Nach dem Einzeichnen: Berechne Seitenlängen, Umfang und/oder Fläche
  - "koordinaten" enthält: "punkte" (Liste mit name, x, y), "max_x", "max_y", "gesucht" (was berechnet werden soll)
  - Im Koordinatensystem gilt: 1 Einheit = 1 cm

- WICHTIG: Genau EINE Aufgabe (Aufgabe 10) muss eine umfangreiche Textaufgabe/Sachaufgabe sein!
  Diese Textaufgabe soll:
  - Eine KREATIVE und EINZIGARTIGE Alltagssituation beschreiben
  - NICHT immer Garten/Zaun! Wähle zufällig aus: Teppich verlegen, Bilderrahmen bauen,
    Tapete kleben, Teich anlegen, Sonnensegel spannen, Pflastersteine legen,
    Sandkasten bauen, Gewächshaus planen, Carport-Dach berechnen, Markise kaufen,
    Tischtuch nähen, Poster drucken, Fliesen im Bad, Parkett verlegen, Wandfarbe kaufen
  - Mehrere Rechenschritte erfordern
  - Die geometrischen Formeln im Kontext anwenden
  - 3-5 Sätze lang sein
  - Konkrete, interessante Details enthalten (Namen, Orte, Preise)

WICHTIG - Jede Aufgabe braucht Angaben für die Skizze:
- "figur": Eine von "rechteck", "quadrat", "dreieck", "dreieck_umfang", "parallelogramm"
- "skizze": Ein Objekt mit den Werten für die Skizze.
  WICHTIG: Zeige IMMER was gesucht wird mit "?"!

  Bei FLÄCHENBERECHNUNG (figur ohne _umfang):
  - Rechteck: {"a": "5 cm", "b": "3 cm", "A": "?"} - A=? weil Fläche gesucht
  - Quadrat: {"a": "4 cm", "A": "?"} - A=? weil Fläche gesucht
  - Dreieck: {"g": "6 cm", "h": "4 cm", "A": "?"} - mit Grundseite g und Höhe h
  - Parallelogramm: {"a": "7 cm", "h": "3 cm", "A": "?"} - mit Seite a und Höhe h

  Bei UMFANGBERECHNUNG (figur mit _umfang):
  - Rechteck: {"a": "5 cm", "b": "3 cm", "U": "?"} - U=? weil Umfang gesucht
  - Quadrat: {"a": "4 cm", "U": "?"} - U=? weil Umfang gesucht
  - Dreieck (figur="dreieck_umfang"): {"a": "5 cm", "b": "4 cm", "c": "3 cm", "U": "?"} - mit allen 3 Seiten!
  - Parallelogramm: {"a": "7 cm", "b": "4 cm", "U": "?"} - mit beiden Seitenlängen

  Bei FORMELUMSTELLUNG:
  - Zeige die gegebenen Werte UND den gesuchten Wert mit "?"
  - Rechteck: {"a": "?", "b": "3 cm", "A": "15 cm²"} - a=? weil Seite gesucht
  - Dreieck: {"g": "8 cm", "h": "?", "A": "24 cm²"} - h=? weil Höhe gesucht

WICHTIG - Formatierung der Lösungen in Typst-Math-Syntax:
- Schreibe jeden Rechenschritt auf eine eigene Zeile, getrennt durch " || "
- JEDER Schritt besteht aus: FORMEL // ERKLÄRUNG (getrennt durch " // ")

KRITISCH - SEHR AUSFÜHRLICHE ERKLÄRUNGEN (wie ein geduldiger Nachhilfelehrer):
- Gehe davon aus, dass das Kind große Schwierigkeiten in Mathe hat und JEDES Detail erklärt braucht!
- Jede Erklärung MUSS 3-5 vollständige Sätze haben - NIEMALS kürzer!
- Erkläre bei JEDEM Schritt:
  1. WAS machen wir? (z.B. "Jetzt setzen wir die Zahlen ein")
  2. WARUM machen wir das? (z.B. "Das ist nötig, weil wir die Formel mit konkreten Werten ausrechnen wollen")
  3. WIE geht das genau? (z.B. "Wir ersetzen den Buchstaben a durch die Zahl 7")
  4. Was bedeutet das ERGEBNIS? (z.B. "Das bedeutet, die Seite ist 7 cm lang")

BEISPIELE für SCHLECHTE Erklärungen (ZU KURZ!):
- "Werte einsetzen" ❌
- "Formel umstellen" ❌
- "Ausrechnen" ❌
- "Ergebnis" ❌

BEISPIELE für GUTE Erklärungen (SO SOLL ES SEIN!):
- "Jetzt setzen wir unsere bekannten Werte in die Formel ein. Das bedeutet, wir ersetzen jeden Buchstaben durch die Zahl, die wir kennen. Hier ersetzen wir a durch 7 cm und b durch 5 cm. Danach können wir ganz normal ausrechnen."
- "Um die Höhe h zu finden, müssen wir die Formel umstellen. Das Ziel ist, dass h alleine auf einer Seite steht. Dazu teilen wir beide Seiten der Gleichung durch g. Was wir auf einer Seite machen, müssen wir auch auf der anderen Seite machen - so bleibt die Gleichung richtig."
- "Jetzt multiplizieren wir 7 mal 5. Das Ergebnis ist 35. Bei den Einheiten rechnen wir cm mal cm, das ergibt cm² (Quadratzentimeter). Quadratzentimeter ist die Einheit für Flächen."

- Benutze ermutigende Sprache: "Das schaffst du!", "Schritt für Schritt!", "Nicht so schwer!"
- Verwende Typst-Math-Syntax für Formeln:
  - Brüche: (Zähler) / (Nenner) - IMMER mit Klammern!
  - Multiplikation: dot (z.B. 5 dot 8)
  - Quadrat: ^2 (z.B. "cm"^2)
  - Quadratwurzel: sqrt(x)
  - Einheiten in Anführungszeichen: "cm", "m", "mm"

KRITISCH - ALLE Zwischenschritte zeigen:
- Bei Umformungen JEDEN Schritt erklären, wie man darauf kommt!
- Beispiel FALSCH: "A = a · b || b = A/a" - hier fehlt der Zwischenschritt!
- Beispiel RICHTIG: "A = a dot b // Die Formel für die Rechtecksfläche || A / a = b // Um b zu finden, teilen wir beide Seiten durch a || b = (35 \"cm\"^2) / (7 \"cm\") // Wir setzen A = 35 cm² und a = 7 cm ein || b = 5 \"cm\" // 35 geteilt durch 7 ergibt 5"
- Jede mathematische Operation (durch etwas teilen, mal 2 nehmen, addieren) braucht eine eigene Zeile mit Erklärung!

KRITISCH für Brüche mit Einheiten (wie im Mathebuch):
- Bei Division IMMER Zahl UND Einheit zusammen in Zähler und Nenner
- RICHTIG: (48 "cm"^2) / (8 "cm") = 6 "cm"
- FALSCH: 48 "cm"^2 / 8 "cm"
- Die Klammern sind wichtig damit Typst den Bruch korrekt setzt!

KRITISCH - AUSGABEFORMAT:
- Antworte mit NICHTS außer dem JSON-Objekt
- KEIN einleitender Text wie "Ich erstelle..." oder "Hier sind..."
- KEIN erklärender Text vor oder nach dem JSON
- KEINE Markdown-Codeblöcke (```)
- Beginne DIREKT mit dem öffnenden {

{
  "aufgaben": [
    {
      "nummer": 1,
      "typ": "standard",
      "aufgabe": "Ein Dreieck hat eine Fläche von 24 cm² und eine Grundseite von 8 cm. Berechne die Höhe h.",
      "figur": "dreieck",
      "skizze": {"g": "8 cm", "h": "?", "A": "24 cm²"},
      "erklaerung": "Wir kennen A = 24 cm² und g = 8 cm. Gesucht ist h. Die Formel lautet: A = ½ · g · h. Wir stellen nach h um.",
      "loesung": "A = (1/2) dot g dot h // Das ist die Formel für die Dreiecksfläche. Die Fläche A berechnet sich aus der Grundseite g mal die Höhe h, geteilt durch 2. || 2 dot A = g dot h // Um die Formel nach h umzustellen, multiplizieren wir zuerst beide Seiten mit 2. So verschwindet der Bruch und wir haben 2·A auf der linken Seite. || h = (2 dot A) / g // Jetzt teilen wir beide Seiten durch g, damit h alleine steht. Was wir auf einer Seite machen, müssen wir auch auf der anderen Seite machen! || h = (2 dot 24 \"cm\"^2) / (8 \"cm\") // Nun setzen wir unsere bekannten Werte ein: A ist 24 cm² und g ist 8 cm. Im Zähler steht 2 mal 24. || h = (48 \"cm\"^2) / (8 \"cm\") // 2 mal 24 ergibt 48. Jetzt müssen wir noch 48 durch 8 teilen. || h = 6 \"cm\" // 48 geteilt durch 8 ergibt 6. Die Höhe des Dreiecks beträgt also 6 cm!",
      "kategorie": "Dreieck - Formelumstellung"
    },
    {
      "nummer": 8,
      "typ": "tabelle",
      "aufgabe": "Berechne die fehlenden Größen der Rechtecke.",
      "figur": "rechteck",
      "tabelle": {
        "spalten": ["a", "b", "U", "A"],
        "zeilen": [
          {"a": "5 cm", "b": "3 cm", "U": "?", "A": "?"},
          {"a": "?", "b": "7 m", "U": "?", "A": "28 m²"},
          {"a": "12 mm", "b": "?", "U": "40 mm", "A": "?"},
          {"a": "?", "b": "?", "U": "24 cm", "A": "32 cm²"}
        ],
        "loesungen": [
          {"a": "5 cm", "b": "3 cm", "U": "16 cm", "A": "15 cm²"},
          {"a": "4 m", "b": "7 m", "U": "22 m", "A": "28 m²"},
          {"a": "12 mm", "b": "8 mm", "U": "40 mm", "A": "96 mm²"},
          {"a": "8 cm", "b": "4 cm", "U": "24 cm", "A": "32 cm²"}
        ]
      },
      "erklaerung": "Nutze die Formeln: A = a · b und U = 2·a + 2·b. Bei manchen Zeilen musst du umstellen!",
      "loesung": "\"Zeile 1:\" // Gegeben: a = 5 cm und b = 3 cm. Gesucht: Umfang U und Fläche A. || U = 2 dot 5 \"cm\" + 2 dot 3 \"cm\" = 16 \"cm\" // Der Umfang berechnet sich mit U = 2·a + 2·b. || A = 5 \"cm\" dot 3 \"cm\" = 15 \"cm\"^2 // Die Fläche ist a mal b. || \"Zeile 2:\" // Gegeben: b = 7 m und A = 28 m². Gesucht: a und U. || a = (28 \"m\"^2) / (7 \"m\") = 4 \"m\" // a aus der Flächenformel. || U = 2 dot 4 \"m\" + 2 dot 7 \"m\" = 22 \"m\" // Umfang berechnen.",
      "kategorie": "Rechteck - Tabelle"
    },
    {
      "nummer": 9,
      "typ": "koordinaten",
      "aufgabe": "Zeichne das Rechteck ABCD mit den Eckpunkten A(1|2), B(6|2), C(6|5) und D(1|5) in das Koordinatensystem ein. Berechne anschließend die Seitenlängen, den Umfang und die Fläche des Rechtecks. (1 Einheit = 1 cm)",
      "figur": "rechteck",
      "koordinaten": {
        "punkte": [
          {"name": "A", "x": 1, "y": 2},
          {"name": "B", "x": 6, "y": 2},
          {"name": "C", "x": 6, "y": 5},
          {"name": "D", "x": 1, "y": 5}
        ],
        "max_x": 8,
        "max_y": 7,
        "gesucht": ["a", "b", "U", "A"]
      },
      "erklaerung": "Zuerst zeichnen wir die vier Punkte A, B, C, D im Koordinatensystem ein und verbinden sie zu einem Rechteck. Dann lesen wir die Seitenlängen ab: Die Seite AB geht von x=1 bis x=6, also ist a = 6 - 1 = 5 cm. Die Seite AD geht von y=2 bis y=5, also ist b = 5 - 2 = 3 cm.",
      "loesung": "a = 6 - 1 = 5 \"cm\" // Die Seite AB (oder CD) geht von x=1 bis x=6. Die Länge ist die Differenz der x-Koordinaten: 6 minus 1 ergibt 5 cm. || b = 5 - 2 = 3 \"cm\" // Die Seite AD (oder BC) geht von y=2 bis y=5. Die Länge ist die Differenz der y-Koordinaten: 5 minus 2 ergibt 3 cm. || U = 2 dot a + 2 dot b // Jetzt berechnen wir den Umfang mit der Formel U = 2·a + 2·b. || U = 2 dot 5 \"cm\" + 2 dot 3 \"cm\" = 16 \"cm\" // Wir setzen ein: 2 mal 5 plus 2 mal 3 ergibt 10 plus 6 gleich 16 cm. || A = a dot b // Die Fläche berechnen wir mit A = a · b. || A = 5 \"cm\" dot 3 \"cm\" = 15 \"cm\"^2 // 5 mal 3 ergibt 15 Quadratzentimeter.",
      "kategorie": "Rechteck - Koordinaten"
    }
  ]
}

WICHTIG für "erklaerung" - Ausführlich erklären für Kinder die Schwierigkeiten haben:
- 4-6 Sätze die den Lösungsweg SEHR AUSFÜHRLICH beschreiben
- Gehe davon aus, dass das Kind schlecht in Mathe ist und viel Unterstützung braucht!
- Erkläre Schritt für Schritt was wir tun werden und WARUM
- Was ist gegeben? Was ist gesucht? (Wiederhole die Werte aus der Aufgabe)
- Welche Formel brauchen wir? Schreibe die Formel in Worten aus!
- Erkläre die Strategie: "Wir müssen die Formel umstellen..." / "Wir setzen die Werte ein..."
- Wenn wir umstellen: Erkläre welche Rechenoperation wir anwenden und warum
- Benutze einfache, ermutigende Sprache: "Das ist gar nicht so schwer!", "Schritt für Schritt schaffen wir das!"

Erstelle jetzt genau 10 verschiedene Aufgaben."""



def generate_random_seed_prompt() -> str:
    """Generate a random seed section to inject into prompts for variety."""
    # Generate random numbers from different ranges
    small = random.sample(range(3, 16), 5)
    medium = random.sample(range(17, 51), 5)
    large = random.sample(range(52, 200), 3)
    decimals = [round(random.uniform(2.0, 9.9), 1) for _ in range(4)]

    # Random coordinates for coordinate exercises
    coords = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(4)]

    # Random seed number
    seed = random.randint(10000, 99999)

    return f"""
ZUFALLS-SEED #{seed} - NUTZE DIESE ZAHLEN:
- Kleine Zahlen für diese Aufgabe: {small[0]}, {small[1]}, {small[2]}, {small[3]}, {small[4]}
- Mittlere Zahlen: {medium[0]}, {medium[1]}, {medium[2]}, {medium[3]}, {medium[4]}
- Große Zahlen: {large[0]}, {large[1]}, {large[2]}
- Dezimalzahlen: {decimals[0]}, {decimals[1]}, {decimals[2]}, {decimals[3]}
- Beispiel-Koordinaten: A({coords[0][0]}|{coords[0][1]}), B({coords[1][0]}|{coords[1][1]}), C({coords[2][0]}|{coords[2][1]}), D({coords[3][0]}|{coords[3][1]})
WICHTIG: Wähle Zahlen aus diesen Listen! NICHT die Beispielzahlen aus dem restlichen Prompt!
"""

def get_single_type_prompt(exercise_type: ExerciseType) -> str:
    """Generate a prompt for a single exercise of a specific type."""
    type_descriptions = {
        ExerciseType.rechteck_flaeche: ("Rechteck", "Flächenberechnung", "standard", "rechteck",
            "Berechne die Fläche eines Rechtecks. Gegeben sind Seite a und Seite b, gesucht ist A."),
        ExerciseType.rechteck_umfang: ("Rechteck", "Umfangberechnung", "standard", "rechteck",
            "Berechne den Umfang eines Rechtecks. Gegeben sind Seite a und Seite b, gesucht ist U."),
        ExerciseType.rechteck_umstellung: ("Rechteck", "Formelumstellung", "standard", "rechteck",
            "Berechne eine fehlende Seite eines Rechtecks. Gegeben sind Fläche A und eine Seite, gesucht ist die andere Seite."),
        ExerciseType.quadrat_flaeche: ("Quadrat", "Flächenberechnung", "standard", "quadrat",
            "Berechne die Fläche eines Quadrats. Gegeben ist Seite a, gesucht ist A."),
        ExerciseType.quadrat_umfang: ("Quadrat", "Umfangberechnung", "standard", "quadrat",
            "Berechne den Umfang eines Quadrats. Gegeben ist Seite a, gesucht ist U."),
        ExerciseType.quadrat_umstellung: ("Quadrat", "Formelumstellung", "standard", "quadrat",
            "Berechne die Seitenlänge eines Quadrats. Gegeben ist die Fläche A, gesucht ist a (Wurzel ziehen!)."),
        ExerciseType.dreieck_flaeche: ("Dreieck", "Flächenberechnung", "standard", "dreieck",
            "Berechne die Fläche eines Dreiecks. Gegeben sind Grundseite g und Höhe h, gesucht ist A."),
        ExerciseType.dreieck_umfang: ("Dreieck", "Umfangberechnung", "standard", "dreieck_umfang",
            "Berechne den Umfang eines Dreiecks. Gegeben sind alle drei Seiten a, b, c, gesucht ist U."),
        ExerciseType.dreieck_umstellung: ("Dreieck", "Formelumstellung", "standard", "dreieck",
            "Berechne eine fehlende Größe eines Dreiecks. Gegeben sind Fläche A und entweder g oder h, gesucht ist die andere."),
        ExerciseType.parallelogramm_flaeche: ("Parallelogramm", "Flächenberechnung", "standard", "parallelogramm",
            "Berechne die Fläche eines Parallelogramms. Gegeben sind Seite a und Höhe h, gesucht ist A."),
        ExerciseType.parallelogramm_umfang: ("Parallelogramm", "Umfangberechnung", "standard", "parallelogramm",
            "Berechne den Umfang eines Parallelogramms. Gegeben sind Seite a und Seite b, gesucht ist U."),
        ExerciseType.parallelogramm_umstellung: ("Parallelogramm", "Formelumstellung", "standard", "parallelogramm",
            "Berechne eine fehlende Größe eines Parallelogramms. Gegeben sind Fläche A und entweder a oder h."),
        ExerciseType.tabelle_rechteck: ("Rechteck", "Tabelle", "tabelle", "rechteck",
            "Erstelle eine Tabellenaufgabe mit 4 Rechtecken. Spalten: a, b, U, A. Verschiedene Einheiten pro Zeile!"),
        ExerciseType.tabelle_quadrat: ("Quadrat", "Tabelle", "tabelle", "quadrat",
            "Erstelle eine Tabellenaufgabe mit 4 Quadraten. Spalten: a, U, A. Verschiedene Einheiten pro Zeile!"),
        ExerciseType.tabelle_dreieck: ("Dreieck", "Tabelle", "tabelle", "dreieck",
            "Erstelle eine Tabellenaufgabe mit 4 Dreiecken. Spalten: g, h, A. Verschiedene Einheiten pro Zeile!"),
        ExerciseType.tabelle_parallelogramm: ("Parallelogramm", "Tabelle", "tabelle", "parallelogramm",
            "Erstelle eine Tabellenaufgabe mit 4 Parallelogrammen. Spalten: a, h, A. Verschiedene Einheiten pro Zeile!"),
        ExerciseType.koordinaten_rechteck: ("Rechteck", "Koordinaten", "koordinaten", "rechteck",
            "Zeichne ein Rechteck mit 4 Eckpunkten A, B, C, D im Koordinatensystem und berechne Seitenlängen, Umfang und Fläche."),
        ExerciseType.koordinaten_quadrat: ("Quadrat", "Koordinaten", "koordinaten", "quadrat",
            "Zeichne ein Quadrat mit 4 Eckpunkten A, B, C, D im Koordinatensystem und berechne Seitenlänge, Umfang und Fläche."),
        ExerciseType.koordinaten_dreieck: ("Dreieck", "Koordinaten", "koordinaten", "dreieck",
            "Zeichne ein rechtwinkliges Dreieck mit 3 Eckpunkten A, B, C im Koordinatensystem und berechne Seitenlängen und Fläche."),
        ExerciseType.koordinaten_parallelogramm: ("Parallelogramm", "Koordinaten", "koordinaten", "parallelogramm",
            "Zeichne ein Parallelogramm mit 4 Eckpunkten A, B, C, D im Koordinatensystem und berechne Seitenlängen, Umfang und Fläche."),
        ExerciseType.textaufgabe: ("Textaufgabe", "Sachaufgabe", "standard", "rechteck",
            "Erstelle eine kreative Textaufgabe/Sachaufgabe mit Geometrie im Alltag (NICHT Garten/Zaun!)."),
    }

    figure, category, typ, figure_type, description = type_descriptions[exercise_type]

    # Base prompt parts that are reused
    format_instructions = r'''
KRITISCH - ZUFÄLLIGE ZAHLEN:
- Würfle gedanklich NEUE Zahlen! NIEMALS die Beispielzahlen kopieren!
- Nutze: 3, 7, 9, 11, 13, 17, 19, 23, 27, 31, 35, 42, 48, 53, 67, 78, 85, 93, 145
- VERMEIDE: 4, 5, 6, 8, 10, 12, 20, 100 - zu häufig!

WICHTIG - Formatierung der Lösungen in Typst-Math-Syntax:
- Schreibe jeden Rechenschritt auf eine eigene Zeile, getrennt durch " || "
- JEDER Schritt besteht aus: FORMEL // ERKLÄRUNG (getrennt durch " // ")

KRITISCH - SEHR AUSFÜHRLICHE ERKLÄRUNGEN (wie ein geduldiger Nachhilfelehrer):
- Jede Erklärung MUSS 3-5 vollständige Sätze haben!
- Erkläre bei JEDEM Schritt: WAS machen wir? WARUM? WIE genau? Was bedeutet das ERGEBNIS?
- SCHLECHT: "Werte einsetzen" oder "Ausrechnen" ❌
- GUT: "Jetzt setzen wir unsere bekannten Werte in die Formel ein. Das bedeutet, wir ersetzen jeden Buchstaben durch die Zahl, die wir kennen. Hier ersetzen wir a durch 7 cm und b durch 5 cm. Danach können wir ganz normal ausrechnen."
- Benutze ermutigende Sprache: "Das schaffst du!", "Schritt für Schritt!"
- Verwende Typst-Math-Syntax: Brüche mit Klammern (Zähler)/(Nenner), Multiplikation mit dot, Einheiten in "cm", "m", "mm"
'''

    if typ == "tabelle":
        return f'''Du bist ein Mathematiklehrer für die 8. Klasse Realschule.
Erstelle genau 1 Tabellenaufgabe zum Thema {figure}.

{description}

Anforderungen:
- VERSCHIEDENE EINHEITEN pro Zeile mischen (cm, m, mm)! NIEMALS dm!
- Manche Werte gegeben, andere mit "?" markiert
- "tabelle" enthält: "spalten", "zeilen" (mit "?"), "loesungen" (alle Werte ausgefüllt)
- KRITISCH: Jede Zeile braucht KOMPLETT ANDERE Zahlen! Würfle neu!
- Nutze: 3, 7, 9, 11, 13, 17, 19, 23, 27, 31, 35, 42, 48, 53, 67, 78, 85
- VERMEIDE: 4, 5, 6, 8, 10, 12, 15, 20, 100
{format_instructions}
KRITISCH - Antworte mit NICHTS außer dem JSON. KEIN Text davor oder danach. Beginne DIREKT mit {{:
{{"aufgaben": [{{"nummer": 1, "typ": "tabelle", "aufgabe": "Berechne die fehlenden Größen...", "figur": "{figure_type}", "tabelle": {{"spalten": [...], "zeilen": [...], "loesungen": [...]}}, "erklaerung": "...", "loesung": "...", "kategorie": "{figure} - Tabelle"}}]}}'''
    elif typ == "koordinaten":
        return f'''Du bist ein Mathematiklehrer für die 8. Klasse Realschule.
Erstelle genau 1 Koordinatenaufgabe zum Thema {figure}.

{description}

Anforderungen:
- Der Schüler zeichnet die Figur im Koordinatensystem nach Koordinatenvorgabe
- KRITISCH: Wähle ZUFÄLLIGE Koordinaten! Variiere Startpunkt und Größe!
- GANZZAHLIGE Koordinaten zwischen 1 und 10 verwenden
- Seitenlängen der Figur: mindestens 3, maximal 8 Einheiten (gut lesbar auf DIN A4)
- max_x und max_y: passend zur Figur wählen (2-3 größer als größte Koordinate), MAXIMAL 10!
- Punkte werden als Koordinaten vorgegeben: A(x|y), B(x|y), ...
- Nach dem Einzeichnen: Berechne Seitenlängen, Umfang und/oder Fläche
- "koordinaten" enthält: "punkte" (Liste mit name, x, y), "max_x", "max_y", "gesucht"
- Im Koordinatensystem gilt: 1 Einheit = 1 cm
{format_instructions}
KRITISCH - Antworte mit NICHTS außer dem JSON. KEIN Text davor oder danach. Beginne DIREKT mit {{:
{{"aufgaben": [{{"nummer": 1, "typ": "koordinaten", "aufgabe": "Zeichne das {figure} ... in das Koordinatensystem ein. Berechne ...", "figur": "{figure_type}", "koordinaten": {{"punkte": [{{"name": "A", "x": 2, "y": 3}}, ...], "max_x": 9, "max_y": 8, "gesucht": ["a", "b", "U", "A"]}}, "erklaerung": "...", "loesung": "...", "kategorie": "{figure} - Koordinaten"}}]}}'''
    else:
        return f'''Du bist ein Mathematiklehrer für die 8. Klasse Realschule.
Erstelle genau 1 Aufgabe zum Thema {figure} - {category}.

{description}

Anforderungen:
- KRITISCH: Würfle gedanklich NEUE Zahlen! NIEMALS Beispielzahlen kopieren!
- Nutze: 3, 7, 9, 11, 13, 17, 19, 23, 27, 31, 35, 42, 48, 53, 67, 78, 85, 93, 145
- VERMEIDE: 4, 5, 6, 8, 10, 12, 15, 20, 100 - zu häufig!
- Verwende verschiedene Einheiten (cm, m, mm) - NIEMALS dm!
- Skizze mit allen gegebenen Werten und "?" für gesuchte Werte
{format_instructions}
KRITISCH - Antworte mit NICHTS außer dem JSON. KEIN Text davor oder danach. Beginne DIREKT mit {{:
{{"aufgaben": [{{"nummer": 1, "typ": "standard", "aufgabe": "...", "figur": "{figure_type}", "skizze": {{...}}, "erklaerung": "...", "loesung": "...", "kategorie": "{figure} - {category}"}}]}}'''


TYPST_TEMPLATE = r'''
#import "@preview/cetz:0.3.2"

#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2cm),
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
  lang: "de",
)

#set heading(numbering: none)

#show heading.where(level: 1): it => [
  #set text(size: 16pt, weight: "bold")
  #block(
    below: 0.5em,
    [#it.body]
  )
  #line(length: 100%, stroke: 0.5pt)
  #v(0.5em)
]

#show heading.where(level: 2): it => [
  #set text(size: 12pt, weight: "bold", fill: rgb("#1a5276"))
  #block(above: 1em, below: 0.3em, it.body)
]

// Aufgabenblatt
= Aufgaben

{exercises_content}

#pagebreak()

// Lösungsblatt
= Lösungen

{solutions_content}
'''

EXERCISE_TEMPLATE = r'''
#block(breakable: false)[
== Aufgabe {number}
#text(size: 9pt, fill: gray)[{category}]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[{exercise_text}]],
  [#align(center)[{sketch}]],
)

#v(0.5em)
{grid}
#v(0.8em)
]
'''

EXERCISE_NO_SKETCH_TEMPLATE = r'''
#block(breakable: false)[
== Aufgabe {number}
#text(size: 9pt, fill: gray)[{category}]

#pad(left: 1em)[{exercise_text}]

#v(0.5em)
{grid}
#v(0.8em)
]
'''

SOLUTION_TEMPLATE = r'''
== Aufgabe {number}
#text(size: 10pt, style: "italic")[{exercise_text}]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[{explanation}]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  {steps}
]

#v(0.5em)
'''

STEP_TEMPLATE = r'''#block(
  fill: {fill_color},
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + {stroke_color}),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ {formula} $],
    [#text(size: 9pt)[{explanation}]],
  )
]
#v(4pt)
'''

STEP_NO_EXPLANATION_TEMPLATE = r'''#block(
  fill: {fill_color},
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + {stroke_color}),
  width: 100%,
)[
  #align(left)[$ {formula} $]
]
#v(4pt)
'''

# Template for row headers in table solutions (e.g., "Zeile 1:")
ROW_HEADER_TEMPLATE = r'''#v(8pt)
#block(
  fill: rgb("#e3f2fd"),
  inset: (x: 12pt, y: 10pt),
  radius: 5pt,
  stroke: (left: 4pt + rgb("#1565c0")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [#text(weight: "bold", size: 11pt)[{row_title}]],
    [#text(size: 10pt)[{row_info}]],
  )
]
#v(6pt)
'''

# CeTZ sketch templates
SKETCH_RECTANGLE = r'''#cetz.canvas({{
  import cetz.draw: *

  // Rectangle
  rect((0, 0), (3, 2), stroke: 0.5pt)

  // Labels with variable names and values
  content((1.5, -0.3), [${label_a}$], anchor: "north")
  content((3.3, 1), [${label_b}$], anchor: "west")
  {extra_label}
}})'''

SKETCH_SQUARE = r'''#cetz.canvas({{
  import cetz.draw: *

  // Square
  rect((0, 0), (2.5, 2.5), stroke: 0.5pt)

  // Labels with variable names and values
  content((1.25, -0.3), [${label_a}$], anchor: "north")
  {extra_label}
}})'''

SKETCH_TRIANGLE = r'''#cetz.canvas({{
  import cetz.draw: *

  // Triangle
  line((0, 0), (3, 0), (1.5, 2.2), close: true, stroke: 0.5pt)

  // Height (dashed)
  set-style(stroke: (dash: "dashed", paint: gray))
  line((1.5, 0), (1.5, 2.2))

  // Right angle marker
  set-style(stroke: 0.3pt)
  line((1.5, 0.2), (1.7, 0.2), (1.7, 0))

  // Labels with variable names and values
  content((1.5, -0.3), [${label_g}$], anchor: "north")
  content((1.75, 1.1), [${label_h}$], anchor: "west")
  {extra_label}
}})'''

SKETCH_TRIANGLE_PERIMETER = r'''#cetz.canvas({{
  import cetz.draw: *

  // Triangle with three labeled sides
  line((0, 0), (3, 0), (1.5, 2.2), close: true, stroke: 0.5pt)

  // Labels for all three sides
  content((1.5, -0.3), [${label_a}$], anchor: "north")
  content((0.5, 1.3), [${label_b}$], anchor: "east")
  content((2.5, 1.3), [${label_c}$], anchor: "west")
  {extra_label}
}})'''

GRID_TEMPLATE = r'''#box(
  width: 100%,
  stroke: 0.5pt + rgb("#cccccc"),
)[
  #cetz.canvas(length: 1cm, {{
    import cetz.draw: *

    let width = {grid_width}
    let height = {grid_height}
    let cell = 0.5  // 5mm cells

    // Vertical lines
    for x in range(0, int(width / cell) + 1) {{
      line((x * cell, 0), (x * cell, height), stroke: 0.3pt + rgb("#cccccc"))
    }}
    // Horizontal lines
    for y in range(0, int(height / cell) + 1) {{
      line((0, y * cell), (width, y * cell), stroke: 0.3pt + rgb("#cccccc"))
    }}
  }})
]'''

SKETCH_PARALLELOGRAM = r'''#cetz.canvas({{
  import cetz.draw: *

  // Parallelogram
  line((0, 0), (3, 0), (3.8, 2), (0.8, 2), close: true, stroke: 0.5pt)

  // Height (dashed)
  set-style(stroke: (dash: "dashed", paint: gray))
  line((0.8, 0), (0.8, 2))

  // Right angle marker
  set-style(stroke: 0.3pt)
  line((0.8, 0.2), (1.0, 0.2), (1.0, 0))

  // Labels with variable names and values
  content((1.5, -0.3), [${label_a}$], anchor: "north")
  content((0.5, 1), [${label_h}$], anchor: "east")
  {extra_label}
}})'''

# Coordinate system template for coordinate exercises
COORDINATE_SYSTEM_TEMPLATE = r'''#cetz.canvas(length: 0.7cm, {{
  import cetz.draw: *

  let max_x = {max_x}
  let max_y = {max_y}

  // Grid lines (light gray)
  set-style(stroke: 0.3pt + rgb("#dddddd"))
  for x in range(0, max_x + 1) {{
    line((x, 0), (x, max_y))
  }}
  for y in range(0, max_y + 1) {{
    line((0, y), (max_x, y))
  }}

  // Axes (black)
  set-style(stroke: 0.8pt + black)
  line((-0.3, 0), (max_x + 0.5, 0), mark: (end: ">"))
  line((0, -0.3), (0, max_y + 0.5), mark: (end: ">"))

  // Axis labels
  content((max_x + 0.7, 0), [$x$], anchor: "west")
  content((0, max_y + 0.7), [$y$], anchor: "south")

  // Tick marks and numbers on x-axis
  for x in range(1, max_x + 1) {{
    line((x, -0.1), (x, 0.1), stroke: 0.5pt)
    content((x, -0.4), [#text(size: 8pt)[#str(x)]], anchor: "north")
  }}

  // Tick marks and numbers on y-axis
  for y in range(1, max_y + 1) {{
    line((-0.1, y), (0.1, y), stroke: 0.5pt)
    content((-0.4, y), [#text(size: 8pt)[#str(y)]], anchor: "east")
  }}

  // Origin label
  content((-0.3, -0.3), [#text(size: 8pt)[0]], anchor: "north-east")

  // Points and shape will be drawn by the student
  {points_markup}
}})'''

# Template for coordinate exercises (with empty coordinate system for drawing)
EXERCISE_COORDINATE_TEMPLATE = r'''
#block(breakable: false)[
== Aufgabe {number}
#text(size: 9pt, fill: gray)[{category}]

#grid(
  columns: (1fr, auto),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[{exercise_text}]],
  [{coordinate_system}],
)

#v(0.5em)
{grid}
#v(0.8em)
]
'''

# Template for coordinate solution (with shape drawn)
SOLUTION_COORDINATE_TEMPLATE = r'''
== Aufgabe {number}
#text(size: 10pt, style: "italic")[{exercise_text}]

#v(0.5em)
#align(center)[{coordinate_system_solution}]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[{explanation}]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  {steps}
]

#v(0.5em)
'''

# Table templates for table exercises
EXERCISE_TABLE_TEMPLATE = r'''
#block(breakable: false)[
== Aufgabe {number}
#text(size: 9pt, fill: gray)[{category}]

#pad(left: 0.5em)[{exercise_text}]

#v(0.5em)
#align(center)[
#table(
  columns: {num_cols},
  align: center + horizon,
  stroke: 0.5pt,
  inset: 8pt,
  {header_row}
  {data_rows}
)
]

#v(0.5em)
{grid}
#v(0.8em)
]
'''

SOLUTION_TABLE_TEMPLATE = r'''
== Aufgabe {number}
#text(size: 10pt, style: "italic")[{exercise_text}]

#v(0.5em)
#align(center)[
#table(
  columns: {num_cols},
  align: center + horizon,
  stroke: 0.5pt,
  inset: 8pt,
  {header_row}
  {solution_rows}
)
]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[{explanation}]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  {steps}
]

#v(0.5em)
'''


def generate_table(table_data: dict, show_solutions: bool = False) -> tuple[str, str]:
    """Generate Typst table markup for table exercises.

    Returns (header_row, data_rows) formatted for Typst table.
    """
    columns = table_data.get("spalten", [])
    rows = table_data.get("zeilen", []) if not show_solutions else table_data.get("loesungen", [])

    # Header row with bold column names (simple bold cells, not table.header)
    header_cells = [f"[*{col}*]" for col in columns]
    header_row = ", ".join(header_cells) + ","

    # Data rows
    data_rows_parts = []
    for row in rows:
        row_cells = []
        for col in columns:
            val = row.get(col, "")
            if val == "?":
                # Question mark in red
                row_cells.append('[#text(fill: rgb("#c0392b"))[?]]')
            elif show_solutions and "?" not in str(val):
                # Solved value in green
                row_cells.append(f'[#text(fill: rgb("#1e8449"))[{val}]]')
            else:
                row_cells.append(f"[{val}]")
        data_rows_parts.append(", ".join(row_cells) + ",")

    data_rows = "\n  ".join(data_rows_parts)

    return header_row, data_rows


def generate_coordinate_system(coord_data: dict, show_solution: bool = False) -> str:
    """Generate a coordinate system with optional shape drawn.

    Args:
        coord_data: Dict with 'punkte' (list of point dicts with 'name', 'x', 'y'),
                   'figur' type, and 'max_x', 'max_y' for axis limits
        show_solution: If True, draw the shape; if False, only show empty grid
    """
    points = coord_data.get("punkte", [])
    max_x = coord_data.get("max_x", 10)
    max_y = coord_data.get("max_y", 10)

    # Limit max values to ensure it fits on DIN A4 (at 0.7cm per unit, max 10 = 7cm)
    max_x = min(max_x, 10)
    max_y = min(max_y, 10)

    # Ensure max values are at least 2 units larger than the largest coordinate
    if points:
        largest_x = max(p.get("x", 0) for p in points)
        largest_y = max(p.get("y", 0) for p in points)
        max_x = max(max_x, largest_x + 2)
        max_y = max(max_y, largest_y + 2)
        # Re-apply limits after adjustment
        max_x = min(max_x, 10)
        max_y = min(max_y, 10)

    points_markup = ""

    if show_solution and points:
        # Draw the shape by connecting points
        point_coords = [(p["x"], p["y"]) for p in points]

        # Draw filled shape
        coords_str = ", ".join([f'({p["x"]}, {p["y"]})' for p in points])
        points_markup += f'''
  // Draw shape
  set-style(stroke: 1.5pt + rgb("#2e86ab"), fill: rgb("#2e86ab").transparentize(80%))
  line({coords_str}, close: true)
'''

        # Draw and label points
        for p in points:
            points_markup += f'''
  // Point {p["name"]}
  set-style(stroke: none, fill: rgb("#d62828"))
  circle(({p["x"]}, {p["y"]}), radius: 0.12)
  content(({p["x"]} + 0.3, {p["y"]} + 0.3), [#text(size: 9pt, weight: "bold")[{p["name"]}]], anchor: "south-west")
'''

    return COORDINATE_SYSTEM_TEMPLATE.format(
        max_x=max_x,
        max_y=max_y,
        points_markup=points_markup,
    )


def generate_grid(solution: str) -> str:
    """Generate a checkered grid (Karo) for working space.

    Grid size is based on the number of solution steps.
    Lineatur 28: 5mm cells without margin.
    """
    # Count solution steps to determine grid height
    steps = [s.strip() for s in solution.split("||") if s.strip()]
    num_steps = len(steps)

    # Calculate grid height: ~1.5cm per step, minimum 4cm, maximum 10cm
    grid_height = max(4, min(10, num_steps * 1.5))

    # Width is 17cm (A4 width minus margins)
    grid_width = 17

    return GRID_TEMPLATE.format(
        grid_width=grid_width,
        grid_height=grid_height,
    )


def format_unit_for_typst(value: str) -> str:
    """Convert unit notation to Typst math syntax."""
    if value == "?":
        return "?"
    value = value.replace(" cm²", ' "cm"^2')
    value = value.replace(" m²", ' "m"^2')
    value = value.replace(" mm²", ' "mm"^2')
    value = value.replace(" cm", ' "cm"')
    value = value.replace(" m", ' "m"')
    value = value.replace(" mm", ' "mm"')
    return value


def generate_sketch(figure: str, values: dict) -> str:
    """Generate a CeTZ sketch based on the figure type and values."""
    if not figure or not values:
        return ""

    def format_label(var_name: str, default: str = "?") -> str:
        """Format a label with variable name and value (e.g., 'a = 5 cm')."""
        val = values.get(var_name, default)
        if val == "?":
            return f'{var_name} = #text(fill: rgb("#c0392b"))[?]'
        formatted_val = format_unit_for_typst(val)
        return f"{var_name} = {formatted_val}"

    def format_result_label(var_name: str, val: str, position: str) -> str:
        """Format a label for A=? or U=? (searched value)."""
        if val == "?":
            return f'content({position}, [#text(fill: rgb("#c0392b"))[$' + var_name + ' = ?$]], anchor: "center")'
        formatted_val = format_unit_for_typst(val)
        return f'content({position}, [${var_name} = {formatted_val}$], anchor: "center")'

    extra_label = ""

    if figure == "rechteck":
        # Show area or perimeter if provided
        if "A" in values:
            extra_label = format_result_label("A", values["A"], "(1.5, 1)")
        elif "U" in values:
            extra_label = format_result_label("U", values["U"], "(1.5, 1)")

        return SKETCH_RECTANGLE.format(
            label_a=format_label("a"),
            label_b=format_label("b"),
            extra_label=extra_label,
        )

    elif figure == "quadrat":
        if "A" in values:
            extra_label = format_result_label("A", values["A"], "(1.25, 1.25)")
        elif "U" in values:
            extra_label = format_result_label("U", values["U"], "(1.25, 1.25)")

        return SKETCH_SQUARE.format(
            label_a=format_label("a"),
            extra_label=extra_label,
        )

    elif figure == "dreieck":
        if "A" in values:
            extra_label = format_result_label("A", values["A"], "(2.5, 1.5)")

        return SKETCH_TRIANGLE.format(
            label_g=format_label("g"),
            label_h=format_label("h"),
            extra_label=extra_label,
        )

    elif figure == "dreieck_umfang":
        if "U" in values:
            extra_label = format_result_label("U", values["U"], "(1.5, 0.8)")

        return SKETCH_TRIANGLE_PERIMETER.format(
            label_a=format_label("a"),
            label_b=format_label("b"),
            label_c=format_label("c"),
            extra_label=extra_label,
        )

    elif figure == "parallelogramm":
        if "A" in values:
            extra_label = format_result_label("A", values["A"], "(2.3, 1)")
        elif "U" in values:
            extra_label = format_result_label("U", values["U"], "(2.3, 1)")

        # For perimeter, show a and b; for area, show a and h
        if "b" in values and "h" not in values:
            # Perimeter mode: show both sides
            return SKETCH_PARALLELOGRAM.format(
                label_a=format_label("a"),
                label_h=format_label("b"),  # Show b instead of h
                extra_label=extra_label,
            )
        else:
            # Area mode: show a and h
            return SKETCH_PARALLELOGRAM.format(
                label_a=format_label("a"),
                label_h=format_label("h"),
                extra_label=extra_label,
            )

    return ""


def repair_json(content: str) -> str:
    """Try to repair common JSON issues from Claude output."""
    # Count braces and brackets
    open_braces = content.count("{")
    close_braces = content.count("}")
    open_brackets = content.count("[")
    close_brackets = content.count("]")

    # Fix extra closing braces at the end
    if close_braces > open_braces:
        extra = close_braces - open_braces
        # Remove extra closing braces from the end pattern like "}}]}"
        for _ in range(extra):
            if content.endswith("}}]}"):
                content = content[:-4] + "}]}"
            elif content.endswith("}}"):
                content = content[:-1]

    # Fix extra closing brackets
    if close_brackets > open_brackets:
        extra = close_brackets - open_brackets
        for _ in range(extra):
            if content.endswith("]]"):
                content = content[:-1]

    # Fix missing closing braces/brackets
    if open_braces > close_braces:
        content += "}" * (open_braces - close_braces)
    if open_brackets > close_brackets:
        content += "]" * (open_brackets - close_brackets)

    return content


def generate_exercises(exercise_type: Optional[ExerciseType] = None) -> list[dict]:
    """Call Claude CLI to generate exercises.

    Args:
        exercise_type: Optional specific exercise type. If None, generates 10 mixed exercises.
    """
    # Generate random seed section for variety
    random_seed = generate_random_seed_prompt()

    if exercise_type:
        base_prompt = get_single_type_prompt(exercise_type)
        print(f"Generating 1 exercise of type '{exercise_type.value}' with Claude CLI...")
    else:
        base_prompt = PROMPT
        print("Generating exercises with Claude CLI...")

    # Inject random seed at the beginning of the prompt
    prompt = random_seed + "\n" + base_prompt

    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--output-format", "json"],
            capture_output=True,
            text=True,
            check=True,
        )

        # Parse JSON output from Claude CLI
        response = json.loads(result.stdout)

        # Extract the actual text content
        if isinstance(response, dict) and "result" in response:
            content = response["result"]
        elif isinstance(response, list):
            # Handle array format
            for item in response:
                if item.get("type") == "text":
                    content = item.get("text", "")
                    break
            else:
                content = result.stdout
        else:
            content = result.stdout

        # Try to parse the content as JSON
        # Remove potential markdown code blocks and extract JSON
        content = content.strip()

        # Handle case where there's text before the JSON (find first '{')
        json_start = content.find('{')
        if json_start > 0:
            # There's text before the JSON, remove it
            content = content[json_start:]

        # Handle case where there's text before the JSON block
        if "```json" in content:
            # Extract content between ```json and ```
            start = content.find("```json") + 7
            end = content.find("```", start)
            if end != -1:
                content = content[start:end]
            else:
                content = content[start:]
        elif "```" in content:
            start = content.find("```") + 3
            end = content.find("```", start)
            if end != -1:
                content = content[start:end]
            else:
                content = content[start:]

        # Also handle simple code block removal if still present
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()

        # Try to repair common JSON issues
        content = repair_json(content)

        data = json.loads(content)
        return data.get("aufgaben", [])

    except subprocess.CalledProcessError as e:
        print(f"Error calling Claude CLI: {e}")
        print(f"stderr: {e.stderr}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        # Show context around the error position
        error_pos = e.pos if hasattr(e, 'pos') else 0
        start = max(0, error_pos - 100)
        end = min(len(content), error_pos + 100)
        print(f"Context around error (pos {error_pos}):")
        print(f"...{content[start:end]}...")
        # Save raw content for debugging
        debug_file = Path("debug_response.json")
        debug_file.write_text(content, encoding="utf-8")
        print(f"Raw content saved to {debug_file}")
        sys.exit(1)


def fix_typst_quotes(text: str) -> str:
    """Replace German quotes with straight quotes for Typst math mode."""
    # Replace German/typographic quotes with straight quotes using Unicode escapes
    text = text.replace("\u201e", '"')  # „ German opening quote (low-9)
    text = text.replace("\u201c", '"')  # " Left double quote
    text = text.replace("\u201d", '"')  # " Right double quote
    text = text.replace("\u201a", "'")  # ‚ Single low-9 quote
    text = text.replace("\u2018", "'")  # ' Left single quote
    text = text.replace("\u2019", "'")  # ' Right single quote
    text = text.replace("\u00ab", '"')  # « Guillemet left
    text = text.replace("\u00bb", '"')  # » Guillemet right
    text = text.replace("\u2039", "'")  # ‹ Single guillemet left
    text = text.replace("\u203a", "'")  # › Single guillemet right
    return text


def is_result_step(formula: str) -> bool:
    """Check if a formula step is a final result (ends with a numeric result with unit)."""
    import re
    formula = formula.strip()

    # Check if formula ENDS with a result: = number "unit" or = number "unit"^2
    # This matches: "U = 14 cm + 10 cm = 24 cm", "A = 7 cm dot 5 cm = 35 cm^2", etc.
    ends_with_result = r'=\s*\d+([.,]\d+)?\s*"?(cm|m|mm)"?(\^2)?\s*$'

    # Also check if it starts with a result variable (A, U, a, b, etc.)
    starts_with_var = r'^[AUabcgh](_\w+)?\s*='

    # It's a result if it starts with a variable AND ends with a numeric result
    return bool(re.search(ends_with_result, formula)) and bool(re.match(starts_with_var, formula))


def format_solution_steps(solution: str, is_table: bool = False) -> str:
    """Format solution steps as Typst blocks with explanations.

    Args:
        solution: The solution string with steps separated by ||
        is_table: If True, don't highlight the last step in green (for table exercises)
    """
    # Fix German quotes in the entire solution
    solution = fix_typst_quotes(solution)
    steps = [s.strip() for s in solution.split("||") if s.strip()]
    result_parts = []

    for i, step in enumerate(steps):
        # Check if this is a row header (e.g., "Zeile 1:" // Gegeben: ...)
        if " // " in step:
            formula, explanation = step.split(" // ", 1)
            formula = formula.strip()

            # Check if formula is a row header like "Zeile 1:" or "\"Zeile 1:\""
            if formula.startswith('"Zeile') or formula.startswith("Zeile"):
                # Extract row title (remove quotes if present)
                row_title = formula.strip('"')
                result_parts.append(
                    ROW_HEADER_TEMPLATE.format(
                        row_title=row_title,
                        row_info=explanation.strip(),
                    )
                )
                continue

        # Extract formula for result detection
        if " // " in step:
            formula_part = step.split(" // ", 1)[0].strip()
        else:
            formula_part = step.strip()

        is_last = i == len(steps) - 1
        is_result = is_result_step(formula_part)

        # Green for: last step (non-table) OR any result step (non-table)
        if not is_table and (is_last or is_result):
            fill_color = 'rgb("#e8f6e9")'
            stroke_color = 'rgb("#1e8449")'
        else:
            fill_color = 'rgb("#f8f9fa")'
            stroke_color = 'rgb("#cccccc")'

        # Check if explanation is present (separated by " // ")
        if " // " in step:
            formula, explanation = step.split(" // ", 1)
            result_parts.append(
                STEP_TEMPLATE.format(
                    formula=formula.strip(),
                    explanation=explanation.strip(),
                    fill_color=fill_color,
                    stroke_color=stroke_color,
                )
            )
        else:
            result_parts.append(
                STEP_NO_EXPLANATION_TEMPLATE.format(
                    formula=step,
                    fill_color=fill_color,
                    stroke_color=stroke_color,
                )
            )

    return "\n".join(result_parts)


def create_typst_document(exercises: list[dict], show_grid: bool = False) -> str:
    """Create the Typst document."""
    # Format exercises
    exercise_parts = []
    for exercise in exercises:
        solution = exercise.get("loesung", "")
        grid = generate_grid(solution) if show_grid else ""
        exercise_type = exercise.get("typ", "standard")

        if exercise_type == "tabelle":
            # Table exercise
            table_data = exercise.get("tabelle", {})
            columns = table_data.get("spalten", [])
            header_row, data_rows = generate_table(table_data, show_solutions=False)

            exercise_parts.append(
                EXERCISE_TABLE_TEMPLATE.format(
                    number=exercise.get("nummer", "?"),
                    category=exercise.get("kategorie", ""),
                    exercise_text=exercise.get("aufgabe", ""),
                    num_cols=len(columns),
                    header_row=header_row,
                    data_rows=data_rows,
                    grid=grid,
                )
            )
        elif exercise_type == "koordinaten":
            # Coordinate exercise with coordinate system
            coord_data = exercise.get("koordinaten", {})
            coordinate_system = generate_coordinate_system(coord_data, show_solution=False)

            exercise_parts.append(
                EXERCISE_COORDINATE_TEMPLATE.format(
                    number=exercise.get("nummer", "?"),
                    category=exercise.get("kategorie", ""),
                    exercise_text=exercise.get("aufgabe", ""),
                    coordinate_system=coordinate_system,
                    grid=grid,
                )
            )
        else:
            # Standard exercise with sketch
            figure = exercise.get("figur", "")
            sketch_values = exercise.get("skizze", {})
            sketch = generate_sketch(figure, sketch_values)

            if sketch:
                exercise_parts.append(
                    EXERCISE_TEMPLATE.format(
                        number=exercise.get("nummer", "?"),
                        category=exercise.get("kategorie", ""),
                        exercise_text=exercise.get("aufgabe", ""),
                        sketch=sketch,
                        grid=grid,
                    )
                )
            else:
                exercise_parts.append(
                    EXERCISE_NO_SKETCH_TEMPLATE.format(
                        number=exercise.get("nummer", "?"),
                        category=exercise.get("kategorie", ""),
                        exercise_text=exercise.get("aufgabe", ""),
                        grid=grid,
                    )
                )

    # Format solutions
    solution_parts = []
    for exercise in exercises:
        exercise_type = exercise.get("typ", "standard")
        is_table = exercise_type == "tabelle"
        steps = format_solution_steps(exercise.get("loesung", ""), is_table=is_table)

        if exercise_type == "tabelle":
            # Table solution with filled-in answers
            table_data = exercise.get("tabelle", {})
            columns = table_data.get("spalten", [])
            header_row, solution_rows = generate_table(table_data, show_solutions=True)

            solution_parts.append(
                SOLUTION_TABLE_TEMPLATE.format(
                    number=exercise.get("nummer", "?"),
                    exercise_text=exercise.get("aufgabe", ""),
                    num_cols=len(columns),
                    header_row=header_row,
                    solution_rows=solution_rows,
                    explanation=exercise.get("erklaerung", ""),
                    steps=steps,
                )
            )
        elif exercise_type == "koordinaten":
            # Coordinate solution with shape drawn
            coord_data = exercise.get("koordinaten", {})
            coordinate_system_solution = generate_coordinate_system(coord_data, show_solution=True)

            solution_parts.append(
                SOLUTION_COORDINATE_TEMPLATE.format(
                    number=exercise.get("nummer", "?"),
                    exercise_text=exercise.get("aufgabe", ""),
                    coordinate_system_solution=coordinate_system_solution,
                    explanation=exercise.get("erklaerung", ""),
                    steps=steps,
                )
            )
        else:
            solution_parts.append(
                SOLUTION_TEMPLATE.format(
                    number=exercise.get("nummer", "?"),
                    exercise_text=exercise.get("aufgabe", ""),
                    explanation=exercise.get("erklaerung", ""),
                    steps=steps,
                )
            )

    return TYPST_TEMPLATE.format(
        exercises_content="\n".join(exercise_parts),
        solutions_content="\n".join(solution_parts),
    )


def create_pdf(exercises: list[dict], output_path: Path, show_grid: bool = False) -> None:
    """Create a PDF with exercises and solutions."""
    typst_content = create_typst_document(exercises, show_grid=show_grid)

    # Write temporary Typst file
    typst_file = output_path.with_suffix(".typ")
    typst_file.write_text(typst_content, encoding="utf-8")

    # Compile to PDF
    pdf_bytes = typst.compile(typst_file)
    output_path.write_bytes(pdf_bytes)

    # Keep Typst file for debugging (same name as PDF but .typ)
    print(f"PDF created: {output_path}")
    print(f"Typst source: {typst_file}")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    karo: Annotated[
        bool,
        typer.Option("--karo", "-k", help="Fügt Karokästchen (Lineatur 28) zum Rechnen hinzu"),
    ] = False,
    typ: Annotated[
        Optional[ExerciseType],
        typer.Option("--typ", "-t", help="Generiert nur 1 Aufgabe des angegebenen Typs"),
    ] = None,
) -> None:
    """Generate math exercises for 8th grade as PDF."""
    # If a subcommand is invoked, don't run the main logic
    if ctx.invoked_subcommand is not None:
        return
    # Output path
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path.cwd()

    if typ:
        output_path = output_dir / f"matheaufgaben_{typ.value}_{timestamp}.pdf"
    else:
        output_path = output_dir / f"matheaufgaben_{timestamp}.pdf"

    # Generate exercises
    exercises = generate_exercises(exercise_type=typ)

    if not exercises:
        print("No exercises generated!")
        sys.exit(1)

    print(f"{len(exercises)} exercise(s) generated.")

    # Create PDF
    create_pdf(exercises, output_path, show_grid=karo)

    print(f"\nDone! PDF created: {output_path}")


@app.command("typen")
def list_types() -> None:
    """List all available exercise types."""
    print("Verfügbare Aufgabentypen:\n")
    for typ in ExerciseType:
        print(f"  {typ.value}")
    print("\nBeispiel: uv run python matheaufgaben.py --typ rechteck-flaeche")


if __name__ == "__main__":
    app()
