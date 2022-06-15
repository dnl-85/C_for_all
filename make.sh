#!/bin/bash

# création du dossier principal et des sous-dossiers du projet
# creating the project's main folder and sub-folders
mkdir $1
mkdir $1/exe
mkdir $1/src
mkdir $1/inc
mkdir $1/pack
mkdir $1/doc

# création du fichier .h incluant les en-têtes pour le programme C
# ce fichier sera placé dans le dossier embedded/
# creating the .h file including headers for the C program
# this file will be in the embedded/ folder
echo """#include <assert.h>
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
""" >> $1/inc/$1.h
echo '... include header file in : '$1'/inc/'$1'.h ...'
echo '    ... DONE ! ...'

# création du fichier .c contenant une première fonction main()
# ce fichier sera à la racine du projet
# creating le .c file including a first main() function
# this file will be at the root of the project
echo '#include "../inc/'$1'.h" ' >> $1/src/$1.c
echo """
int main(void) {
    printf(\"Hello, World ! \n\");
    return 0;
}
""" >> $1/src/$1.c
echo '... include program file in : '$1'/src/'$1'.c ...'
echo '    ... DONE ! ...'

# création d'une license MIT contenant le login de l'utilisateur et la date de lancement du projet
# ce fichier sera dans le dossier license/
# creating a MIT license including user's login and the starting date of the project
# this file will be in the license/ folder
echo "Copyright - " $1 >> $1/doc/LICENSE
echo "by : "$USER >> $1/doc/LICENSE
date >> $1/doc/LICENSE
echo """
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

""" >> $1/doc/LICENSE
echo '... include MIT license in : '$1'/license/LICENSE ...'
echo '    ... DONE ! ...'

# création d'un script permettant de compiler rapidement pour linux, win32 et win64, ainsi que de faire un zip
# de sauvegarde de la compilation à chaque compilation
# creating a script who's gonna make a fast compilation for linux, win32 and win64, and make a zip archive
# who's gonna backup the compilation at each compilation
echo "#!/bin/bash" >> $1/Makefile.sh
echo "rm pack/"$1".zip" >> $1/Makefile.sh
echo "gcc -Wall -o exe/"$1"_l64 src/"$1".c -lm" >> $1/Makefile.sh
echo "i686-w64-mingw32-gcc -o exe/"$1"_w32.exe src/"$1".c" >> $1/Makefile.sh
echo "x86_64-w64-mingw32-gcc -o exe/"$1"_w64.exe src/"$1".c" >> $1/Makefile.sh
echo "zip pack/"$1".zip -r exe/" >> $1/Makefile.sh
echo "zip pack/"$1".zip -r inc/" >> $1/Makefile.sh
echo "zip pack/"$1".zip -r src/" >> $1/Makefile.sh
echo "zip pack/"$1".zip -r doc/" >> $1/Makefile.sh
echo "zip pack/"$1".zip *.c" >> $1/Makefile.sh
echo "zip pack/"$1".zip *.md" >> $1/Makefile.sh
echo "zip pack/"$1".zip *.sh" >> $1/Makefile.sh
chmod +x $1/Makefile.sh
echo '... include make_file for easy compilation in : '$1'/Makefile.sh ...'
echo '    ... DONE ! ...'

# création d'un fichier texte markdown README.md pour le projet
# creating a markdown text file README.md for the project
echo "# README : " $1 >> $1/doc/README.md
echo "### description file for current C project" >> $1/doc/README.md
echo "-----" >> $1/doc/README.md
echo "  give in this file a precise description of your project and how it works !  " >> $1/doc/README.md
echo '... include README.md ...'
echo '    ... DONE ! ...'

# et voilà !
# that's all folks !
echo '... project is READY ! ...'

# maintenant nous pouvons commencer
# now we can work
cd $1
xfce4-terminal --command="nohup notepadqq --new-window src/$1.c --new-window inc/$1.h --new-window doc/README.md"
rm nohup.out
echo "... this terminal will clear screen in 5 seconds ..."
sleep 5
clear
