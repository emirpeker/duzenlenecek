def find_pattern(arr):
    n=len(arr)
    for p_len in range(1,n//2+1):
        pattern=arr[:p_len]
        repeat_time=n//p_len

        if pattern*repeat_time==arr:
            return pattern,repeat_time

    return arr,1
array=[1, 2, 1, 3, 1, 2, 1, 3]
pattern,repeats=find_pattern(array)
print("Oruntu:",pattern)
print("Tekrar sayisi:",repeats)