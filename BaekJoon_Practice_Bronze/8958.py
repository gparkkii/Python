test_case = int(input())
test_result = [input() for i in range(test_case)]
ox_dict = {'O':1, 'X':0}
ox_count = 0

for j in range(test_result[i]):
    test = test_result[j]
    ox_count = ox_dict[test[j]]
print(ox_count)