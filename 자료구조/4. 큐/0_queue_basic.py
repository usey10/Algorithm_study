# python 에서 큐 사용하기(리스트 응용)
queue = []


for i in range(1,11):
    queue.append(i) # put()
print(queue)

print(queue[0]) # peek() 는 [0] 이용

for i in range(1,11):
    val = queue.pop(0) # get() 은 pop(0) 을 이용
    print(val, end=' ')
print()



# 패키지 사용하여 큐 사용하기
# 멀티 프로세싱에서 안정적으로 사용할 수 있음.
from queue import Queue

queue = Queue()

for i in range(1,11):
    queue.put(i)

# print(queue.peek())  # peek() 구현되어있지 않음.

for i in range(1,11):
    val = queue.get()
    print(val, end=' ')
print()

