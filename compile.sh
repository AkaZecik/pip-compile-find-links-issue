#!/bin/sh

cd subproject
echo "============================== COMPILING SUBPROJECT =============================="
echo
pip-compile -U -v requirements.in

echo
echo "============================== GENERATER requirements.txt  ======================="
echo
cat requirements.txt
echo

cd ..
echo "============================== COMPILING MAIN PROJECT ============================"
echo
pip-compile -U -v requirements.in
