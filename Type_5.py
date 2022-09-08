# 5. Реализуйте алгоритм перемешивания списка.
n = list(input('введите список: '))
print(n)
l=int(len(n))

for i in range(l):
    j =int(n.random.randint(0, l-1))
    element=n.pop(j)
    n.append(element)
print(n)
 # Assign array
# arr = [1, 2, 3, 4, 5, 6]
 
# # Display original array
# print("Original List: ", arr)
 
# # Get length of List
# n = len(arr)
 
# #repeat the following for n number of times
# for i in range(n):
#     #select an index randomly
#     j = random.randint(0, n-1)
#     #delete the element at that index.
#     element=arr.pop(j)
#     #now append that deleted element to the list
#     arr.append(element)
# print("Shuffled List: ",arr)   
