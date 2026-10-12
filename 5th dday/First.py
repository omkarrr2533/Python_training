import numpy as np

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