#show heading.where(
    level:1
) : set text (
        20pt,
        font:"Songti SC",
        weight:700
    )

#show heading.where(
    level:1
) : set align(center)

#show heading.where(
    level:2
) : set text (
        15pt,
        font:"Songti SC"
    )

#set heading(level:1)
#show link: underline

#set text(
    font:("Menlo","PingFang SC"),
    style:"normal",
    weight:"regular",
    size: 15pt,
)

#set page(
  margin: (x: 0.9cm, y: 1.3cm),
)

#set par(
  leading: 10pt,
  justify: true
)

#let chiline() = {v(-3pt); line(length: 100%); v(-5pt)}

#[  
    #set align(center+horizon)
    #set text(
        size:50pt,
        font:"Songti SC",
        weight:"black"
    )
    Most\
    Leetcode\
    Notes\
]

#pagebreak()

= 二分搜索

```python
def binarySearch(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

#pagebreak()

= 快慢指针
```python
class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        fast = 1
        ans = len(nums)
        while (fast < ans):
            # 判断当前fast指针和slow指针
            if nums[slow] < nums[fast]:# fast 指针大于slow指针，所以移动slow指针
                slow+=1
                nums[slow]=nums[fast]
            fast +=1
        return slow + 1
```

#pagebreak()
