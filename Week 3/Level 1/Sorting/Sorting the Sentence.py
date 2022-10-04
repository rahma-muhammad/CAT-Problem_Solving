def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot= array[0]
        less = [ i for i in array[1:] if i[-1] <= pivot[-1]]
        greater = [ i for i in array[1:] if i[-1] > pivot[-1]]

        return quicksort(less) + [pivot] + quicksort(greater)

class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(' ')
        arr = quicksort(arr)
        newarr = []
        for a in arr:
            i = int(a[-1]) - 1
            newarr.insert(i, a[:-1])

        news = ' '.join(newarr)
        return news

t = Solution()
print(t.sortSentence("is2 sentence4 This1 a3")) #Output: "This is a sentence"
print(t.sortSentence("lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"))