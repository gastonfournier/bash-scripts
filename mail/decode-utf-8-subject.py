#!/usr/bin/python
from email.header import decode_header
import sys 

if (len(sys.argv) > 1):
    subject = sys.argv[1]
    print decode_header(subject)[0][0]
else:
    print "USE: python "+sys.argv[0]+" \"=?UTF-8?Q?TEST:_T=C3=A9st_c=C3=B3n_=C3=A1c=C3=A9nt=C3=B3s?=\""
