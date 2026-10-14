"""import numpy as np

a = np.array([10, 20, 30, 40])
print(a)
print(type(a))

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)

print(np.zeros(4))
print(np.ones((2, 3)))
print(np.full((2,2), 7))

print(np.eye(3))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))



b = np.array(b.shape)
print(b.ndim)
print(b.size)
print(b.dtype)


print(np.array([1, 2.5, 3]).dtype)

x = np.array([1, 2, 3])
print(x.astype(float))



"""

import numpy as np
import time

data = list(range(1_000_000))

arr = np.arange(1_000_000)

t = time.time()
sum(data)
print("list :", time.time() - t)

t = time.time()
arr.sum()
print("numpy:", time.time() - t)


x = np.array([10,20,30,40,50,60])

print(x[0])
print(x[-1])
print(x[1:4])
print(x[::4])


m = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(m[1,2])
print(m[0])
print(m[:, 1])
print(m[0:2, 1:])


n = np.array([5, 12, 8, 20, 3])

print(n > 7)
print(n[n > 7])
print(n[(n > 4) & (n < 15)])


n = np.array([5, 12, 8, 20, 3])
n[n > 10] = 0
print(n)

n = np.array([5, 12, 8, 20, 3])
safe = n.copy()
safe[0] = 99
print(n[0])



marks = np.array([45, 78, 33, 90])
result = np.where(marks >= 40, "Pass", "Fail")

print(result)

p = np.array([1,2,3])
q = np.array([10,20,30])

print(p + q)
print(p * q)
print(q / p)
print(p ** 2)
print(p * 10)




print(np.sqrt(np.array([4,5,6,2,3])))
print(np.round(np.array([1.254, 5.1265])))

print(np.abs(np.array([-3, 4])))
print(np.cumsum(np.array([1, 2, 3, 4])))

