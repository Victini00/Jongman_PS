def solution(h, k, boxes):
    boxes.sort()
    if h<=k:
        return 0

    if len(boxes) == 1:
        if boxes[0] > k:
            return -1
        else:
            if h-boxes[0] >k:
                return -1
            else:
                return 1

    

    min_value = 100000001
    able_index=[]
    for i in range(len(boxes)):
        if boxes[i] <= k:
            able_index.append(i)
    
    if len(able_index) >=1:
        largest_index = able_index[-1]
    else:
        return -1


    copy_boxes = [0 for _ in range(len(boxes))]
    for j in range(len(copy_boxes)):
        copy_boxes[j] = boxes[j] - boxes[largest_index]
        if solution(h-boxes[largest_index],k,copy_boxes[largest_index+1:]) == -1:
            break
        min_value = min([min_value, 1+solution(h-boxes[largest_index],k,copy_boxes[largest_index+1:])])


    if min_value == 100000001:
        return -1
    else: 
        return min_value

print(solution(12,3,[2,3,6,7,8,10,11]))