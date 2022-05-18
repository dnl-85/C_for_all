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

pour se simplifier le processus de façon générale, les 3 scripts bash présents dans ce dépôt permettent de compiler un programme C selon le système de destination de l'exécutable :  
- make_lnx : va compiler et créer un exécutable pour Linux en utilisant la commande gcc. l'exécutable prendra le nom de *'nom-du-programme.c_build_lnx64'* et sera dans le même dossier que le programme source.  
    
        ./make_lnx nom_du_programme.c
    
- make_win : va compiler et créer un exécutable pour Windows en utilisant mingw-w64. l'exécutable prendre le nom de *'nom-du-programme.c_build_win64.exe'* et sera dans le même dossier que le programme source.  
    
        ./make_win nom_du_programme.c
    
- make_all : va compiler et créer un exécutable pour Linux & Windows en utilisant gcc & mingw-w64. les exécutables prendront respectivement les noms de *'nom-du-programme.c_build_lnx64'* et *'nom-du-programme.c_build_win64.exe'* et seront dans le même dossier que le programme source.

        ./make_all nom_du_programme.c

et voilà ! ...  

Daniel, le 17/05/2022.  

