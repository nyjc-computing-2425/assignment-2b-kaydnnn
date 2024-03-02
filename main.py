num = input('Enter a number (decimal only): ')
tmp = num.strip(" ")
tmp = tmp.split(".")[1]
dp = len(tmp)

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
