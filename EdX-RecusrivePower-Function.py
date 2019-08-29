def RecursivePower(base, exp):
	if exp <= 0:
		return 1

	else:
		return base * RecursivePower(base, exp-1)

print(RecursivePower(8,4))
