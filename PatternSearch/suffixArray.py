from collections import defaultdict
class SuffixArray:
    def __init__(self):
        self.suffixes = []

    def suffixArray(self, s):
        self.suffixes = [(s[i:], i) for i in range(len(s))]
        self.suffixes.sort(key=lambda x: x[0])
        return [s[1] for s in self.suffixes]

    def search(self, txt, pat, n):
        m = len(pat)
        l = 0
        r = n-1
        found = False
        lst = list(self.suffixes)
        while l<=r and not found:
            mid = (l+r)//2;
            start = lst[mid][1]
            val = txt[start :start+len(pat)]
            if pat == val:
                found = True
            else:
                if pat < val:
                    r = mid - 1
                elif pat > val:
                        l = mid + 1
        return found

s = SuffixArray()
str = "banana"
s.suffixArray(str)
if (s.search(str, "nna", 6)):
    print("Found")
else:
    print("not found")