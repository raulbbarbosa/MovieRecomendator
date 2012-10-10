#!/usr/bin/env python

# ---------------------------
# projects/netflix/Collatz.py
# Copyright (C) 2012
# ---------------------------

import math
import sys
sys.path.append('./caches')
#from Average import average_cache
from avgUsers import avg_user
from avgMovies import avg_movies


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
    a[1] = []
    users_a = a[1]



    while True :
        s = r.readline()
        if s == "" :
            return False   
        if s [-2] == ":":
            have_buffer[0] = s.split(":")[0]
            return True
        users_a.append(int(s))

    
# ------------
# netflix_eval
# ------------

def netflix_eval (movie, user,everyone) :
    """
    
    return the max cycle length in the range [i, j]
    """

    #the result of some calculation.
    #a lot of calculatios    
    #avg = (avg_user[user-1] + everyone )/2  
    diff = (avg_user[user-1] - everyone)/4
    return max(1.0,min(5.0, (avg_user[user-1] + avg_movies[movie-1])/2 + diff))
            
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

    #print "RMSE"
    users_that_have_avg_rating_diff_from_zero = [i for i in avg_user if i!=0.0]    
    everyone = sum(users_that_have_avg_rating_diff_from_zero ,0.0)/len(users_that_have_avg_rating_diff_from_zero)
    next_movie = [0]
    while True : #return False when we reach eof
        a = [0, []]
        end_reached = netflix_read(r, a, next_movie)
        movie = a[0]
        users_list = a[1]        
        ratings = [0.0]*len(users_list)       
        c = 0
        for user in users_list :
            ratings[c] += netflix_eval(movie,user,everyone)
            c+=1
        netflix_print(w, movie, ratings)
        
        if not end_reached :
            break
    #netflix_rmse(actual, predictions)
    #print
