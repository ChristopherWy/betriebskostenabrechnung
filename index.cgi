#!/usr/bin/env python3
import cgi
import cgitb; cgitb.enable()

print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()

htmlFormat = """
<html>
   <head>
        <title>Betriebskostenabrechnung einfach gemacht</title>
        <link rel="icon" type="image/png" href="/images/logo-1.png">
        <link rel="stylesheet" href="css/style.css">
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

     <h3>Bitte Name und Alter eingeben:</h3>
     <form method="post" action="example1.cgi">
     <table border=0>
     <tr><td>Name:</td><td><input type="text" name="name"/></td></tr>
     <tr><td>Alter:</td><td><input type="text" name="age"/></td></tr>
    </table>
    <input type="submit" name="submit" value="OK"/>
    </form>

  <footer>
     <p>2021 @ Christopher Wyczisk & Amit Jerochim GbR </p>
  </footer>
</body>
</html> """

print(htmlFormat)