#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os, sys, getpass
from datetime import *

####################################################################################################
### make.py : script d'aide à la compilation de programme en C avec Python3 !
### juin 2022 - sous license MIT - MEYER Daniel
####################################################################################################
### contact : meyer.daniel67@protonmail.com OU https://t.me/dnl_85
### dépôt   : https://github.com/dnl-85/C_for_all
####################################################################################################

editeur = "notepadqq"

####################################################################################################
### fonction 'main' principale, celle qui va gérer le script lors d'un appel depuis $bash
####################################################################################################
def main(options):
    if "-all" in options:
        compile_linux(options[2])
        compile_win32(options[2])
        compile_win64(options[2])
        zip_compile(options[2].replace(".c", ""))
        print("... terminé ! ...")
    elif "-l" in options:
        compile_linux(options[2])
        zip_compile(options[2].replace(".c", ""))
    elif "-w32" in options:
        compile_win32(options[2])
        zip_compile(options[2].replace(".c", ""))
    elif "-w64" in options:
        compile_win64(options[2])
        zip_compile(options[2].replace(".c", ""))
    elif "-h" in options:
        aide()
    elif "-i" in options:
        info()
    elif "-start" in options:
        start_projet(f"{options[2]}")
    elif "-install" in options:
        install_progs()
    else:
        print("... PAS D'OPTIONS SPECIFIEES! ...")

def horodatage():
    jour = date.today()
    heure = datetime.now()
    moment = jour.strftime("%d_%m_%Y") + "_" + heure.strftime("%H:%M:%S")
    return moment

def compile_linux(projet):
    print("... compilation de la version linux 64bits ...")
    os.system(f"gcc -Wall -o exe/build_l64 src/{projet} -lm")
    print("... version linux 64bits générée ...")

def compile_win32(projet):
    print("... compilation de la version windows 32bits ...")
    os.system(f"i686-w64-mingw32-gcc -o exe/build_w32.exe src/{projet}")
    print("... version windows 32bits générée ...")

def compile_win64(projet):
    print("... compilation de la version windows 64bits ...")
    os.system(f"x86_64-w64-mingw32-gcc -o exe/build_w64.exe src/{projet}")
    print("... version windows 64bits générée ...")

def zip_compile(projet):
    print("... création d'un zip contenant votre projet et vos exécutables ...")
    try:
        os.system(f"rm pack/{projet}.zip")
    except:
        print("... le pack initial n'existe pas encore ...")
    finally:
        os.system(f"zip pack/{projet}.zip -r exe/")
        os.system(f"zip pack/{projet}.zip -r inc/")
        os.system(f"zip pack/{projet}.zip -r src/")
        os.system(f"zip pack/{projet}.zip -r doc/")
        os.system(f"zip pack/{projet}.zip *.*")

def install_progs():
    print("... installation de gcc et mingw si absents ...")
    print(" > 1. installation de gcc...")
    os.system("sudo apt-get install gcc")
    print(" > 2. installation de mingw-w64...")
    os.system("sudo apt-get install mingw-w64")
    print("... OK! ...")
    
####################################################################################################
### la fonction start_projet contient le code initial si l'on souhaite démarrer un projet, ce code
### initial peut être changé selon les besoins les plus courants de chacun... ceci est ma version ;)
####################################################################################################
def start_projet(projet):
    code_initial = f"""#include "../inc/{projet}.h" """ + """

int main(void)
{
    printf("Hello, World !\\n");
    return 0;
}
"""
    header = """#include <assert.h>
#include <complex.h>
#include <ctype.h>
#include <errno.h>
#include <fenv.h>
#include <float.h>
#include <inttypes.h>
#include <iso646.h>
#include <limits.h>
#include <locale.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <signal.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stddef.h>
#include <setjmp.h>
#include <time.h>
#include <tgmath.h>
#include <wchar.h>
#include <wctype.h>
"""
    license_mit = f"""Copyright - {horodatage()} \n""" + f"""by : {getpass.getuser()} \n""" + """ 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the 'Software'), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of
the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
    readme_md = f"""# README : {projet}.""" + """
### description du projet C ici présent.
-----
  donnez ici une description et documentation précise de votre projet en C et comment il fonctionne
  """

    os.system(f"mkdir {projet}")
    os.system(f"mkdir {projet}/exe")
    os.system(f"mkdir {projet}/doc")
    os.system(f"mkdir {projet}/src")
    os.system(f"mkdir {projet}/inc")
    os.system(f"mkdir {projet}/pack")
    os.system(f"cp make.py {projet}/make.py")
    
    with open (f"{projet}/inc/{projet}.h", "w") as fichier:
        fichier.write(header)
    
    with open(f"{projet}/src/{projet}.c", "w") as fichier:
        fichier.write(code_initial)

    with open(f"{projet}/doc/LICENSE", "w") as fichier:
        fichier.write(license_mit)

    with open(f"{projet}/doc/README.md", "w") as fichier:
        fichier.write(readme_md)
        

    if editeur != "nano":
        os.system(f"{editeur} --new-window {projet}/src/{projet}.c --new-window {projet}/inc/{projet}.h")
    else:
        os.system(f"nano {projet}/src/{projet}.c")

####################################################################################################
### fonctions d'aide & d'infos
####################################################################################################
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
>  python3 make.py -install              : va installer gcc et mingw-w64 sur votre système.

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
