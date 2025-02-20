import time

# 0 ~ 1000000를 리스트에 저장한다
test_list = [x for x in range(0, 1000001)]

# 0 ~ 1000000를 set에 저장한다
test_set = set([x for x in range(0, 1000001)])

# 특정 데이터가 리스트에 있는지 확인할 때 걸리는 시간 파악
t_0 = time.time()
print(1000000 in test_list)
t_1 = time.time()

print(f"리스트에서 걸린 시간: {t_1 - t_0}")

# 특정 데이터가 set에 있는지 확인할 때 걸리는 시간 파악
t_0 = time.time()
print(1000000 in test_set)
t_1 = time.time()

print(f"set에서 걸린 시간: {t_1 - t_0}")