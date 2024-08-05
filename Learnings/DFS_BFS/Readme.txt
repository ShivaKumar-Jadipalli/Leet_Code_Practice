https://youtu.be/xlVX7dXLS64?si=suL3y-K-UgYmit8J

See the explanation of BFS in the same video 

Deepth First search : 

I don't see anything in particular but this means that we can visit every element in the tree like imagine visiting one element in each level instead of visiting every element in each level of a tree , There is no rule of which element to select in the children you can select any thing if condition is mentioned it will either be smaller/greater one 

sudo code : 

G = Given tree 

marked = [False] * G.size()
def (G,v):
    visit(v)
    marked[v] = True
    for w in G.neighbours(v):
        if not marked[w]
            dfs(G,w)

There are also some other kind of implementations but I am not writing them here cause they are hard to understand 

Pre-order and Post-Order and Topological sort 

Pre-Order : The element which is visited 
Post-Order : The element which is completely visited like if you have visited all childrean of it then it can be marked 
Topological Sort : Reversed version of Post-Order 


The given code is already from Pre-order to make it as post-order all you have to do is place " visit(v) " at the end of the code 

In the video He also created a code to create a maze 


