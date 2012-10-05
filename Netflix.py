#!/usr/bin/env python

# ---------------------------
# projects/netflix/Collatz.py
# Copyright (C) 2012
# ---------------------------


# ------------
# netflix_read
# ------------

def netflix_read (r, a, have_buffer) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    movie = 0

    if have_buffer == [0] :    

        s = r.readline()
        if s == "" :
            return False
    
    
        if s[-2] == ":": # checks if the last element == ":"
            movie  = int(s.split(":")[0]) #try to print
    else:

        movie  = int(have_buffer[0]) #try to print
           
    assert type(movie) is int

    a [0] = movie
    users_a = a[1]



    while True :
        s = r.readline()
        if s == "" :
            return False   
        if s [-2] == ":":
            have_buffer[0] = s.split(":")[0]
            return True
        users_a.append(int(s[0]))

    
# ------------
# netflix_eval
# ------------

def netflix_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """

# -------------
# netflix_print
# -------------

def netflix_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")
"""
# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """


    
    next_movie = [0]
    while True : #return False when we reach eof
        a = [0, []]
        end_reached = netflix_read(r, a, next_movie)
#        v = netflix_eval(a[0], a[1])

#       netflix_print(w, a[0], a[1], v)
        if end_reached :
          break
    
