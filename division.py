num=int(raw_input("enter a number"))
div=int(raw_input("enter a number to check for division"))
if num%div==0:
    print " the number is divisible by %s"%(div)
elif num%2==0:
    print "the number is even"
else:
    print "the number is odd"