import array;

# init an array of ints with 0 of size 9
# array is a class

a = array.array('i');

# fill the array with element and index
a.insert(1, 0);
a.insert(2, 1);
a.insert(3, 1);

# append the the element to the end of the array
a.append(3);

# display the array's elements
for element in a:
	print(element);

print("Address and Length: ", a.buffer_info());



print("how many times the number 1 appear in the array?")
print(a.count(1));

b = [8, 9, 19];
# this is a list, but since it's of the same type code (int)
# extend(iterable) takes in either an array or an iterable of the same nature

a.extend(b);
print(a);
a.reverse();
print(a);


print("Transforming the array into a list: ")
a_list = a.tolist();
print(a_list);
