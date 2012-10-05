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
#optional testing!

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
        r = StringIO.StringIO("1:\n2\n3\n4\n5:\n6\n7\n8\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)


    def test_solve_2 (self) :
        r = StringIO.StringIO("1:\n5:\n6\n7\n8\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)


    def test_solve_3 (self) :
        r = StringIO.StringIO("3:\n1\n2\n4:\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)       
     
    """
    def test_read_3 (self) :
        r = StringIO.StringIO("10 10\n")
        a = [0, 0]
        b = netflix_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 10)

    def test_read_4 (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = netflix_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 1)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = netflix_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = netflix_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = netflix_eval(1, 999999)
        self.assert_(v == 525)

    def test_eval_5 (self) :
        v = netflix_eval(1, 3)
        self.assert_(v == 8)
    def test_eval_6 (self) :
        v = netflix_eval(3, 2)
        self.assert_(v == 8)
    def test_eval_7 (self) :
        v = netflix_eval(3, 3)
        self.assert_(v == 8)
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        netflix_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        netflix_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        netflix_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        netflix_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("100 200\n900 1000\n201 210\n1 10\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "100 200 125\n900 1000 174\n201 210 89\n1 10 20\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("900000 999999\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "900000 999999 507\n")
    def test_solve_4 (self) :
        r = StringIO.StringIO("139163 552953\n776468 628994\n378628 766439\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "139163 552953 470\n776468 628994 504\n378628 766439 509\n")

    def test_solve_5 (self) :
        r = StringIO.StringIO("9043 9820\n3546 2708\n2234 2573\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "9043 9820 260\n3546 2708 217\n2234 2573 209\n")
"""
# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
