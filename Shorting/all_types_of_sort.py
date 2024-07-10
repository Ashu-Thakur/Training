import random
#! Bubble Short
def genratelist():
    main_list = []
    for i in range(100):
        main_list.append(random.choice(range(100)))
    return main_list


main_list = genratelist()
for i in range(len(main_list)):
    flg = False
    for j in range(len(main_list) - 1 - i):
        if main_list[j] > main_list[j + 1]:
            flg = True
            main_list[j], main_list[j + 1] = main_list[j + 1], main_list[j]
    if not flg:
        break
print("Shortted list -----------------------------")
print(main_list) 
print("--------------------------------------------------------------------------------------------------")
# selection short
li = genratelist()
print("unShortted list -----------------------------")
print(li)

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[j] < li[i]:
            li[i],li[j] = li[j],li[i]

print("Selection Shorted list -----------------------------")
print(li)

# !Insertion Short------
li = genratelist()
print("Unsorted list -----------------------------")
print(li)

for i in range(1, len(li)):
    key = li[i]
    j = i - 1
    while j >= 0 and li[j] > key:
        li[j + 1] = li[j]
        j = j - 1
    li[j + 1] = key

print("-------------------------------------")
print(li)

# ! ---------------------------Merge Short-------------------
def Merge_list(left, right):
    li = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            li.append(left[i])
            i += 1
        else:
            li.append(right[j])
            j += 1

    # Append the remaining elements from both lists
    while i < len(left):
        li.append(left[i])
        i += 1

    while j < len(right):
        li.append(right[j])
        j += 1

    return li

def Merge_Short(li):
    if len(li) <= 1:
        return li

    mid = len(li) // 2
    left = Merge_Short(li[:mid])
    right = Merge_Short(li[mid:])

    return Merge_list(left, right)

# Example usage:
li = genratelist()
print("Unsorted list -----------------------------")
print(li)
sorted_li = Merge_Short(li)
print("Sorted list -----------------------------")
print(sorted_li)

# !By Default Python use TimShort for shorting it is combination of merge short and insertion short ,it is a hybrid algo.
