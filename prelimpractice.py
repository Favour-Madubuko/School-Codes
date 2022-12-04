'''def min_index(firstlist, secondlist):
    the_min = firstlist
    the_max = secondlist
    the_index = []
    for each_number in range(len(the_min)):
        if the_min[each_number] < the_max[each_number]:
            final_index = the_min.index(the_min[each_number])
            the_index.append(final_index)
    return the_index
print(min_index([40, 50, 10, 90, 100, 70],[60, 20, 19, 95, 30, 20]))
'''

'''
def pairwise_product(firstlist, secondlist):
    the_min = firstlist
    the_max = secondlist
    the_index = []
    for each_number in range(len(the_min)):
        final_product = the_min[each_number] * the_max[each_number]
        the_index.append(final_product)
    return the_index
print(pairwise_product([40, 50, 10, 90] ,[6, 2, 2, 5]))
'''

'''
def pairwise_ratio(firstlist, secondlist):
    the_index = []
    for each_number in range(len(firstlist)):
        final_product = round((firstlist[each_number] / secondlist[each_number]), 3)
        the_index.append(final_product)
    return the_index
print(pairwise_ratio([40, 50, 10, 90] ,[60, 20, 19, 95]))
'''


