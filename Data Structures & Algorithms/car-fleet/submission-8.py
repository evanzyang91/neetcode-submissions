class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        pos_time = {}
        for i in range(len(position)):
            times.append((target-position[i])/speed[i])
            pos_time[position[i]] = times[-1]
        
        #find fleets
        pos_sort = sorted(position)
        fleets = 1
        while len(pos_sort) > 0:
            print(pos_time[pos_sort[len(pos_sort)-1]])
            if pos_time[pos_sort[len(pos_sort)-1]] < pos_time[pos_sort[len(pos_sort)-2]]:
                #pop the end
                #add a fleet
                fleets += 1
                pos_sort.pop(len(pos_sort)-1)
                continue
            else:
                pos_sort.pop(len(pos_sort)-2)
                #pop the one before the end
        
        return fleets