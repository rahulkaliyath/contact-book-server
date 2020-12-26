import random 
import string 
  
def ran_gen(size=5, chars=string.ascii_lowercase[:10] + string.digits): 
    return ''.join(random.choice(chars) for x in range(size))