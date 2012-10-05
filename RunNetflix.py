#!/usr/bin/env python

# ------------------------------
# projects/Netflix/RunNetflix.py
# Copyright (C) 2012
# Raul U Cardenas
# Raul B Barbosa
# -------------------------------

"""
To run the program
    % python RunNetflix.py < RunNetflix.in > RunNetflix.out
    % chmod ugo+x RunNetflix.py
    % RunNetflix.py < RunNetflix.in > RunNetflix.out

To document the program
    % pydoc -w Netflix
"""

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----

netflix_solve(sys.stdin, sys.stdout)
