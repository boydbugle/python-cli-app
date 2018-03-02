import cgitb; cgitb.enable()
import sys, os, cgi, pickle
from cookie import SimpleCookie


class form(dict):
    def __init__(self, fields):
        dict.__init__(self,fields):
        for k, v in self.items(): self[k] = v.value

form = form(cgi.FieldStorage())

if __name__=='__main__':
    main()
