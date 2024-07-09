# !multiprocessing Code
import multiprocessing
import multiprocessing.process
import time

square_list = []
def Add_Sqaure(num):
    global square_list
    for i in range(num):
        time.sleep(0.2)
        print("sqaures : ", i*i)
        square_list.append(i*i)
    print(square_list)

p1 = multiprocessing.Process(target=Add_Sqaure, args=(15,))

p1.start()
p1.join()

print("Done")
print(square_list) #this is blank , The issue arises because each process in the multiprocessing module has its own memory space. When you modify the square_list in the child process, those changes are not reflected in the parent process. 

#! for achive this sharing we have to use the Shared memory between them
print("---------------------------Sharing Memory----------------------")

def Add_square(num,q):
    for i in range(num):
        print("Sqaure :",i*i)
        q.put(i*i)


q = multiprocessing.Queue()
t1 = multiprocessing.Process(target = Add_square, args = (15,q))

t1.start()
t1.join()
print("After Processing :",end="")

while not (q.empty()):
    print(q.get(), end= "  ")


# multiproccessing with lock 