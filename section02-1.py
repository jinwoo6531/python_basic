# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print('Hello Python!')


# Separator 옵션 사용
# sep = 문자열 사이에 공백을 채워주는 기능
print('T', ' E', ' S', ' T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep="@")

# end 옵션 사용
# 끝을 이어주는 옵션
print('Welcome To', end=' ')
print('동막골')

# format 사용 [], {}, ()
print('{} and {}'.format('You', "Me"))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} arb {b}".format(a='You', b="Me"))

print("%s's favorite number is %d" % ('Eunki', 7))
