

import re

str  = '1억3,500'

amt = re.findall(r"\d+\.?\d*",str)
print(amt)