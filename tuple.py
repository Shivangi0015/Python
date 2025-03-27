#TUPLES
# immutable, written iniside ()

# Tuple OPERATIONS:
#1 tuple.index(element) - returns the index value where element occurred very first 
#2 tuple.count(element) - count the no. of times the element occurred

#PROGRAM 1:
#count the number of students with 'A' grade in the tuple = ["C","D","A","A","B","B","A"]

grade =('C','D','A','A','B','B','A')
print("Number of students with 'A' grade:",grade.count('A'))


# PROGRAM 2:
# store the above values in a list and sort them from 'A' to 'D'

grade_new =['C','D','A','A','B','B','A']
print("\nBefore sorting:",grade_new)
grade_new.sort()
print("\nSorted list:",grade_new)

