n = int(input())

heights = input().split(' ')
heights = [ int(x) for x in heights ]

widths = input().split(' ')
widths = [ int(x) for x in widths ]

total_area = 0

for i in range(n):
    curr_h = heights[i]
    next_h = heights[i+1]
    curr_w = widths[i]

    a_rect = min(curr_h, next_h)*curr_w
    a_tri = abs(curr_h - next_h)*curr_w / 2
    a_fence = a_rect + a_tri
    total_area += a_fence

print(total_area)