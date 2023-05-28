from model.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n=5
f="data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f=a

def random_string(prefix,maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phones(minlen,maxlen):
    symbols = string.digits+"()+-"
    return "".join([random.choice(symbols) for i in range(random.randrange(minlen,maxlen))])

testdata = [
    Contact(firstname=random_string("fname", 10), lastname=random_string("lname", 10), middlename=random_string("mname", 10),mobile=random_phones(10, 14))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))