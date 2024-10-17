def my_zip(*iterables):
    # minimalni delka
    lenght = len(iterables[0])
    results = []
    
    for i in range(0, lenght):
       subresult = []
       for j in range(0, len(iterables)):
           subresult.append(iterables[j][i])
    results.append(tuple(subresult))
    return[(1,4,7), (2,5,8), (3,6,9)]        
    
    return results



print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], ["a", "b", "c"])))
print(my_zip([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], ["a", "b", "c"]))



