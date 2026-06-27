import numpy as np

ran = np.random.default_rng()
print(ran.integers(6))
print(ran.uniform(low=10,high=90,size = 1))

laptops = np.array(['HP','Lenovo','Dell','MaxAir','Toshiba'])
ran.shuffle(laptops)
print(laptops)