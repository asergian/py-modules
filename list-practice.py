####################################################
### 1. Practice List creation, append, pop
####################################################

print("\n1. Practice list creation, append, pop\n")

# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 
print("1.1. List containing multiple values:", List)

# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List2 = [['Geeks', 'For'], ['Geeks']] 
print("1.2. Multi-Dimensional List:", List2) 

# accessing a element from the  
# list using index number 
print("1.3. Accessing element from the list. #0:", List[0], ", #1:", List[2]) 

# accessing a element using 
# negative indexing 
print("1.4. Accessing element using negative indexing")

# print the last element of list 
print("1.4.1. Last element of the list:", List[-1])
    
# print the third last element of list  
print("1.4.2. Third to last element of the list:", List[-3]) 

# list with multiple data types
List3 = [1, 2,  3, "GFG", 2.3]
print("1.5. List with multiple data types:", List3)

# add element to end of list using List.append(value)
List3.append(5)
List3.append("ok")
print("1.6. Append elements 5 and 'ok' to list:", List3)

# remove element from end of list using List.pop()
x = List3.pop() # remove the last element and store it in x
List3.append("ok") # put the last element back
print("1.7. Pop then reappend value to list. Value:", x, ", List:", List3)
#print(List3[7]) # raises IndexError


####################################################
### 2. Practice list splicing, indexing, removing
####################################################
print("\n2. Practice list splicing, indexing, removal\n")
li = [1, 2, 3, 4]
print("2.0. li =", li)

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
print('2.1. li[1:3] =', li[1:3])   # Return list from index 1 to 3 => [2, 4]
print('2.2. li[2:] =', li[2:])    # Return list starting from index 2 => [4, 3]
print('2.3. li[:3] =', li[:3])    # Return list from beginning until index 3  => [1, 2, 4]
print('2.4. li[::2] =', li[::2])   # Return list selecting elements with a step size of 2 => [1, 4]
print('2.5. li[::-1] =', li[::-1])  # Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]
print("2.6. Remove index 2 using 'del li[2]'", li)

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
print("2.7. Removed first occurance of '2' using li.remove(2):'", li)
#li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again
print("2.8. Reinsert 2 and index 1 using 'li.insert(1, 2)'", li)

# Get the index of the first item found matching the argument
print("2.9. Get index of first '2' using li.index(2)", li.index(2)) # => 1
#li.index(4)  # Raises a ValueError as 4 is not in the list

# You can add lists
# Note: values for li and for other_li are not modified.
other_li = [4, 5, 6]
li + other_li  # => [1, 2, 3, 4, 5, 6]
print("2.10. List addition. other_li =", other_li)
print("2.10.1 li + other_li =", li + other_li)

# Concatenate lists with "extend()"
# Note: values for li are modified
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]
print("2.10.2 li.extend(other_li) =", li)

# Check for existence in a list with "in"
print("2.11. Check for existence in a list with 'in'", 1 in li)  # => True

# Examine the length with "len()"
print("2.12. len(li)", len(li))  # => 6