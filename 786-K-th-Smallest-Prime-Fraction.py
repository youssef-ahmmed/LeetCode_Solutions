class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        frac_map = {}

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                frac_map[f'{arr[i]}/{arr[j]}'] = arr[i] / arr[j]

        frac_map = {k: v for k, v in sorted(frac_map.items(), key=lambda item: item[1])}

        return list(map(int, list(frac_map.keys())[k - 1].split('/')))
