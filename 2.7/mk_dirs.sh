#!/bin/bash
mkdir Doc
# these are needed because files in them are included in docs
# see cp_py_src.sh for details
mkdir Grammar
mkdir Lib
mkdir Lib/test
mkdir Parser
# Include/patchlevel.h is used by the Makefile to determine Python version
mkdir Include
