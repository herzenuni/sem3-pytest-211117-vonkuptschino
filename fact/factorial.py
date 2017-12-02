def fact(n):
	res = None
	if type(n) is not int:
		raise TypeError
	try:
		n = int(n)
	except (ValueError, TypeError):
		print('arg {} is not an integer or negative'.format(n))
	else:
		if n < 0:
			raise ValueError
		elif n == 0:
			return 1
		else:
			res = n * fact(n - 1)
		return res
