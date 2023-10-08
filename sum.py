#%%
#if __name__ == '__main__':

def calculateSum(list_data):
    if list_data.__len__() == 0:
        return 0

    else:
        sum_total = 0
        for x in list_data:
            sum_total += x
        return sum_total

assert calculateSum([]) == 0
assert calculateSum([2,3,4,5,6]) == 20
print("CalculateSum : ", calculateSum([2,3,4,5,6]))


def average(list_data):
    if list_data.__len__() == 0:
        return 0
    else:
        sum_total = 0
        for x in list_data:
            sum_total += x
        average_number =sum_total/len(list_data)
        return average_number

assert average([])==0
assert average([5,10,15,20,25]) == 15
print("Average : ", average([2,3,4,5,6]))

def multiply(list_data) :
    if list_data.__len__() == 0:
        return 0
    else:
        multiply = 1
        for x in list_data:
            multiply *= x

        return multiply

assert multiply([])==0
assert multiply([2,4,6,8,10]) == 3840
assert multiply([1,2,3,4,5]) == 120
print("Multiply : ", multiply([3,6,9,12]))



def median(list_data):
    if list_data.__len__() == 0:
        return 0
    else:
        list_data = sorted(list_data)
        middleIndex = len(list_data)//2
        if len(list_data) % 2 == 0:
            return (list_data[middleIndex-1]+list_data[middleIndex])/2
        else:
            return (list_data[middleIndex])

assert median([])==0
assert median([2,4,6,8,10])==6
assert median([1,2,3,4])==2.5
print("Median : ", median([1,2,3,4,8]))



























#%%
