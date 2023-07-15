# from Allison Weins, Senior Product Manager at GitHub demo

import re

e_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-.]+$'
p_regex = r'^\+?1?\d{9,15}$'
s_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$'

def checkvalid(text, regex):
    if re.search(regex, text):
        return True
    else:
        return False
    
# Add a main method to test all the regular expressions
if __name__ == '__main__':
    print(("valid","invalid")[checkvalid('test@microsoft.com', e_regex)])
    print(("valid","invalid")[checkvalid('(425)555-2368', p_regex)])
    print(("valid","invalid")[checkvalid('test1234@', s_regex)])