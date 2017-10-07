#Odd/Even
def odd_even():
    for n in range(1, 2001):
        if n % 2 != 0:
            print "Number is ", n,". This is an odd number."
        else:
            print "Number is ", n,". This is an even number."
odd_even()

#Multiply
def multiply():
    li = [2,4,10,16]
    for i in range(0, len(li)):
        li[i] = li[i]*5
    print li
multiply()

#Hacker Challenge
