Za pokretanje potrebno je postaviti putanju do pysrc modula i do src foldera projekta u PYTHONPATH
Putanja do pysrc zavisi od nacina na koji je instaliran PyDev plugin
Ako je PyDev instaliran
  skidanjem zip fajla i eksportovanjem u dropins folder Eclipsa, putanja je
     {Putanje do foldera PyDev plugina u dropins folderu Eclipsa}/plugins/org.python.pydev_4.5.4.201601292234/pysrc
  preko opcije Help->Install New Software
     {Putanje do Eclipsa}/plugins/org.python.pydev_4.5.4.201601292234/pysrc

     
     
 Primeri se pokrecu iz terminala u Linuxu ili command prompta u Windowsu
Pre pokretanja potrebno je proveriti da li je postavljena PYTHONPATH putanja do pysrc foldera PyDev plugina
	sa sledecim komandama
	Linux 
	
	"$PYTHONPATH"
	
	Windows
	
	echo %PYTHONPATH%

	ako vec postoji postavljena putanja do pysrc foldera
	potrebno je jos dodati putanju do src foldera u PYTHONPATH
	Linux
	export PYTHONPATH=$PYTHONPATH:{putanja_do_tim21_foldera}
	
	Windows
	set PYTHONPATH=%PYTHONPATH%;{putanja_do_tim21_foldera}

Ako nije postavljena putanja do pysrc foldera pre pokretanja se moze sa jednom naredbom postaviti putanja 
do pysrc foldera
i do src foldera

Linux
export PYTHONPATH={putanja_do_pysrc_foldera}:{putanja_do_tim21_foldera}

Windows
set PYTHONPATH={putanja_do_pysrc_foldera};{putanja_do_tim21_foldera}


Informacije za login:
	Menadzer transporta:
		username: ivan1
		password: ivan123
	Menadzer hangara:
		username: alkes
		password: men2
	Radnik:
		username: marko
		password: marko123