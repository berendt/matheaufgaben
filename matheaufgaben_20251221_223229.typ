
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


#block(breakable: false)[
== Aufgabe 1
#text(size: 9pt, fill: gray)[Rechteck - Flächenberechnung]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Ein Rechteck hat die Seitenlängen a = 17 cm und b = 9 cm. Berechne die Fläche A des Rechtecks.]],
  [#align(center)[#cetz.canvas({
  import cetz.draw: *

  // Rectangle
  rect((0, 0), (3, 2), stroke: 0.5pt)

  // Labels with variable names and values
  content((1.5, -0.3), [$a = 17 "cm"$], anchor: "north")
  content((3.3, 1), [$b = 9 "cm"$], anchor: "west")
  content((1.5, 1), [#text(fill: rgb("#c0392b"))[$A = ?$]], anchor: "center")
})]],
)

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 2
#text(size: 9pt, fill: gray)[Quadrat - Umfangberechnung]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Ein Quadrat hat eine Seitenlänge von a = 13 m. Berechne den Umfang U des Quadrats.]],
  [#align(center)[#cetz.canvas({
  import cetz.draw: *

  // Square
  rect((0, 0), (2.5, 2.5), stroke: 0.5pt)

  // Labels with variable names and values
  content((1.25, -0.3), [$a = 13 "m"$], anchor: "north")
  content((1.25, 1.25), [#text(fill: rgb("#c0392b"))[$U = ?$]], anchor: "center")
})]],
)

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 3
#text(size: 9pt, fill: gray)[Parallelogramm - Flächenberechnung]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Ein Parallelogramm hat die Grundseite a = 23 mm und die Höhe h = 14 mm. Berechne die Fläche A.]],
  [#align(center)[#cetz.canvas({
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
  content((1.5, -0.3), [$a = 23 "m"m$], anchor: "north")
  content((0.5, 1), [$h = 14 "m"m$], anchor: "east")
  content((2.3, 1), [#text(fill: rgb("#c0392b"))[$A = ?$]], anchor: "center")
})]],
)

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 4
#text(size: 9pt, fill: gray)[Dreieck - Umfangberechnung]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Ein Dreieck hat die drei Seiten a = 27 cm, b = 35 cm und c = 42 cm. Berechne den Umfang U des Dreiecks.]],
  [#align(center)[#cetz.canvas({
  import cetz.draw: *

  // Triangle with three labeled sides
  line((0, 0), (3, 0), (1.5, 2.2), close: true, stroke: 0.5pt)

  // Labels for all three sides
  content((1.5, -0.3), [$a = 27 "cm"$], anchor: "north")
  content((0.5, 1.3), [$b = 35 "cm"$], anchor: "east")
  content((2.5, 1.3), [$c = 42 "cm"$], anchor: "west")
  content((1.5, 0.8), [#text(fill: rgb("#c0392b"))[$U = ?$]], anchor: "center")
})]],
)

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 5
#text(size: 9pt, fill: gray)[Rechteck - Formelumstellung]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Ein Rechteck hat die Fläche A = 171 m² und die Seitenlänge b = 9 m. Berechne die Seitenlänge a.]],
  [#align(center)[#cetz.canvas({
  import cetz.draw: *

  // Rectangle
  rect((0, 0), (3, 2), stroke: 0.5pt)

  // Labels with variable names and values
  content((1.5, -0.3), [$a = #text(fill: rgb("#c0392b"))[?]$], anchor: "north")
  content((3.3, 1), [$b = 9 "m"$], anchor: "west")
  content((1.5, 1), [$A = 171 "m"^2$], anchor: "center")
})]],
)

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 6
#text(size: 9pt, fill: gray)[Quadrat - Formelumstellung]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Ein Quadrat hat die Fläche A = 196 cm². Berechne die Seitenlänge a.]],
  [#align(center)[#cetz.canvas({
  import cetz.draw: *

  // Square
  rect((0, 0), (2.5, 2.5), stroke: 0.5pt)

  // Labels with variable names and values
  content((1.25, -0.3), [$a = #text(fill: rgb("#c0392b"))[?]$], anchor: "north")
  content((1.25, 1.25), [$A = 196 "cm"^2$], anchor: "center")
})]],
)

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 7
#text(size: 9pt, fill: gray)[Dreieck - Formelumstellung]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Ein Dreieck hat die Fläche A = 91 mm² und die Höhe h = 13 mm. Berechne die Grundseite g.]],
  [#align(center)[#cetz.canvas({
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
  content((1.5, -0.3), [$g = #text(fill: rgb("#c0392b"))[?]$], anchor: "north")
  content((1.75, 1.1), [$h = 13 "m"m$], anchor: "west")
  content((2.5, 1.5), [$A = 91 "mm"^2$], anchor: "center")
})]],
)

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 8
#text(size: 9pt, fill: gray)[Parallelogramm - Tabelle]

