title: Artikel im Online Magazin Dr. Web
duration: März 2009
tags: [ Infrastructure, ]
date: 2010-03-01 12:00
---
Wir haben es probiert und einige Seiten bekannter Marken verglichen:
ein Teil der Web-Nutzer muss sich über Ladezeiten von 20 Sekunden und mehr ärgern.
Warum ist das so? Wann ist das wichtig? Und worauf muss man achten, um schnellere Zugriffe zu ermöglichen.

Physiker und Mathematiker geben, wenn man sie nach der Geschwindigkeit fragt, gerne die bekannte Formel wieder:
Geschwindigkeit = zurückgelegter Weg / Zeit.
Internet-User kürzen diese Formel so circa auf: **Geschwindigkeit = 1 / vergangene Zeit bis zur Darstellung der gewünschten Seite**.
Theoretisch braucht das Signal bei Lichtgeschwindigkeit von Europa ans andere Ende der Welt – zum Beispiel nach China – weit unter einer Sekunde.
In der Praxis werden Seiten jedoch bedeutend langsamer geladen. [Durchschnittlich 50 Objekte](http://www.websiteoptimization.com/speed/tweak/average-web-page/) müssen transferiert werden – wobei meist schon das HTML Gerüst mit einer Größe von 312 kB aufwartet.
Bedenkt man dann auch, dass die HTTP/1.1 Spezifikation vorschlägt, [lediglich 2 Objekte parallel](http://developer.yahoo.com/performance/rules.html) zu laden, so wundert es nicht, dass beim Testen Ladezeiten von über 20 Sekunden keine Seltenheit waren.

## Aber wen interessiert das?

Naja, man nehme zum Beispiel den bekannten Sportartikelhersteller Nike. Dieser buhlt weltweit um Kunden und somit auch um Internetnutzer.
Somit müssen sich internationale Marken auch damit befassen, wie schnell beziehungsweise langsam deren Seiten – zum Beispiel – in China geöffnet werden.

Speziell, wer einen Online-Shop betreibt, sollte sich Gedanken zum Thema Geschwindigkeit machen, da Veröffentlichungen von Google und Amazon ein ähnliches Bild zeichnen:

* Um **0,9 Sekunden** langsamerer Seitenaufbau geht bei **Google** mit einem Traffic- und auch Werbeinnahmen**verlust** von **20%** einher.
* **Amazon**‘s Experimente zeigen, dass pro **0,1 Sekunden** das Geschäft um **1% zurückgeht**.

> Quelle: O’Reilly Media, Inc. (15.Juli 2008) – Website Optimization (ISBN: 978-0-596-51508-9) – Kapitel: Web Performance Optimization

Für reine Informationsseiten ist es natürlich um einiges schwerer, relevante und messbare Daten zu erhalten.
Generell gilt sicher, dass je wichtiger dem User der zu erwartende Inhalt ist, desto länger ist er gewillt auf diesen zu warten.
Eine [Studie](http://sigs.aisnet.org/sighci/bit04/BIT_Nah.pdf) aus dem Jahr 2004 gibt die „Tolerable-Waiting-Time” ohne Feedback mit 13 Sekunden an, mit angezeigtem Fortschrittsbalken mit 38 Sekunden für nicht-funktionierende Links an.

Somit lässt sich die Toleranz gegenüber der Wartezeit am einfachsten durch User-Feedback erhöhen – wobei Breitbandnutzer sicher auch andere Erwartungen mit sich bringen als Besitzer eines Einwählmodems.

Weiterführende Links:

* [The Psychology of Web Performance](http://www.websiteoptimization.com/speed/tweak/psychology-web-performance/)
* [Consumer Reaction to a Poor Online Shopping Experience](http://www.akamai.com/dl/whitepapers/Site_Abandonment_Final_Report.pdf?campaign_id=1-SQIB1curl=/dl/whitepapers/Site_Abandonment_Final_Report.pdf&curl=/dl/whitepapers/Site_Abandonment_Final_Report.pdf&solcheck=1&)
* Video: [Steve Souders — High Performance Web Sites: 14 Rules for Faster Pages](http://video.yahoo.com/video/play?vid=1040890)

## Und wie schnell sind Seiten internationaler Marken wirklich?

Um dies herauszufinden, habe ich in den letzten Tagen einige Messungen durchgeführt und mir die Ergebnisse notiert.

Dabei habe ich Seitenaufrufe aus Europa (London) und Seitenaufrufe aus China (Kanton) gegenübergestellt.
* [Dolce&Gabbana](http://www.dolcegabbana.com/) 9,2 sec / 39,8 sec
* [Gucci](http://www.gucci.com/) 5,9 sec / 82,0 sec
* [Nike](http://www.nike.com/) 1,9 sec / 2,1 sec
* [Oakley](http://www.oakley.com/) 6,6 sec / 40,0 sec
* [Rolex](http://www.rolex.com/) 11,4 sec / 21,9 sec

Die ermittelten Werte habe ich mit Hilfe des Webdienstes [Gomez](http://www.gomeznetworks.com/) messen lassen, jeweils dreimal an unterschiedlichen Tagen und zu unterschiedlichen Zeiten von einem Server in London und einem in Kanton. Das Ergebnis sind die Ladezeiten der Startseiten beziehungsweise der Mittelwert – jedoch ohne Berücksichtigung der unterschiedlichen Seitengrössen und Anzahl der geladenen Inhaltsobjekte.

Da ich eingangs Beobachtungen von Amazon und Google zitiert habe, sollen zum Vergleich auch deren Startseiten dem gleichen Prozedere unterzogen werden:

* [Google](http://www.google.com/) 0,2 sec / 0,1 sec
* [Amazon](http://www.amazon.com/) 3,5 sec / 14,6 sec

## Die Moral von der Geschicht’?

Nach meiner Erfahrung mangelt es am Verständnis, dass auch das Internet – auch, wenn dies der Name anders suggeriert – nicht komplett ortsungebunden ist. Daten brauchen Zeit, um von einem Ort zum anderen zu gelangen und sogar Lichtgeschwindigkeit ist manchmal nicht schnell genug.

Um diesem Problem zu begegnen, sollte man zu allererst die eigenen Webseiten analysieren. Dies geht lokal mit dem beliebten Firefox-Plugin „[Firebug](http://getfirebug.com/)” und den Add-Ons „[YSlow](http://developer.yahoo.com/yslow/)” und „[Hammerhead](http://stevesouders.com/hammerhead/)” oder auch dem hervorragendem Windows Tool „[Fiddler](http://www.fiddlertool.com/fiddler/)“.

Nach den ersten Tests sollte man sich das eigene Werk noch einmal zur Brust nehmen und nach den von Yahoo! veröffentlichten “Best-Practices” für schnellere Webseiten Schritt für Schritt verbessern. Dabei sollte man sich vorerst mit den ersten beiden Regeln ernsthaft auseinandersetzen.

Witzigerweise haben 3 der 5 Seiten sogar die zweite Regel “Auf ein Content Delivery Network (CDN) zurückzugreifen” implementiert. Jedoch nutzt lediglich die Nike-Seite das Potential dieser zugekauften verteilten Serverlandschaft, was auch an den hervorragenden weltweiten Werten erkennbar ist. Dies legt nahe, dass ein oftmals teures CDN erst als zweite Möglichkeit angepeilt werden sollte, nachdem der Inhalt auf Geschwindigkeit optimiert wurde. Zu den alteingesessenen CDN-Anbietern wie [Akamai Technologies](http://www.akamai.com/), [Mirror Image Internet](http://www.mirror-image.com/) oder [Limelight Networks}(http://www.limelightnetworks.com/) sind übrigens vor kurzem auch die Internetgrössen [Amazon](http://aws.amazon.com/cloudfront/) und [Google](http://appengine.google.com/) dazugestossen.

Für Tests aus entfernteren Regionen eignen sich Webservices wie [Gomez](http://www.gomeznetworks.com/) oder [Watchmouse](http://www.watchmouse.com/).

Manchmal sind aber die Seiten, die getestet werden sollen, nicht öffentlich erreichbar. Dies gilt zum Beispiel für Intranet-Applikationen, die die Mitarbeiter aus dem chinesischen Tochterunternehmen nutzen sollen, jedoch ständig über langsame Seiten klagen. Für derartige Situationen bietet sich ein zuverlässigen Proxy-Server bei den Endnutzern an, mit dem man anschließend beobachten kann, wie langsam sich die Seiten tatsächlich aufbauen, nachdem sie um den halben Globus gejagt wurden. Nach dieser vermeintlichen Grenzerfahrung lässt sich vermutlich so manch leidvolles Klagen aus dem entfernten Land besser verstehen und hoffentlich auch in Zukunft verhindern.


----

Publiziert bei:

* http://www.drweb.de/magazin/wurden-sie-20-sekunden-auf-eine-webseite-warten/

