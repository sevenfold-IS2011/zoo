#TecWeb - gruppo zoo

Zironda: non è meglio fare un'unica tabella utenti con una colonna "tipo" invece di farne due?

Allora, va tutto nella root, senza suddivisione su cgi-bin e sarcazzo, in quanto quando consegnamo gli script dentro cgi-bin verranno linkati direttamente nella root (leggere http://www.studenti.math.unipd.it/index.php?id=corsi#c439 )... stessa cosa per public_html

facendo così possiamo tenere tutti i link relativi e poi continua a funzionare anche al momento della consegna



per installare CGI::Session:

perl -MCPAN -e shell
[qualche yes se ve lo chiede]
install CGI::Session



roba utile:

http://stackoverflow.com/questions/1305749/how-do-i-create-an-xml-template-in-perl

tanta roba su come gestire l'xml in perl:
http://perl-xml.sourceforge.net/faq/