# Sum of Positive Numbers in array

def positive_sum(arr):
    s = 0
    for i in arr:
        if i > 0 :
            s = s+i
    return s
<------------------------------------------------------->
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

<------------------------------------------------------->

def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))

<------------------------------------------------------->

def positive_sum(arr):
    return sum( max(i, 0) for i in arr )

<------------------------------------------------------->

#lambda Function
positive_sum = lambda a: sum(e for e in a if e > 0)


<------------------------------------------------------->

#lambda Function
positive_sum=lambda a:sum(x>0and x for x in a)

<------------------------------------------------------->

#array's summing
def positive_sum(arr):
    nums = [num for num in arr if num > 0]
    return sum(nums)






