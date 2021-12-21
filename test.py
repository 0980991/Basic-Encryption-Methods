from ciphers import Ciphers
from PlayFair import PlayFair


pf = PlayFair()
pf.fillGrid('PLAYFAIR')
# Horizontal tests
# pf.decrypt([1, 5])
# pf.decrypt([6, 10])
# pf.decrypt([11, 15])
# pf.decrypt([16, 20])
# pf.decrypt([21, 25])
pf.decrypt([5, 25])
pf.decrypt([25, 5])

# Vertical tests
# pf.decrypt([1, 21])
# pf.decrypt([2, 22])
# pf.decrypt([3, 23])
# pf.decrypt([4, 24])
# pf.decrypt([5, 25])

# Box tests
# pf.decrypt([1, 7])
# pf.decrypt([1, 13])
# pf.decrypt([1, 19])
# pf.decrypt([1, 25])
# pf.decrypt([5, 9])
# pf.decrypt([5, 13])
# pf.decrypt([5, 17])
# pf.decrypt([5, 21])

# pf.decrypt([25, 19])
# pf.decrypt([25, 13])
# pf.decrypt([25, 7])
# pf.decrypt([25, 1])
# pf.decrypt([21, 17])
# pf.decrypt([21, 13])
# pf.decrypt([21, 9])
# pf.decrypt([21, 9])
# pf.decrypt([17, 9])



# cipher = Ciphers()
# cipher.decryptPlayfair()