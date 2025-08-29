import sys
import math
k = len(sys.argv)
maxvalue = -math.inf
minvalue = math.inf
for i in range(1,k):
    if int(sys.argv[i]) > maxvalue:
        maxvalue = int(sys.argv[i])
    if int(sys.argv[i]) < minvalue:
        minvalue =  int(sys.argv[i])
print(maxvalue)
print(minvalue)
