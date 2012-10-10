#!/usr/bin/env python

# -------------------------------
# projects/netflix/TestNetflix.py
# Copyright (C) 2012
# -------------------------------

"""
To test the program:
    % python TestNetflix.py >& TestNetflix.py.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py >& TestNetflix.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import math
import sys
sys.path.append('./caches')
from avgUsers import avg_user
from avgMovies import avg_movies
from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1:\n2\n3\n4\n5:\n6\n7\n8\n")
        a = [0, []]
        c = [0]
        b = netflix_read(r, a, c)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1][0]== 2)
        self.assert_(a[1][1]== 3)
        self.assert_(a[1][2]== 4)
        a = [0,[]]


        if b :
            b = netflix_read(r, a, c)
            self.assert_(b    == False)
            self.assert_(a[0] ==  5)
            self.assert_(a[1][0]== 6)
            self.assert_(a[1][1]== 7)
            self.assert_(a[1][2]== 8)

    def test_read_2 (self) :
        r = StringIO.StringIO("1:\n5:\n6\n7\n8\n")
        a = [0, []]
        c = [0]
        b = netflix_read(r, a, c)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == [])
        if b :
            b = netflix_read(r, a, c)
            self.assert_(b    == False)
            self.assert_(a[0] ==  5)
            self.assert_(a[1][0]== 6)
            self.assert_(a[1][1]== 7)
            self.assert_(a[1][2]== 8)

    def test_read_3 (self) :
        r = StringIO.StringIO("3:\n1\n2\n4:\n")
        a = [0, []]
        c = [0]
        b = netflix_read(r, a, c)
        self.assert_(b    == True)
        self.assert_(a[0] ==  3)
        self.assert_(a[1][0]== 1)
        self.assert_(a[1][1]== 2)
        if b :
            b = netflix_read(r, a, c)
            self.assert_(b    == False)
            self.assert_(a[0] ==  4)

    # ----
    # solve
    # ----
 
    def test_solve_1 (self) :
        r = StringIO.StringIO("10:\n1531863\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "10:\n3.05131797961\n")  

    def test_solve_2 (self) :
        r = StringIO.StringIO("10000:\n523108\n10001:\n2609496\n1474804\n831991\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "10000:\n3.73064674114\n10001:\n4.13497769562\n3.69980243158\n2.87965854669\n")  

    def test_solve_3 (self) :
        r = StringIO.StringIO("1001:\n67976\n1025642\n624334\n239718\n143504\n")
        w = StringIO.StringIO()
        netflix_solve(r, w) 
        self.assert_(w.getvalue() == "1001:\n3.53533976535\n3.25160826479\n3.35917250612\n3.93993859118\n3.75000352624\n")  
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        netflix_print(w, 1 , [1.0,2.0,3.0])
        self.assert_(w.getvalue() == "1:\n1.0\n2.0\n3.0\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        netflix_print(w, 3, [])
        self.assert_(w.getvalue() == "3:\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        netflix_print(w, 5, [3.4,4.3,5.0,1.0])
        self.assert_(w.getvalue() == "5:\n3.4\n4.3\n5.0\n1.0\n")    
    
    # ----
    # eval
    # ----

    def test_eval_1 (self) :

        movie_id = 1
        user_id = 30878
        #user_avg = avg_user [user_id -1]         
        #movie_avg = avg_movies[movie_id-1]   
        everyone = 1.0
        v = netflix_eval(movie_id, user_id, everyone)
        self.assert_(v >= 1.0 and v <= 5.0)
        self.assert_(str(v) == "4.34787519597")

    def test_eval_2 (self) :

        movie_id = 10
        user_id = 1952305
        user_avg = avg_user [user_id -1] 
        movie_avg = avg_movies[movie_id-1]
        everyone = 2.4
        v = netflix_eval(movie_id, user_id, everyone)
        self.assert_(v >= 1.0 and v <= 5.0)
        self.assert_(str(v) == "3.54036144578")

    def test_eval_3 (self) :

        movie_id = 1000
        user_id = 2326571
        user_avg = avg_user [user_id -1] 
        movie_avg = avg_movies[movie_id-1]
        everyone = 3.0
        v = netflix_eval(movie_id, user_id, everyone)
        self.assert_(v >= 1.0 and v <= 5.0)
        self.assert_(str(v) == "3.57758913413")
# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
