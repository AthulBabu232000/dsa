height = [1,8,6,2,5,4,8,3,7]
target= 49
start=0
end=len(height)-1
result=0
minValue=0
while start<=end:
    minValue=min(height[start],height[end])
    print(height[start],height[end])
    if(result<minValue*(end-start)):
        result=minValue*(end-start)
    print(result)
    if(minValue==height[start]):
        start=start+1
    else:
        end=end-1
    
    
