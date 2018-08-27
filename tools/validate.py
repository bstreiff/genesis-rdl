#!/usr/bin/env python3
#
# This is basically copied from the systemrdl-compiler examples.

from systemrdl import RDLCompiler, RDLListener, RDLWalker, RDLCompileError
from systemrdl.node import FieldNode
import os
import sys

# Collect input files from the command line arguments
input_files = sys.argv[1:]

for input_file in input_files:
    try:
        # Create an instance of the compiler
        rdlc = RDLCompiler()
        # Compile the file provided
        rdlc.compile_file(input_file)
        
        # Elaborate the design
        root = rdlc.elaborate()
    except RDLCompileError:
        # A compilation error occurred. Exit with error code
        sys.exit(1)
