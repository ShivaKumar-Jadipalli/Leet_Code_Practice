https://youtu.be/wGSQ486Y4sc?si=tdm7zehCpS00ebAi

This is the video where I learned from 

heapq by default uses min heap to use max heap you should either change the list symbols to negative or use 

heapq._heapify_max(list)


so I found that turning a list into heap is of time complexity O(n) and inserting an element is of O(logn) in the problem 2462 I am finding the minimum value each time which is too much time complexity I just want to find once , So I still don't understand how heaps helps me to solve this problem let's see anyway first I will learn about heaps then I will see the best solution to see how heaps are used 


Time complexity 

                      lists           Heaps 
insertion_middle      O(n)             O(logn)
Deletion_middle       O(n)             O(logn)
Accesing_middle       O(1)             O(n)

Note : Accesing min and max in heap is just O(1) , since heap always maintains Ascending Binary order 

it is just that heaps is a type of list where minimum sorted order is always maintained so when you add an element into this since the previous heap is already sorted this new element will get inserted in the sorted order with just O(logn) 

Basics in heap : 
heapq.heapify(data) - no need to assign it to another variable it modifies the data inplace itself 
heapq.heappush(data,4)
heapq.heappop(data) - remove last element 
heapreplace() 
heappushpop() 
heapq.merge(data_1 , data_2 ) it won't take all at once instead it will go through one by one 
heapq.nsmallest(3,data) - returns the smallest 3 in data 
heapq.nlargest(3,data) 