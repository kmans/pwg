'''
pwg: password generator
evolution of the binary bit cipher shift project
pwg is a unique and compliant password generator based on a website's sitename

v1 alpha - July 2015
Tested on Python 3.4.3 and Python 2.7.10

Passwords are generated as follows:
<first letter of sitename><length of sitename><! character><password>

While the first three letters of the password are insecure, 
it helps to have some idea of what the password is in reference to, 
and the password itself is as secure as the size of the default alphabet, 
block size, and the length you specify

Please make sure to create your own DEFAULT_ALPHABET variable as follows:
import string, random
alpha = list(string.letters + string.digits)
random.shuffle(alpha)
DEFAULT_ALPHABET = ''.join(alpha)


Usage:
pwg = Pwg()
pwg.genpass(sitename)
pwg.chkpass(password, sitename)


Released under the MIT License
(c) 2015 Kamil Mansuri
Based on a unique generation algorithm developed by fogleman

'''

#Create your own default alphabet in Python
#import string, random
#alpha = list(string.letters + string.digits)
#random.shuffle(alpha)
#DEFAULT_ALPHABET = ''.join(alpha)

#change this immediately.
DEFAULT_ALPHABET = 'bM0SQ3x1puOaNdKP5BItmfDWyhZXYkqleGzC74EiU8AgjLJ62T9FovcHRwsnVr'

DEFAULT_BLOCK_SIZE = 45
MIN_LENGTH = 7

class Pwg(object):

    def __init__(self, alphabet=DEFAULT_ALPHABET, block_size=DEFAULT_BLOCK_SIZE):
        self.alphabet = alphabet
        self.block_size = block_size
        self.mask = (1 << block_size) - 1
        #we implement this to ensure python 3 compatibility
        self.mapping = list(range(block_size).__reversed__())

    #creates your password for the website
    def genpass(self, sitename):
        sitename = sitename.lower()

        return sitename[0].upper()+str(len(sitename))+'!'+self.encode_num(sum(map(ord, sitename)))

    #returns True if the password belongs to the webiste
    #the first char in password should match first letter of website, followed by length of the sitename, followed by a !
    def chkpass(self, password, sitename):
        sitename = sitename.lower()

        if password[0].lower() == sitename[0] and int(password[1]) == len(sitename) and password[2] == "!":
            return self.decode_num(password[3:]) == sum(map(ord, sitename))
        else:
            return self.decode_num(password) == sum(map(ord, sitename))

    def encode_num(self, n, min_length=MIN_LENGTH):
        return self.enbase(self.encode(n), min_length)

    def decode_num(self, n):
        return self.decode(self.debase(n))

    def encode(self, n):
        return (n & ~self.mask) | self._encode(n & self.mask)

    def _encode(self, n):
        result = 0
        for i, b in enumerate(self.mapping):
            if n & (1 << i):
                result |= (1 << b)
        return result

    def decode(self, n):
        return (n & ~self.mask) | self._decode(n & self.mask)

    def _decode(self, n):
        result = 0
        for i, b in enumerate(self.mapping):
            if n & (1 << b):
                result |= (1 << i)
        return result

    def enbase(self, x, min_length=MIN_LENGTH):
        result = self._enbase(x)
        padding = self.alphabet[0] * (min_length - len(result))
        return '%s%s' % (padding, result)

    def _enbase(self, x):
        n = len(self.alphabet)
        if x < n:
            return self.alphabet[x]
        return self._enbase(x // n) + self.alphabet[x % n]

    def debase(self, x):
        n = len(self.alphabet)
        result = 0
        for i, c in enumerate(reversed(x)):
            result += self.alphabet.index(c) * (n ** i)
        return result


