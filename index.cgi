#!/usr/bin/env python3

import time
print("Content-Type: text/html\n\n")  # html markup follows

timeStr = time.strftime("%c") # obtains current time

htmlFormat = """
<html>
   <head>
        <title>Betriebskostenabrechnung einfach gemacht</title>
        <link rel="icon" type="image/png" href="/images/logo-1.png">
  </head>
<body>
  <p>The current Central date and time is:  {timeStr}</p>
</body>
</html> """

print(htmlFormat.format(**locals()))  # see {timeStr} embedded above