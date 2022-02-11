import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
diff = 3e9+1
nums.sort()

for i in range(N-2):
    j, k = i+1, N-1
    while j < k:
        if nums[i] + nums[j] + nums[k] == 0:
            ans = [nums[i], nums[j], nums[k]]
            print(*ans)
            sys.exit(0)

        if abs(nums[i] + nums[j] + nums[k]) < diff:
            diff = abs(nums[i] + nums[j] + nums[k])
            ans = [nums[i], nums[j], nums[k]]

        if nums[i] + nums[j] + nums[k] > 0:
            k -= 1
        elif nums[i] + nums[j] + nums[k] < 0:
            j += 1

print(*ans)