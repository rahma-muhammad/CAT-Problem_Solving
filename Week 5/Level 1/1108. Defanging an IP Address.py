class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

t =Solution()
print(t.defangIPaddr("1.1.1.1")) #Output: "1[.]1[.]1[.]1"