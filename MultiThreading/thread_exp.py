# import time

# # Create an empty list
# my_list = []

# # Get the start time
# start_time = time.time()

# # Loop from 1 to 500 and append to the list
# for i in range(1, 1000):

#     my_list.append(i)
#     # print(my_list.append(i))

# # Get the end time
# end_time = time.time()

# # Calculate the time taken
# time_taken = end_time - start_time

# # Print the results
# print("Time taken:", time_taken, "seconds")

# print("----------------------------------------------------------")
# import threading
# # import time

# li = []
# thread_list = []

# def adding_element(start,End):
#     for i in range(start,End):
#         li.append(i)


# def Associate_the_task_to_threads(number_of_thread,total_data):
#     for i in range(number_of_thread):
#         start = i * total_data // number_of_thread
#         end = start + total_data//number_of_thread
#         thread = threading.Thread(target=adding_element,args=(start,end))
#         thread_list.append(thread)

# Associate_the_task_to_threads(51,1000)
# start_time = time.time()
# for i in thread_list :
#     i.start()

# print(threading.current_thread.__name__)

# for thread in thread_list:
#     thread.join()

# End_time = time.time()

# print("the actual time taken for proccesing is ",End_time - start_time)

# !--------------------------------------------------------------------------
#! finding square and cubes by multithreading and normal single thread
# normal code
import time

def finding_square(num):
    for i in range(num):
        print("Sqaure : ",i * i)
        time.sleep(0.2)

def finding_cubes(sum):
    for i in range(sum):
        print("Cubes : ",i*i*i)
        time.sleep(0.2)


start = time.time()
finding_square(15)
finding_cubes(15)
end = time.time()
print("Total Time taken for this taks is :", end - start)

# !acheiving by multithreading
import threading

t1 = threading.Thread(target=finding_square, args=(15,))
t2 = threading.Thread(target=finding_cubes, args=(15,))

start = time.time()
t1.start()
t2.start()


t1.join()
t2.join()

print("time taken by threading is :",time.time() - start)

