def isPrime(n):
	if n==1:
		return False
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			return False
	return True

n="*3"

# have to replace 3/6/9 digits, else 3 possibles will be multiples of 3 => max 7
# have to replace even number
# hence must replace 6 digits (or 12)

#cannot replace final digit, else even
#also final digit must be non5 odd obvs
#remaining digits cannot add to mult of 3

#only need to check replacing 0/1/2s


#instead: check 1,2,3digits numbers, insert into ****** + 1/3/7/9
# check not mult of 3
# include 0xx


starLength = 2
a = "3*77*****3"
print(a.index("*",3))
print(int(a.replace('*','0')))


def fInt(n,digits=2):
	return "{:0>{}d}".format(n,digits)


def checkPermutations(x, digits):
	for perm in (fInt(x) for x in range(10**digits) if not sum([int(fInt(x)[i]) > int(fInt(x)[i+1]) for i in range(digits-1)])):
		rep = '**'
		for (i, digit) in enumerate(fInt(x)):
			rep = rep[:i+int(perm[i])] + digit + rep[i+int(perm[i]):]
		print(rep)
		print(perm)
	return 0



def checkValue(n):
	missedCount = 0
	for i in range(10):
		if not isPrime(4):
			pass


def f(digits=1):
	for i in range(10**digits):
		if i%3 != 0:
			check = checkPermutations(i, digits)
			if check:
				return check
		if i>1020:
			return
	return f(digits+1)

f()