#pad(left: 0.5em)[Berechne die fehlenden Größen der Parallelogramme.]

#v(0.5em)
#align(center)[
#table(
  columns: 3,
  align: center + horizon,
  stroke: 0.5pt,
  inset: 8pt,
  [*a*], [*h*], [*A*],
  [19 cm], [7 cm], [#text(fill: rgb("#c0392b"))[?]],
  [#text(fill: rgb("#c0392b"))[?]], [11 m], [143 m²],
  [48 mm], [#text(fill: rgb("#c0392b"))[?]], [624 mm²],
  [#text(fill: rgb("#c0392b"))[?]], [8,5 cm], [178,5 cm²],
)
]

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 9
#text(size: 9pt, fill: gray)[Dreieck - Koordinaten]

#grid(
  columns: (1fr, auto),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Zeichne das Dreieck ABC mit den Eckpunkten A(2|1), B(9|1) und C(5|8) in das Koordinatensystem ein. Berechne anschließend die Grundseite g, die Höhe h und die Fläche A des Dreiecks. (1 Einheit = 1 cm)]],
  [#cetz.canvas(length: 0.7cm, {
  import cetz.draw: *

  let max_x = 10
  let max_y = 10

  // Grid lines (light gray)
  set-style(stroke: 0.3pt + rgb("#dddddd"))
  for x in range(0, max_x + 1) {
    line((x, 0), (x, max_y))
  }
  for y in range(0, max_y + 1) {
    line((0, y), (max_x, y))
  }

  // Axes (black)
  set-style(stroke: 0.8pt + black)
  line((-0.3, 0), (max_x + 0.5, 0), mark: (end: ">"))
  line((0, -0.3), (0, max_y + 0.5), mark: (end: ">"))

  // Axis labels
  content((max_x + 0.7, 0), [$x$], anchor: "west")
  content((0, max_y + 0.7), [$y$], anchor: "south")

  // Tick marks and numbers on x-axis
  for x in range(1, max_x + 1) {
    line((x, -0.1), (x, 0.1), stroke: 0.5pt)
    content((x, -0.4), [#text(size: 8pt)[#str(x)]], anchor: "north")
  }

  // Tick marks and numbers on y-axis
  for y in range(1, max_y + 1) {
    line((-0.1, y), (0.1, y), stroke: 0.5pt)
    content((-0.4, y), [#text(size: 8pt)[#str(y)]], anchor: "east")
  }

  // Origin label
  content((-0.3, -0.3), [#text(size: 8pt)[0]], anchor: "north-east")

  // Points and shape will be drawn by the student
  
})],
)

#v(0.5em)

#v(0.8em)
]


#block(breakable: false)[
== Aufgabe 10
#text(size: 9pt, fill: gray)[Rechteck - Sachaufgabe]

#grid(
  columns: (1fr, 5cm),
  column-gutter: 1em,
  align: (left + top, center + top),
  [#pad(left: 0.5em)[Familie Yilmaz möchte ihr Wohnzimmer mit einem neuen Teppich auslegen. Das Wohnzimmer ist rechteckig und hat die Maße 6,3 m Länge und 4,8 m Breite. Der gewünschte Teppichboden kostet 27 Euro pro Quadratmeter. Außerdem möchten sie eine Fußleiste um den gesamten Raum anbringen (die Türbreite von 85 cm wird ausgespart). Die Fußleiste kostet 8 Euro pro Meter. Berechne die Fläche des Zimmers, den Umfang, die Länge der benötigten Fußleiste und die Gesamtkosten für Teppich und Fußleiste.]],
  [#align(center)[#cetz.canvas({
  import cetz.draw: *

  // Rectangle
  rect((0, 0), (3, 2), stroke: 0.5pt)

  // Labels with variable names and values
  content((1.5, -0.3), [$a = 6,3 "m"$], anchor: "north")
  content((3.3, 1), [$b = 4,8 "m"$], anchor: "west")
  content((1.5, 1), [#text(fill: rgb("#c0392b"))[$A = ?$]], anchor: "center")
})]],
)

#v(0.5em)

#v(0.8em)
]


