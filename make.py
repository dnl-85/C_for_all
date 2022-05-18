#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os, sys, getpass
from datetime import *

####################################################################################################
### make.py : script d'aide à la compilation de programme en C avec Python3 !
### mai 2022 - sous license MIT - MEYER Daniel
####################################################################################################
### contact : meyer.daniel67@protonmail.com OU https://t.me/dnl_85
### dépôt   : https://github.com/dnl-85/C_for_all
####################################################################################################

def main(options):
    if "-all" in options:
        dossier = dossier_sortie(f"{options[2]}_allsys__")
        compile_linux(dossier, options[2])
        compile_win32(dossier, options[2])
        compile_win64(dossier, options[2])
        copie_original(dossier, options[2])
        print("... terminé ! ...")
    elif "-l" in options:
        dossier = dossier_sortie(f"{options[2]}_lnx64__")
        compile_linux(dossier, options[2])
        copie_original(dossier, options[2])
    elif "-w32" in options:
        dossier = dossier_sortie(f"{options[2]}_win32__")
        compile_win32(dossier, options[2])
        copie_original(dossier, options[2])
    elif "-w64" in options:
        dossier = dossier_sortie(f"{options[2]}_win64__")
        compile_win64(dossier, options[2])
        copie_original(dossier, options[2])
    elif "-h" in options:
        aide()
    elif "-i" in options:
        info()
    elif "-start" in options:
        start_projet(f"{options[2]}")
    else:
        print("... PAS D'OPTIONS SPECIFIEES! ...")

def horodatage():
    jour = date.today()
    heure = datetime.now()
    login = getpass.getuser()
    moment = login + "_" + jour.strftime("%d_%m_%Y") + "_" + heure.strftime("%H:%M:%S")
    return moment

def dossier_sortie(nom_projet):
    print("création du dossier de destination de compilation ...")
    dossier = f"{nom_projet}__{horodatage()}"
    print("-> le dossier de destination de votre compilation sera : ", dossier)
    os.system(f"mkdir -p {dossier}")
    print("... OK! ...")
    return dossier

def compile_linux(dossier, projet):
    print("... compilation de la version linux 64bits ...")
    os.system(f"gcc -Wall -o {dossier}/{projet}_build_lnx64 {projet}")
    print("... version linux 64bits générée ...")

def compile_win32(dossier, projet):
    print("... compilation de la version windows 32bits ...")
    os.system(f"i686-w64-mingw32-gcc -o {dossier}/{projet}_build_win32.exe {projet}")
    print("... version windows 32bits générée ...")

def compile_win64(dossier, projet):
    print("... compilation de la version windows 64bits ...")
    os.system(f"x86_64-w64-mingw32-gcc -o {dossier}/{projet}_build_win64.exe {projet}")
    print("... version windows 64bits générée ...")

def copie_original(dossier, projet):
    print("... copie du programme C source utilisé pour la compilation ...")
    os.system(f"cp -u {projet} {dossier}")
    print("... OK! ...")

### la fonction start_projet contient le code initial si l'on souhaite démarrer un projet, ce code
### initial peut être changé selon les besoins les plus courants de chacun... ceci est ma version ;)
def start_projet(projet):
    code_initial = """
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include <strings.h>

int main(void) {
    printf("Hello, World !\n");
    return 0;
    }
"""
    with open(f"{projet}.c", "a") as fichier:
        fichier.write(code_initial)
    print("... votre projet est initialisé ...")
    os.system("sleep 1")
    os.system(f"nano {projet}.c")

def aide():
    print("""
make.py - script d'aide à la compilation de programme C sous Python3.
commandes :
>  python3 make.py -all [programme.c]    : va compiler le programme C pour tous les systèmes.
>  python3 make.py -l [programme.c]      : va compiler le programme C pour Linux en 64bits uniquement.
>  python3 make.py -w32 [programme.c]    : va compiler le programme C pour Windows en 32bits uniquement.
>  python3 make.py -w64 [programme.c]    : va compiler le programme C pour Windows en 64bits uniquement.
>  python3 make.py -h                    : va afficher ce message d'aide.
>  python3 make.py -i                    : va afficher les informations concernant ce script.
>  python3 make.py -start [projet]       : va créer un nouveau programme C. 

NOTE : inutile de spécifier le nom du fichier source en C entre [.] !
par exemple, si votre fichier source s'appelle 'essai.c' et que vous voulez compiler pour tous les systèmes,
il suffit de taper :
    python3 make.py -all essai.c

NOTE : dans le cas d'un nouveau projet, inutile de spécifier le suffixe du fichier, donnez juste le nom
de votre programme; ce script se chargera du reste... exemple:
    python3 make.py -start nouveau
ceci va créer un programme 'nouveau.c' dans le répertoire courant, et l'ouvrir avec Nano.

RAPPEL : ce script a besoin d'avoir gcc et mingw installés sur la machine !

Bonne utilisation. Daniel.
""")

def info():
    print("""
make.py - script d'aide à la compilation de programme C sous Python3.
version Mai 2022  -  sous license MIT  -  par MEYER Daniel.
contact : meyer.daniel67@protonmail.com OU https://t.me/dnl_85
dépôt   : https://github.com/dnl-85/C_for_all
""")

####################################################################################################
### lancement du programme
####################################################################################################
main(sys.argv)
