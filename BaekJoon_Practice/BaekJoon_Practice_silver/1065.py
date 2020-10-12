# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 입력 : 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 출력 : 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

n = int(input())
cnt = 0

def hansu(a):
    a = str(a)
    my_list = []
    for i in range(len(a) - 1):
        my_list.append(int(a[i]) - int(a[i+1]))
    if len(set(my_list)) == 1:
        return True
    
for i in range(1,n+1):
    if i <= 99:
        cnt += 1
    else:
        if hansu(i) == True:
            cnt += 1
        else:
            pass
 
print(cnt)