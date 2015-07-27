## pwg: password generator

pwg: password generator
evolution of the binary bit cipher shift project
pwg is a unique and compliant password generator based on a website's sitename

v1 alpha - July 2015
Tested on Python 3.4.3 and Python 2.7.10

Passwords are generated as follows:

*`<first letter of sitename><length of sitename><!><password>`*

While the first three characters of the password can be easily guessed, 
I believe it helps to have some idea of what the password is in reference to, 
and the password itself is as secure as the size of the default alphabet, 
block size, and the length you specify

Please make sure to create your own `DEFAULT_ALPHABET` variable as follows:

```
import string, random`
alpha = list(string.letters + string.digits)
random.shuffle(alpha)
DEFAULT_ALPHABET = ''.join(alpha)
```

Usage:
```
pwg = Pwg()
pwg.genpass(sitename)
pwg.chkpass(password, sitename)
```

######Released under the MIT License
######(c) 2015 Kamil Mansuri
######Originally based on my Missee binary cipher project, along with an algorithm developed by fogleman
