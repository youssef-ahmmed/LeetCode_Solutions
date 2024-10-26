class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        parents = [folder[0]]

        for i in range(1, len(folder)):
            if not folder[i].startswith(parents[-1] + '/'):
                parents.append(folder[i])

        return parents