#pagebreak()

// Lösungsblatt
= Lösungen


== Aufgabe 1
#text(size: 10pt, style: "italic")[Ein Rechteck hat die Seitenlängen a = 17 cm und b = 9 cm. Berechne die Fläche A des Rechtecks.]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Wir kennen beide Seitenlängen des Rechtecks: a = 17 cm und b = 9 cm. Gesucht ist die Fläche A. Die Formel für die Rechtecksfläche lautet: A = a · b. Das bedeutet, wir multiplizieren einfach die beiden Seiten miteinander. Das ist gar nicht so schwer - wir müssen nur die Zahlen einsetzen und ausrechnen!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = a dot b $],
    [#text(size: 9pt)[Das ist die Formel für die Rechtecksfläche. Die Fläche eines Rechtecks berechnet sich, indem wir die Länge a mit der Breite b multiplizieren. Diese Formel musst du dir gut merken!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = 17 "cm" dot 9 "cm" $],
    [#text(size: 9pt)[Jetzt setzen wir unsere bekannten Werte in die Formel ein. Wir ersetzen den Buchstaben a durch 17 cm und den Buchstaben b durch 9 cm. Das Einsetzen ist ein wichtiger Schritt!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = 153 "cm"^2 $],
    [#text(size: 9pt)[Nun rechnen wir 17 mal 9 aus. Das ergibt 153. Bei den Einheiten gilt: cm mal cm ergibt cm² (Quadratzentimeter). Die Fläche des Rechtecks beträgt also 153 Quadratzentimeter. Super gemacht!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 2
#text(size: 10pt, style: "italic")[Ein Quadrat hat eine Seitenlänge von a = 13 m. Berechne den Umfang U des Quadrats.]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Wir haben ein Quadrat mit der Seitenlänge a = 13 m. Gesucht ist der Umfang U. Bei einem Quadrat sind alle vier Seiten gleich lang. Der Umfang ist die Summe aller Seitenlängen. Die Formel lautet: U = 4 · a. Das bedeutet, wir nehmen die Seitenlänge mal 4, weil ein Quadrat 4 gleich lange Seiten hat. Schritt für Schritt schaffen wir das!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = 4 dot a $],
    [#text(size: 9pt)[Das ist die Formel für den Umfang eines Quadrats. Weil alle vier Seiten gleich lang sind, müssen wir die Seitenlänge a einfach mit 4 multiplizieren. Das ist die kürzeste Formel für den Umfang!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = 4 dot 13 "m" $],
    [#text(size: 9pt)[Jetzt setzen wir den Wert für a ein. Die Seitenlänge ist 13 m, also ersetzen wir a durch 13 m. Nun müssen wir nur noch 4 mal 13 ausrechnen.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = 52 "m" $],
    [#text(size: 9pt)[4 mal 13 ergibt 52. Der Umfang des Quadrats beträgt also 52 Meter. Das bedeutet: Wenn du einmal um das ganze Quadrat herumgehst, legst du 52 Meter zurück. Toll gemacht!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 3
#text(size: 10pt, style: "italic")[Ein Parallelogramm hat die Grundseite a = 23 mm und die Höhe h = 14 mm. Berechne die Fläche A.]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Wir haben ein Parallelogramm mit der Grundseite a = 23 mm und der Höhe h = 14 mm. Gesucht ist die Fläche A. Die Formel für die Parallelogrammfläche ist fast wie beim Rechteck: A = a · h. Wir multiplizieren die Grundseite mit der Höhe. Wichtig: Die Höhe steht senkrecht auf der Grundseite! Das schaffst du!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = a dot h $],
    [#text(size: 9pt)[Das ist die Formel für die Fläche eines Parallelogramms. Sie sieht aus wie beim Rechteck, nur dass wir hier die Höhe h verwenden. Die Höhe ist der senkrechte Abstand zwischen den parallelen Seiten.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = 23 "mm" dot 14 "mm" $],
    [#text(size: 9pt)[Wir setzen unsere Werte ein: a ist 23 mm und h ist 14 mm. Jetzt müssen wir 23 mal 14 rechnen. Das ist etwas schwieriger, aber wir schaffen das!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = 322 "mm"^2 $],
    [#text(size: 9pt)[23 mal 14 ergibt 322. Bei den Einheiten gilt wieder: mm mal mm ergibt mm² (Quadratmillimeter). Die Fläche des Parallelogramms beträgt also 322 Quadratmillimeter. Sehr gut!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 4
#text(size: 10pt, style: "italic")[Ein Dreieck hat die drei Seiten a = 27 cm, b = 35 cm und c = 42 cm. Berechne den Umfang U des Dreiecks.]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Wir haben ein Dreieck mit den drei Seitenlängen a = 27 cm, b = 35 cm und c = 42 cm. Gesucht ist der Umfang U. Der Umfang eines Dreiecks ist einfach die Summe aller drei Seiten. Die Formel lautet: U = a + b + c. Wir addieren also alle drei Seitenlängen. Das ist wirklich nicht schwer - einfach zusammenzählen!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = a + b + c $],
    [#text(size: 9pt)[Das ist die Formel für den Umfang eines Dreiecks. Der Umfang ist die Gesamtlänge aller Seiten zusammen. Stell dir vor, du gehst einmal um das Dreieck herum - diese Strecke ist der Umfang!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = 27 "cm" + 35 "cm" + 42 "cm" $],
    [#text(size: 9pt)[Jetzt setzen wir alle drei Seitenlängen ein. Wir ersetzen a durch 27 cm, b durch 35 cm und c durch 42 cm. Nun addieren wir diese drei Zahlen.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = 104 "cm" $],
    [#text(size: 9pt)[27 plus 35 ergibt 62, und 62 plus 42 ergibt 104. Der Umfang des Dreiecks beträgt also 104 cm. Das bedeutet, wenn du einmal um das ganze Dreieck gehst, legst du 104 cm zurück. Prima!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 5
#text(size: 10pt, style: "italic")[Ein Rechteck hat die Fläche A = 171 m² und die Seitenlänge b = 9 m. Berechne die Seitenlänge a.]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Wir kennen die Fläche A = 171 m² und eine Seite b = 9 m. Gesucht ist die andere Seite a. Die Formel für die Rechtecksfläche lautet A = a · b. Diesmal müssen wir die Formel umstellen, damit a alleine steht. Dazu teilen wir beide Seiten durch b. Das klingt kompliziert, aber Schritt für Schritt ist es machbar!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = a dot b $],
    [#text(size: 9pt)[Das ist die Formel für die Rechtecksfläche. Die Fläche ist Länge mal Breite. Aber diesmal kennen wir die Fläche und eine Seite, und suchen die andere Seite.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a dot b = A $],
    [#text(size: 9pt)[Wir tauschen die beiden Seiten der Gleichung. Das dürfen wir immer machen! So steht das Gesuchte (mit a drin) auf der linken Seite. Das macht es übersichtlicher.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a = A / b $],
    [#text(size: 9pt)[Jetzt teilen wir beide Seiten der Gleichung durch b. Was wir auf einer Seite machen, müssen wir auch auf der anderen Seite machen! So verschwindet das b auf der linken Seite und a steht alleine.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a = (171 "m"^2) / (9 "m") $],
    [#text(size: 9pt)[Wir setzen unsere Werte ein: Die Fläche A ist 171 m² und b ist 9 m. Jetzt müssen wir 171 durch 9 teilen.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a = 19 "m" $],
    [#text(size: 9pt)[171 geteilt durch 9 ergibt 19. Bei den Einheiten kürzt sich m² durch m zu m. Die gesuchte Seitenlänge a beträgt also 19 Meter. Geschafft!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 6
#text(size: 10pt, style: "italic")[Ein Quadrat hat die Fläche A = 196 cm². Berechne die Seitenlänge a.]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Wir kennen die Fläche A = 196 cm² und suchen die Seitenlänge a. Bei einem Quadrat gilt: A = a². Um a zu finden, müssen wir die Quadratwurzel aus der Fläche ziehen. Das heißt: Welche Zahl mal sich selbst ergibt 196? Diese Umkehrrechnung zum Quadrieren nennt man Wurzelziehen. Das schaffst du!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = a^2 $],
    [#text(size: 9pt)[Das ist die Formel für die Quadratfläche. Bei einem Quadrat sind alle Seiten gleich lang, also ist die Fläche gleich Seitenlänge mal Seitenlänge, also a².]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a^2 = A $],
    [#text(size: 9pt)[Wir tauschen die Seiten der Gleichung. So steht a² auf der linken Seite und wir können besser sehen, was wir umstellen müssen.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a = sqrt(A) $],
    [#text(size: 9pt)[Um von a² auf a zu kommen, müssen wir die Quadratwurzel ziehen. Die Quadratwurzel ist die Umkehrung des Quadrierens. Wir fragen: Welche Zahl mal sich selbst ergibt A?]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a = sqrt(196 "cm"^2) $],
    [#text(size: 9pt)[Jetzt setzen wir unseren Wert für A ein. Die Fläche ist 196 cm². Wir ziehen die Quadratwurzel aus 196 cm².]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a = 14 "cm" $],
    [#text(size: 9pt)[Die Quadratwurzel aus 196 ist 14, denn 14 mal 14 ergibt 196. Die Wurzel aus cm² ist cm. Die Seitenlänge des Quadrats beträgt also 14 cm. Super!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 7
#text(size: 10pt, style: "italic")[Ein Dreieck hat die Fläche A = 91 mm² und die Höhe h = 13 mm. Berechne die Grundseite g.]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Wir kennen die Fläche A = 91 mm² und die Höhe h = 13 mm. Gesucht ist die Grundseite g. Die Formel für die Dreiecksfläche lautet A = ½ · g · h. Um g zu berechnen, müssen wir die Formel umstellen. Zuerst multiplizieren wir mit 2, dann teilen wir durch h. Schritt für Schritt schaffen wir das gemeinsam!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = (1/2) dot g dot h $],
    [#text(size: 9pt)[Das ist die Formel für die Dreiecksfläche. Die Fläche ist die Hälfte von Grundseite mal Höhe. Das ½ ist da, weil ein Dreieck die halbe Fläche eines Rechtecks mit gleicher Grundseite und Höhe hat.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ 2 dot A = g dot h $],
    [#text(size: 9pt)[Um das ½ loszuwerden, multiplizieren wir beide Seiten mit 2. Links haben wir dann 2 mal A, rechts verschwindet die ½ und es bleibt g mal h. Das macht die Formel einfacher!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ g dot h = 2 dot A $],
    [#text(size: 9pt)[Wir tauschen die Seiten, damit g links steht. Das sieht ordentlicher aus und wir sehen besser, was wir als nächstes tun müssen.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ g = (2 dot A) / h $],
    [#text(size: 9pt)[Jetzt teilen wir beide Seiten durch h. So steht g ganz alleine auf der linken Seite. Das ist unser Ziel: g alleine zu haben!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ g = (2 dot 91 "mm"^2) / (13 "mm") $],
    [#text(size: 9pt)[Wir setzen unsere Werte ein: A ist 91 mm² und h ist 13 mm. Im Zähler rechnen wir 2 mal 91.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ g = (182 "mm"^2) / (13 "mm") $],
    [#text(size: 9pt)[2 mal 91 ergibt 182. Jetzt müssen wir noch 182 durch 13 teilen. Das ist der letzte Rechenschritt!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ g = 14 "mm" $],
    [#text(size: 9pt)[182 geteilt durch 13 ergibt 14. Die Grundseite des Dreiecks beträgt also 14 mm. Toll gemacht!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 8
#text(size: 10pt, style: "italic")[Berechne die fehlenden Größen der Parallelogramme.]

#v(0.5em)
#align(center)[
#table(
  columns: 3,
  align: center + horizon,
  stroke: 0.5pt,
  inset: 8pt,
  [*a*], [*h*], [*A*],
  [#text(fill: rgb("#1e8449"))[19 cm]], [#text(fill: rgb("#1e8449"))[7 cm]], [#text(fill: rgb("#1e8449"))[133 cm²]],
  [#text(fill: rgb("#1e8449"))[13 m]], [#text(fill: rgb("#1e8449"))[11 m]], [#text(fill: rgb("#1e8449"))[143 m²]],
  [#text(fill: rgb("#1e8449"))[48 mm]], [#text(fill: rgb("#1e8449"))[13 mm]], [#text(fill: rgb("#1e8449"))[624 mm²]],
  [#text(fill: rgb("#1e8449"))[21 cm]], [#text(fill: rgb("#1e8449"))[8,5 cm]], [#text(fill: rgb("#1e8449"))[178,5 cm²]],
)
]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Bei einem Parallelogramm gilt: A = a · h. Die Fläche ist Grundseite mal Höhe. Wenn die Fläche gesucht ist, multiplizieren wir. Wenn eine Seite oder die Höhe gesucht ist, müssen wir die Formel umstellen und teilen. In jeder Zeile sind andere Werte gegeben - lies genau nach, was du berechnen sollst!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #v(8pt)
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
    [#text(weight: "bold", size: 11pt)[Zeile 1:]],
    [#text(size: 10pt)[Gegeben sind a = 19 cm und h = 7 cm. Gesucht ist die Fläche A. Hier müssen wir nur multiplizieren!]],
  )
]
#v(6pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = a dot h = 19 "cm" dot 7 "cm" = 133 "cm"^2 $],
    [#text(size: 9pt)[Wir setzen ein und rechnen: 19 mal 7 ergibt 133. Die Fläche beträgt 133 Quadratzentimeter. Das war der einfachste Fall!]],
  )
]
#v(4pt)

#v(8pt)
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
    [#text(weight: "bold", size: 11pt)[Zeile 2:]],
    [#text(size: 10pt)[Gegeben sind h = 11 m und A = 143 m². Gesucht ist die Grundseite a. Wir müssen die Formel umstellen!]],
  )
]
#v(6pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a = A / h = (143 "m"^2) / (11 "m") = 13 "m" $],
    [#text(size: 9pt)[Aus A = a · h wird a = A / h. Wir teilen die Fläche durch die Höhe: 143 durch 11 ergibt 13. Die Grundseite ist 13 Meter.]],
  )
]
#v(4pt)

#v(8pt)
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
    [#text(weight: "bold", size: 11pt)[Zeile 3:]],
    [#text(size: 10pt)[Gegeben sind a = 48 mm und A = 624 mm². Gesucht ist die Höhe h. Wieder umstellen!]],
  )
]
#v(6pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ h = A / a = (624 "mm"^2) / (48 "mm") = 13 "mm" $],
    [#text(size: 9pt)[Aus A = a · h wird h = A / a. Wir teilen die Fläche durch die Grundseite: 624 durch 48 ergibt 13. Die Höhe ist 13 Millimeter.]],
  )
]
#v(4pt)

#v(8pt)
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
    [#text(weight: "bold", size: 11pt)[Zeile 4:]],
    [#text(size: 10pt)[Gegeben sind h = 8,5 cm und A = 178,5 cm². Gesucht ist die Grundseite a. Hier rechnen wir mit Kommazahlen!]],
  )
]
#v(6pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ a = A / h = (178,5 "cm"^2) / (8,5 "cm") = 21 "cm" $],
    [#text(size: 9pt)[Wir teilen die Fläche durch die Höhe: 178,5 durch 8,5 ergibt 21. Die Grundseite ist 21 cm. Auch mit Kommazahlen klappt das!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 9
#text(size: 10pt, style: "italic")[Zeichne das Dreieck ABC mit den Eckpunkten A(2|1), B(9|1) und C(5|8) in das Koordinatensystem ein. Berechne anschließend die Grundseite g, die Höhe h und die Fläche A des Dreiecks. (1 Einheit = 1 cm)]

#v(0.5em)
#align(center)[#cetz.canvas(length: 0.7cm, {
  import cetz.draw: *

  let max_x = 10
  let max_y = 10

  // Grid lines (light gray)
  set-style(stroke: 0.3pt + rgb("#dddddd"))
  for x in range(0, max_x + 1) {
    line((x, 0), (x, max_y))
  }
  for y in range(0, max_y + 1) {
    line((0, y), (max_x, y))
  }

  // Axes (black)
  set-style(stroke: 0.8pt + black)
  line((-0.3, 0), (max_x + 0.5, 0), mark: (end: ">"))
  line((0, -0.3), (0, max_y + 0.5), mark: (end: ">"))

  // Axis labels
  content((max_x + 0.7, 0), [$x$], anchor: "west")
  content((0, max_y + 0.7), [$y$], anchor: "south")

  // Tick marks and numbers on x-axis
  for x in range(1, max_x + 1) {
    line((x, -0.1), (x, 0.1), stroke: 0.5pt)
    content((x, -0.4), [#text(size: 8pt)[#str(x)]], anchor: "north")
  }

  // Tick marks and numbers on y-axis
  for y in range(1, max_y + 1) {
    line((-0.1, y), (0.1, y), stroke: 0.5pt)
    content((-0.4, y), [#text(size: 8pt)[#str(y)]], anchor: "east")
  }

  // Origin label
  content((-0.3, -0.3), [#text(size: 8pt)[0]], anchor: "north-east")

  // Points and shape will be drawn by the student
  
  // Draw shape
  set-style(stroke: 1.5pt + rgb("#2e86ab"), fill: rgb("#2e86ab").transparentize(80%))
  line((2, 1), (9, 1), (5, 8), close: true)

  // Point A
  set-style(stroke: none, fill: rgb("#d62828"))
  circle((2, 1), radius: 0.12)
  content((2 + 0.3, 1 + 0.3), [#text(size: 9pt, weight: "bold")[A]], anchor: "south-west")

  // Point B
  set-style(stroke: none, fill: rgb("#d62828"))
  circle((9, 1), radius: 0.12)
  content((9 + 0.3, 1 + 0.3), [#text(size: 9pt, weight: "bold")[B]], anchor: "south-west")

  // Point C
  set-style(stroke: none, fill: rgb("#d62828"))
  circle((5, 8), radius: 0.12)
  content((5 + 0.3, 8 + 0.3), [#text(size: 9pt, weight: "bold")[C]], anchor: "south-west")

})]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Zuerst zeichnen wir die drei Punkte A(2|1), B(9|1) und C(5|8) ins Koordinatensystem ein und verbinden sie zu einem Dreieck. Die Grundseite g ist die Seite AB auf der x-Achse, sie geht von x=2 bis x=9. Die Höhe h ist der senkrechte Abstand von C zur Grundseite, das ist die Differenz der y-Werte. Dann berechnen wir die Fläche mit A = ½ · g · h.]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ g = 9 - 2 = 7 "cm" $],
    [#text(size: 9pt)[Die Grundseite AB liegt waagerecht auf y = 1. Sie geht von x = 2 (Punkt A) bis x = 9 (Punkt B). Die Länge ist die Differenz: 9 minus 2 ergibt 7 cm. Das können wir direkt im Koordinatensystem abzählen!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ h = 8 - 1 = 7 "cm" $],
    [#text(size: 9pt)[Die Höhe ist der senkrechte Abstand von der Spitze C zur Grundseite AB. Die Grundseite liegt bei y = 1, die Spitze C bei y = 8. Die Höhe ist also 8 minus 1 gleich 7 cm. Auch das können wir abzählen!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = (1/2) dot g dot h $],
    [#text(size: 9pt)[Jetzt berechnen wir die Fläche mit der Dreiecksformel. Die Fläche ist die Hälfte von Grundseite mal Höhe.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = (1/2) dot 7 "cm" dot 7 "cm" $],
    [#text(size: 9pt)[Wir setzen unsere Werte ein: g = 7 cm und h = 7 cm. Zuerst rechnen wir 7 mal 7.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = (1/2) dot 49 "cm"^2 $],
    [#text(size: 9pt)[7 mal 7 ergibt 49 Quadratzentimeter. Jetzt müssen wir noch durch 2 teilen, also die Hälfte nehmen.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = 24,5 "cm"^2 $],
    [#text(size: 9pt)[Die Hälfte von 49 ist 24,5. Die Fläche des Dreiecks beträgt also 24,5 Quadratzentimeter. Sehr gut gemacht!]],
  )
]
#v(4pt)

]

#v(0.5em)


== Aufgabe 10
#text(size: 10pt, style: "italic")[Familie Yilmaz möchte ihr Wohnzimmer mit einem neuen Teppich auslegen. Das Wohnzimmer ist rechteckig und hat die Maße 6,3 m Länge und 4,8 m Breite. Der gewünschte Teppichboden kostet 27 Euro pro Quadratmeter. Außerdem möchten sie eine Fußleiste um den gesamten Raum anbringen (die Türbreite von 85 cm wird ausgespart). Die Fußleiste kostet 8 Euro pro Meter. Berechne die Fläche des Zimmers, den Umfang, die Länge der benötigten Fußleiste und die Gesamtkosten für Teppich und Fußleiste.]

#pad(left: 1em)[
  #text(weight: "bold", fill: rgb("#1e8449"))[Lösungsweg:]
  #v(0.2em)
  #text(size: 10pt)[Das ist eine Sachaufgabe mit mehreren Schritten! Wir haben ein rechteckiges Wohnzimmer mit a = 6,3 m und b = 4,8 m. Zuerst berechnen wir die Fläche für den Teppich mit A = a · b. Dann berechnen wir den Umfang mit U = 2·a + 2·b für die Fußleiste. Von diesem Umfang ziehen wir die Türbreite ab. Zum Schluss berechnen wir die Kosten. Schritt für Schritt schaffen wir das!]
  #v(0.4em)
  #text(weight: "bold", fill: rgb("#1e8449"))[Rechnung:]
  #v(0.3em)
  #block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = a dot b $],
    [#text(size: 9pt)[Zuerst berechnen wir die Fläche des Wohnzimmers. Diese brauchen wir, um zu wissen, wie viel Quadratmeter Teppich Familie Yilmaz kaufen muss.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = 6,3 "m" dot 4,8 "m" $],
    [#text(size: 9pt)[Wir setzen die Maße des Zimmers ein: Länge 6,3 m mal Breite 4,8 m. Das ist eine Kommarechnung, aber das schaffen wir!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ A = 30,24 "m"^2 $],
    [#text(size: 9pt)[6,3 mal 4,8 ergibt 30,24. Das Wohnzimmer hat also eine Fläche von 30,24 Quadratmetern. So viel Teppich wird benötigt!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = 2 dot a + 2 dot b $],
    [#text(size: 9pt)[Jetzt berechnen wir den Umfang des Zimmers. Das ist die Strecke einmal um das ganze Zimmer herum, wo die Fußleiste hin soll.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = 2 dot 6,3 "m" + 2 dot 4,8 "m" $],
    [#text(size: 9pt)[Wir setzen ein: 2 mal 6,3 m plus 2 mal 4,8 m. Erst die Multiplikationen, dann die Addition!]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ U = 12,6 "m" + 9,6 "m" = 22,2 "m" $],
    [#text(size: 9pt)[2 mal 6,3 ist 12,6 und 2 mal 4,8 ist 9,6. Zusammen ergibt das 22,2 Meter Umfang.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ "Fußleiste" = 22,2 "m" - 0,85 "m" = 21,35 "m" $],
    [#text(size: 9pt)[Aber die Tür braucht keine Fußleiste! Wir ziehen die Türbreite von 85 cm = 0,85 m ab. Es werden also 21,35 m Fußleiste benötigt.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ "Kosten Teppich" = 30,24 "m"^2 dot 27 "Euro"/"m"^2 = 816,48 "Euro" $],
    [#text(size: 9pt)[Der Teppich kostet 27 Euro pro Quadratmeter. Wir rechnen: 30,24 mal 27 ergibt 816,48 Euro für den Teppich.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#f8f9fa"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#cccccc")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ "Kosten Fußleiste" = 21,35 "m" dot 8 "Euro"/"m" = 170,80 "Euro" $],
    [#text(size: 9pt)[Die Fußleiste kostet 8 Euro pro Meter. Wir rechnen: 21,35 mal 8 ergibt 170,80 Euro für die Fußleiste.]],
  )
]
#v(4pt)

#block(
  fill: rgb("#e8f6e9"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stroke: (left: 3pt + rgb("#1e8449")),
  width: 100%,
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 16pt,
    align: (left + horizon, left + horizon),
    [$ "Gesamtkosten" = 816,48 "Euro" + 170,80 "Euro" = 987,28 "Euro" $],
    [#text(size: 9pt)[Zum Schluss addieren wir beide Kosten: 816,48 plus 170,80 ergibt 987,28 Euro. Familie Yilmaz muss insgesamt 987,28 Euro bezahlen. Fertig!]],
  )
]
#v(4pt)

]

#v(0.5em)

