
def splitter(**kwargs):
	return kwargs

def func(a,b,c):
	return a**2+b**2-c**2

print(func(**(splitter(a=11, b=22, c=33))))

l1 = [1,2,3,4,5,6,8,5,3,6,8]
l1.pop()
