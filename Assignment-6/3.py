import numpy
arr = numpy.array([input().split() for _ in range (int(input().split()[0]))],int)
print (arr.transpose())
print (arr.flatten())