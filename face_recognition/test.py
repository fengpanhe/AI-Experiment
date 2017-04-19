import matplotlib.pyplot as plt
import numpy as np
import math


aa = np.array([1,2,3,4])
bb = np.array([1,2,3])
# cc = np.sum(aa * bb)
dd = np.dot(aa[1:],bb)
dd = np.random.random(10)/10 - 0.05
print(dd)

a = np.zeros([2,3])
print(a)
a[1] = np.array([1,2,3])
print(a)
# ['008000','98FB98','90EE90','9ACD32','ADFF2F','7FFF00','7CFC00','00FF00','32CD32','00FA9A','00FF7F','66CDAA','7FFFD4','20B2AA','3CB371','2E8B57','8FBC8F','228B22','006400','6B8E23','808000','556B2F','008080']

# ['#FFFF00','#FFD700','#FFBF00','#FFA500','#FF4D00','#FF2400','#FF00FF','#FF0000','#F0F8FF','#E32636','#E0FFFF','#CCFF00','#CCCCFF','#8B00FF','#7FFFD4','#66FF00','#6495ED','#5E86C1','#4169E1','#30D5C8','#2A52BE','#1E90FF','#082567','#00FFFF','#00FF00','#007FFF','#0047AB','#003399','#003366','#003153','#002FA7','#0000FF','#000080']