from nsetools import Nse
from pprint import pprint
nse = Nse()
q = nse.get_quote('infy')
pprint(q)