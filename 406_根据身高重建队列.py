from typing import List 


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 0的从小到大排列
        # 记录每个数字当前的情况
        height_dict = {}
        sorted_height = []
        for p in people:
            height = p[0]
            if height not in height_dict:
                height_dict[height] = [] 
            height_dict[height].append(p)
        for height in height_dict:
            height_dict[height] = sorted(height_dict[height], key=lambda x: x[1])
        sorted_height = sorted(height_dict.keys())
        
        current_height = {k:0 for k in sorted_height}

        queue = [] 
        while len(queue) < len(people):
            match = None
            for height in sorted_height:
                # 如果这个数刚好符合要求
                if match is None and height_dict[height] and height_dict[height][0][1] == current_height[height]:
                    queue.append(height_dict[height][0])
                    height_dict[height].pop(0)
                    match = height 
                    break
            
            for height in sorted_height:
                if match >= height:
                    current_height[height] += 1
            print('====', match)
            print(queue)
            print(current_height)
            print(sorted_height)
            print(height_dict)

        return queue


if __name__ == '__main__':
    s = Solution() 
    # print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
    print(s.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))
        