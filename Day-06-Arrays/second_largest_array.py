class Solution:
    def getSecondLargest(self, arr):

      """///////////// NAIVE APPROACH //////////"""
      """arr.sort()
        second_largest = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] == arr[len(arr)-1]:
                second_largest = second_largest
            elif arr[i] > second_largest:
                second_largest = arr[i]
        return second_largest"""   
      """///////////Time Complexity here is O(nlog(n))/////////////"""

      """///////////// EXPECTED APPROACH HAVING TC O(N) ///////////"""
      second_largest = -1
      largest = -1
        
      for i in range(0,len(arr)):
          if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
          elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
      return second_largest