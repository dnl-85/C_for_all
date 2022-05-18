# Comment compiler un programme en C en executable pour Windows en 32bits ou 64bits sous Linux
### ... et comment se faire un script pour générer sans effort un exécutable depuis un programme C sous Linux ...
-----

pour compiler un programme exécutable pour windows sous un système linux, il faut premièrement installer mingw-w64 et gcc sous Linux via les commandes bash suivantes :  
    
    sudo apt-get install mingw-w64
    sudo apt-get install gcc
    
en cas de doute, il est possible de vérifier la présence de ces commandes avant de continuer :

    gcc --version
    i686-w64-mingw32-gcc --version
    x86_64-w64-mingw32-gcc --version

pour compiler en 32 bits, voilà la commande :  
    
    i686-w64-mingw32-gcc -o nom_du_programme_32.exe nom_du_programme_C.c

pour compiler en 64 bits, voilà la commande :  
    
    x86_64-w64-mingw32-gcc -o nom_du_programme_64.exe nom_du_programme_C.c

-----

pour se simplifier le processus de façon générale, le script bash présent dans ce dépôt permet de compiler un programme C pour Linux, Windows 32bits et Windows 64bits :  
- make_all va compiler et créer un exécutable pour Linux & Windows en utilisant gcc, mingw-w64 et mingw. les exécutables prendront respectivement les noms de *'nom-du-programme.c_build_lnx64'*, *'nom-du-programme.c_build_win64.exe'* et *'nom-du-programme.c_build_win32.exe'* et seront dans un dossier à part. le nom du dossier va se générer automatiquement en portant le nom du programme source C, ainsi que la date et l'heure du 'build'. une copie du programme source en C va également être intégrer dans le dossier de 'build' (histoire de garder une trace).

        ./make_all nom_du_programme.c

pour vérifier le résultat et l'exécutabilité de votre programme pour windows sous linux, utilisez Wine, qui est juste excellent pour ça !  

et voilà ! ... d'une pierre , 3 coups !

Daniel, le 17/05/2022.  

