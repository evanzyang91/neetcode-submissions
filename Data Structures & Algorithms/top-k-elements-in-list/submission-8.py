class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # preprocess frequencies
        unique = {}
        for num in nums:
            if num not in unique:
                unique[num] = 1
            else:
                unique[num] += 1

        # [freq, num]
        counts = []
        for key in unique:
            counts.append([unique[key], key])
        counts.sort()

        output = []
        while len(output) < k:
            output.append(counts.pop()[1])
        return output

        
