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
    return true if that succeeds and it has more lines to read, false otherwise
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

def netflix_eval (movie, user,users_avg) :
    """
    computes a prediction given a movie and a specific user
    movie is a movie id
    user is a user id
    users_avg is the average of all users average that are different from 0.0
    return a prediction between 1 and 5
    """
    assert movie >= 1 and movie <= 17770
    assert user >= 1 and user <= 2649429
    assert users_avg >=1.0 and users_avg <= 5.0
    diff = (avg_user[user-1] - users_avg)/4
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

    assert movie >= 1 and movie <= 17770     

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

    users_that_have_avg_rating_diff_from_zero = [i for i in avg_user if i!=0.0]    
    avg_of_everyone_diff_than_zero = sum(users_that_have_avg_rating_diff_from_zero ,0.0)/len(users_that_have_avg_rating_diff_from_zero)
    next_movie = [0]
    while True : #return False when we reach eof
        a = [0, []]
        end_reached = netflix_read(r, a, next_movie)
        movie = a[0]
        users_list = a[1]        
        ratings = [0.0]*len(users_list)       
        c = 0
        for user in users_list :
            ratings[c] += netflix_eval(movie,user,avg_of_everyone_diff_than_zero)
            c+=1
        netflix_print(w, movie, ratings)
        
        if not end_reached :
            break
    
