def trap(height):
    """
    42.接雨水
    0、初始，i=0
    1、j=i+1，如果第i列后面一列不比其高，则i往右移一列，否则：
    2、j往右移，找到height[j]>height[j-1]时，停下:
    a)如果：height[j]>=height[i]，则计算可装雨水量，并将i移到j的位置，进行下一轮计算
    b)如果：height[j]<height[i]，则k=j+1为，往右移动k，如果height[k]>=height[j]，则移动j到k的位置，并进行下一轮：否则，计算当前可装雨水量，并将i移到j的位置，然后再从1开始
    """
    if not height or len(height) < 3:
        return 0
    n = len(height)
    result,i = 0,0
    while i < n-2:
        j = i + 1
        while j < n:
            if j-i == 1 and height[j]>=height[i]:
                i = j - 1
                break
            if j-i> 1 and height[j] >= height[j-1]:
                if height[j] >= height[i]:
                    tmp,k=0,i+1
                    while k < j:
                        tmp+=height[k]
                        k +=1
                    result += height[i]*(j-i-1)-tmp
                    i = j - 1
                    break
                else:
                    t = j + 1
                    while t < n: 
                        if height[t]>=height[j]:
                            j = t
                            break
                        else:
                            t += 1
                    if t == n-1 or t == n:
                        h = min(height[j],height[i])
                        tmp,k = 0, i+1
                        while k < j:
                            tmp += height[k] if h > height[k] else h
                            k +=1
                        result += h*(j-i-1)-tmp
                        i = j - 1
                        break
            else:
                j += 1
        i += 1
    return result


if __name__ =="__main__":
    height =[5,4,2,3] # [7,2,4] # [0,1,0,2,1,0,1,3,2,1,2,1] # [4,2,0,3,2,5] # [9,6,8,8,5,6,3] #  [5,4,2,3,4] # [5,2,1,2,1,5] #  [5,2,1,2,1,5] # [4,9,4,5,3,2] # [0,1,0,2,1,0,1,3,2,1,2,1] #  
    print(trap(height))