class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            j, k = 0, len(image[i]) - 1
            while j < k:
                image[i][j], image[i][k] = image[i][k], image[i][j]
                image[i][j] ^= 1
                image[i][k] ^= 1

                j += 1
                k -= 1
            
            if j == k:
                image[i][j] ^= 1

        return image
