"""Find the Runner-Up Score!
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.if __name__ == '__main__':"""

    n = int(raw_input())
    arr = map(int, raw_input().split())
resultantList = []
 
for element in arr:
    if element not in resultantList:
        resultantList.append(element)

resultantList.sort()
print(resultantList[-2])