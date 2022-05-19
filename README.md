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

pour se simplifier le processus de façon générale, le script en Python3 présent dans ce dépôt permet de compiler un programme C pour Linux, Windows 32bits et Windows 64bits. son utilisation est très simple depuis un terminal $bash:  

    >  python3 make.py -all [programme.c]    : va compiler le programme C pour tous les systèmes.
    >  python3 make.py -l [programme.c]      : va compiler le programme C pour Linux en 64bits uniquement.
    >  python3 make.py -w32 [programme.c]    : va compiler le programme C pour Windows en 32bits uniquement.
    >  python3 make.py -w64 [programme.c]    : va compiler le programme C pour Windows en 64bits uniquement.
    >  python3 make.py -h                    : va afficher ce message d'aide.
    >  python3 make.py -i                    : va afficher les informations concernant ce script.
    >  python3 make.py -start [projet]       : va créer un nouveau programme C. 
    >  python3 make.py -install              : va installer gcc et mingw-w64 sur votre système.

NOTE : inutile de spécifier le nom du fichier source en C entre [.] !  
par exemple, si votre fichier source s'appelle 'essai.c' et que vous voulez compiler pour tous les systèmes, il suffit de taper :  

    python3 make.py -all essai.c

NOTE : dans le cas d'un nouveau projet, inutile de spécifier le suffixe du fichier, donnez juste le nom de votre programme; ce script se chargera du reste... exemple:  

    python3 make.py -start nouveau

ceci va créer un programme 'nouveau.c' dans le répertoire courant, et l'ouvrir avec Nano.  
le script 'make.py' peut être modifié et adapté au besoin de chacun.  

-----

pour finir et pour vérifier le résultat et l'exécutabilité de votre programme pour windows sous linux, je vous recommande d'utiliser Wine, qui est juste excellent pour ça !  

et voilà ! ...  

Daniel, le 17/05/2022.  

