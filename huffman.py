size = int(input())
input_list = list(map(int, input().split()))
anser = 0
while size > 1 :
    input_list =  sorted(input_list)
    print(input_list)
    marged_num = input_list[0] + input_list[1]
    anser += marged_num
    input_list.append(marged_num)
    input_list.pop(0)
    input_list.pop(1)
    size -= 1

print(anser)
