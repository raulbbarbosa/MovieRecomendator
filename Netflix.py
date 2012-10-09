#!/usr/bin/env python

# ---------------------------
# projects/netflix/Collatz.py
# Copyright (C) 2012
# ---------------------------

import math
import sys
sys.path.append('./caches')
from Average import average_cache

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

def netflix_eval (movie, user) :
    """
    
    return the max cycle length in the range [i, j]
    """

    #the result of some calculation.
    #a lot of calculatios    


    return average_cache


# -------------
# netflix_rmse
# -------------
def netflix_rmse(actual, predictions) :
    """
    NOTE: actual needs to be build beforehand

    """
    mean = 0.0    

    for i in range( len(predictions)) :
    
        mean += (actual[i] - predictions[i])**2
            
    mean /= len(predictions)

    return math.sqrt(mean)    

# -------------
# netflix_print
# -------------

def netflix_print (w, movie, ratings) :
    """
    prints the values of i, j, and v
    w is a writer
    movie is a integer that represents a movie id    
    ratings is a list of ratings
    """

    w.write(str(movie) + ":\n") 
    for rating in ratings :
        w.write(str(rating)+"\n")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """

    print "RMSE"
    
    next_movie = [0]
    while True : #return False when we reach eof
        a = [0, []]
        end_reached = netflix_read(r, a, next_movie)
        movie = a[0]
        users_list = a[1]        
        ratings = [0.0]*len(users_list)       
        c = 0
        for user in users_list :
            ratings[c] += netflix_eval(movie,user)
            c+=1
        netflix_print(w, movie, ratings)
        
        if not end_reached :
            break
    #netflix_rmse(actual, predictions)
    #print
