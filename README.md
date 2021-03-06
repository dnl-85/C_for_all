# Comment compiler un programme en C en executable pour Windows en 32bits ou 64bits sous Linux
### ... et comment se faire un script Python & $Bash pour générer sans effort un exécutable depuis un programme C sous Linux ...
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

ceci va créer un répertoire dans le répertoire courant contenant les divers fichiers .c et .h ainsi qu'une license MIT et un fichier README en markdown. les fichiers 'nouveau.c' et 'nouveau.h' vont s'ouvrir avec l'éditeur de code spécifié dans le script python (pour ma part ça sera Notepad++).   
de plus, 'make.py' va se copier dans le projet afin de servir de fichier de compilation pour le développeur par la suite. bien sûr le script 'make.py' peut être modifié et adapté au besoin de chacun. cette commande aura pour effet de créer un dossier de travail avec un ensemble de sous-dossiers afin de structurer proprement le projet :  

    nouveau/
        |---- exe/
        |---- inc/
        |        +---- nouveau.h
        |---- doc/
        |        +---- LICENSE
        |        +---- README.md
        |---- src/
        |        +---- nouveau.c
        |---- pack/
        + make.py
        
- le dossier 'exe/' va contenir les futurs compilations (exécutables) du projet.  
- le dossier 'inc/' va contenir à minima le header .h du programme, et peut être modifié à la guise du développeur.  
- le dossier 'doc/' va contenir à minima une license MIT avec le nom du login du pc du développeur et l'heure de création du projet ainsi que la documentation du programme.  
- le dossier 'src/' va contenir à minima le programme .c, lui même contenant la fonction principale 'main'.  
- le dossier 'pack/' va contenir une sauvegarde du projet, empaqueté dans une archive .zip, et ceci sera créé ou remis à jour à chaque compilation du projet.  
- et pour finir 'make.py' contient le script de compilation, se basant sur gcc et mingw comme décrit au début de cet article.  

concernant le script make.py : à chaque compilation, il va générer automatiquement une archive zip contenant l'intégralité du projet dans sa forme telle que d'écrite quelques lignes plus haut, et contenant bien sûr les exécutables dans le dossier exe/.  
pour ça, il suffit de taper la commande :

    python3 make.py -all nouveau.c
    
depuis un terminal pointant dans la racine du projet.  
note : contrairement au script shell (voir description ci-dessous), ce script python n'est pas exclusif à ce projet. il faudra néanmoins respecter la structure des dossiers pour qu'il puisse fonctionner sans erreurs et sans omettre certaines parties du projet.  

-----

en ce qui me concerne, étant accro à Linux depuis 1998 et ne me voyant pas revenir sous Windows pour développer mes projets (même sous menace de la torture), je me suis fait un petit script $bash qui génère automatiquement un dossier avec des sous-dossiers, une amorce de programme C, une amorce de header .h, un script de compilation $bash, un README en markdown et une license MIT, juste en tapant la commande suivante depuis un terminal pointant sur le dossier contenant ce script :  

    > ./make.sh nom_du_projet
    
d'emblée, le programme .c présent dans le projet va contenir une fonction main() laissant un petit 'hello world !' si on le compile et l'exécute. par exemple, si je tape :

    > ./make.sh nouveau

le terminal va changer de répertoire de travail et passer directement dans le dossier fraichement créé.  
un dossier 'nouveau' va apparaitre et contenir :  

    nouveau/
        |---- exe/
        |---- inc/
        |        +---- nouveau.h
        |---- doc/
        |        +---- LICENSE
        |        +---- README.md
        |---- src/
        |        +---- nouveau.c
        |---- pack/
        + Makefile.sh

- le dossier 'exe/' va contenir les futurs compilations (exécutables) du projet.  
- le dossier 'inc/' va contenir à minima le header .h du programme, et peut être modifié à la guise du développeur.  
- le dossier 'doc/' va contenir à minima une license MIT avec le nom du login du pc du développeur et l'heure de création du projet ainsi que la documentation du programme.  
- le dossier 'src/' va contenir à minima le programme .c, lui même contenant la fonction principale 'main'.  
- le dossier 'pack/' va contenir une sauvegarde du projet, empaqueté dans une archive .zip, et ceci sera créé ou remis à jour à chaque compilation du projet.  
- et pour finir Makefile.sh contient le script de compilation, se basant sur gcc et mingw comme décrit au début de cet article.  

comme j'utilise Notepadqq (Notepad++) comme editeur de code, mon script fini par ouvrir le programme c, le header h et README.md dans cette application, chacun dans un onglet séparé.  

concernant le script Makefile.sh : à chaque compilation, il va générer automatiquement une archive zip contenant l'intégralité du projet dans sa forme telle que d'écrite quelques lignes plus haut, et contenant bien sûr les exécutables dans le dossier exe/.  
pour ça, il suffit de taper la commande :

    ./Makefile.sh
    
depuis un terminal pointant dans la racine du projet.  
note : cette commande est exclusive à ce projet, si vous changez le nom du programme 'nouveau.c' pour un autre, ou la structure des dossiers du projet, la commande doit être modifiée manuellement en conséquence sinon elle ne fonctionnera plus...  

-----

pour finir et pour vérifier le résultat et l'exécutabilité de votre programme pour windows sous linux, je vous recommande d'utiliser Wine, qui est juste excellent pour ça !  

et voilà ! ...  

Daniel, le 17/05/2022.  

