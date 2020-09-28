# 하고싶은 대로만 한다면 다 된다고 믿어!
# 엘리스 홈페이지의 비밀번호를 어떻게 설정할지 고민이 많던 건웅은 듣고 있던 노래 윤하 - 비밀번호 486에서 영감을 받아 다음과 같이 비밀번호를 만들기로 했습니다.
# 4 = love / 6 = kiss / 8 = smile
# 예를 들어 '48686'의 숫자가 입력되면
# 'lovesmilekisssmilekiss'와 같은 문자열 비밀번호를 반환합니다.

# 이렇게 해봐요!
# 주어진 조건에 맞는 비밀번호를 만들어주는 함수 yoonHa()를 만들어봅시다.

# 인자 : 숫자 nums
# 반환값 : 변환한 비밀번호 문자열

# Hints!
# 1.문자열의 각 글자를 반복 인자로 사용할 수 있어요.
# for i in "486":
#    print(i)

# 2.문자열에 연산자를 사용해 간단하게 문자열을 붙일 수 있어요.
# str1 = ""
# str2 = "love"
# str1 = str2 + str2 + str2
# print(str1)

# 3.사전형 자료형을 활용하면 더욱 쉽게 문제를 해결할 수 있어요.
# 4.입력되는 수는 4, 8, 6 만 있어요.
# 5.예시로 주어진 486은 예시예요. 모든 4, 8, 6의 조합에 대해 만족하도록 코드를 작성해주세요.


# 채점을 위한 코드입니다. 이를 수정하지 마세요!



password = {"4": "love", "8": "smile", "6": "kiss"}

def yoonHa(nums):
    words = str(nums)
    str1 = ""
    for i in words:
        str1 = str1 + password[i]
    return str1

nums = int(input())
print(yoonHa(nums))