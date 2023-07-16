def find_leaders(arr):
    n = len(arr)
    leaders = [arr[n - 1]]
    max_leader = arr[n - 1]
    for i in range(n - 2, -1, -1):
        if arr[i] > max_leader:
            max_leader = arr[i]
            leaders.append(arr[i])
    leaders.reverse()
    return leaders
arr = [16, 17, 4, 3, 5, 2]
result = find_leaders(arr)
print("Leaders in the array:", result)
arr = [5, 4]
result = find_leaders(arr)
print("Leaders in the array:", result)
