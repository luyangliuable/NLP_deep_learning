import numpy as np
import torch

print("random torch tensor ------------------------")
x = torch.rand(2, 2)
y = torch.rand(2, 2)
print(x)
print(y)


print("tensor addition ----------------------------")
z = x + y
print(str(y))


print("tensor addition in place -------------------")
y.add_(x)
print(y)

z = x * y
z = torch.mul(x, y)
y.mul_(x)


z = x - y
z = torch.sub(x, y)

z = x / y
z = torch.div(x, y)

x = torch.tensor([2.5, 0.1])
print(x)


print("tensor slicing -------------------")
x = torch.rand(5, 3)
print(x)
print(x[1, :])


print("Getting item from tensor ---------")
print(x[1, 1].item())

print("Reshaping a tensor ---------------")
x = torch.rand(4, 4)
print(x)
y = x.view(16)
print(y)


print("Tensor view ----------------------")
x = torch.rand(4, 4)
print(x)
y = x.view(16)
print(y)
z = x.view(-1, 8)
print(z)
print(z.size())
w = x.view(2, 8)
print(w)
print(w.size())


print("Numpy ----------------------------")
a = torch.ones(5)
print(a)
b = a.numpy()
print(type(b)) # can use use b.__class__


print("IMPORTANT: if Pytorch uses CPU instead of GPU, objects will share same memory address")
a = torch.ones(5)
b = a.numpy()
a.add_(1)
print(a) # This is:
print(b) # the same as this!

