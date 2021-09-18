#!/usr/bin/env python3

print("Content-Type: text/html\n\n")

htmlFormat = """
<html>
   <head>
        <title>Betriebskostenabrechnung einfach gemacht</title>
        <link rel="icon" type="image/png" href="/images/logo-1.png">
        <link rel="stylesheet" href="css/styles.css">
  </head>
<body>
  <h1>Betriebskostenabrechnung erstellen</h1>
  <nav>
    <ul>
      <li><a href="https://betriebskostenabrechnung-einfach-gemacht.com">Startseite</a></li>
      <li><a href="https://betriebskostenabrechnung-einfach-gemacht.com/datenschutz">Datenschutz</a></li>
      <li><a href="https://betriebskostenabrechnung-einfach-gemacht.com/kontakt">Kontakt</a></li>
    </ul>
  </nav>

  <footer>
     <p>2021 @ Christopher Wyczisk & Amit Jerochim GbR </p>
  </footer>
</body>
</html> """

print(htmlFormat)