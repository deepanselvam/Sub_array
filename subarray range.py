class Solution:
    def realArray(self, ar, b, c):
        lst = []
        i = b
        while i <= c:
            lst.append(ar[i])
            i += 1
        return lst

if __name__ == "__main__":
    print("enter the length of the array: ")
    size = int(input())
    arr = []
    i = 0
    while i < size:
        arr.append(int(input()))
        i += 1
    print("enter the starting index of the array: ")
    b = int(input())
    print("enter the ending index of the array: ")
    c = int(input())
    answer = Solution()
    print(answer.realArray(arr, b, c))
