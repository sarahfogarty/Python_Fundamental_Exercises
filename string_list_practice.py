
#print the position of the first instance of "day". Then create a new string where the word "day" is replaced with the word "month".
str1 = "It's thanksgiving day. It's my birthday,too!"
str2 = "day"
print str1.find(str2)

print str1.replace("day", "month")

#print the min and max values in a list - it should work for any list
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#print the first and last values - then create a new list only containing the first and last values
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]

print x[0]
print x[len(x)-1]



#sort list - split list in half - Push the list created from the first half to position 0 of the list created from the second half. The output should be:[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
list1 = x[0:len(x)/2]
list2 = x[len(x)/2:len(x)]
print "list 1", list1
print "list 2", list2
list2.insert(0,list1)
print list2
