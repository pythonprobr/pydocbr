#!/bin/bash
PYTHON_SRC=../../cpython
cp $PYTHON_SRC/.???* . # .hgignore, .gitignore etc.
cp $PYTHON_SRC/LICENSE .
cp $PYTHON_SRC/Grammar/Grammar Grammar/
cp $PYTHON_SRC/Lib/test/exception_hierarchy.txt Lib/test/
cp $PYTHON_SRC/Parser/Python.asdl Parser/
cp $PYTHON_SRC/Include/patchlevel.h Include/
# do not uncomment this unless you know all translations will be overwritten,
# and that is what you really want to do
# cp -Rv $PYTHON_SRC/Doc/ Doc/