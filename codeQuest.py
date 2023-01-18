# Welcome to the Lumos Coding Quest
# you have been given a linked list with duplicate values
# upon running this code, you will see a string that has been formed by collecting the data in the nodes of the linked list
# you need to complete the "MyAnswer" function and ensure that it removes the duplicate nodes from the linkedlist
# when you collate the string that this new linked list contains, you will get the link to the whitelist form
# Note:- "list" represents the said linked list

from helper import *
def duplicatesCheck(aList):
   addList = []
   delList = []
   delDict = {}
   finalList = []
   last =[]
   for i in range(0,len(aList)):
      index = -1
      for j in range(0,len(aList)):
         index += 1
         if aList[i] == aList[j]:
            delList.append(index)
      delDict[aList[i]] = delList
      delList = []

   for k,v in delDict.items():
      for i in range(0, len(v)):
         if i != 0 and len(v) > 1:
            finalList.append(v[i])

   last = sorted(finalList)
   return last
   
def removeLinkedListNode(self, position):
   if self.headval is None:
            return
   index = 0
   current = self.headval
   while current.nextval and index < position:
      previous = current
      current = current.nextval
      index += 1
   if index < position:
      print("\nIndex is out of range.")
   elif index == 0:
      self.headval = self.headval.nextval
   else:
      previous.nextval = current.nextval
      # current = None #Optional statement

def firsttime(self):
   myList = []
   answer = ""
   myVal = self.headval
   while myVal is not None:
      if myVal.dataval not in myList:
         myList.append(myVal.dataval)
         answer += myVal.dataval
      myVal = myVal.nextval
   return answer

def MyAnswer(mylinkdlist):
   aList = []
   aList.append(mylinkdlist.headval.dataval)
   aList.append(e1.dataval)
   aList.append(e2.dataval)
   aList.append(e3.dataval)
   aList.append(e4.dataval)
   aList.append(e5.dataval)
   aList.append(e6.dataval)
   aList.append(e7.dataval)
   aList.append(e8.dataval)
   aList.append(e9.dataval)
   aList.append(e10.dataval)
   aList.append(e11.dataval)
   aList.append(e12.dataval)
   aList.append(e13.dataval)
   aList.append(e14.dataval)
   aList.append(e15.dataval)
   aList.append(e16.dataval)
   aList.append(e17.dataval)
   aList.append(e18.dataval)
   aList.append(e19.dataval)
   aList.append(e20.dataval)
   aList.append(e21.dataval)
   aList.append(e22.dataval)
   aList.append(e23.dataval)
   aList.append(e24.dataval)
   aList.append(e25.dataval)
   aList.append(e26.dataval)
   aList.append(e27.dataval)
   aList.append(e28.dataval)
   aList.append(e29.dataval)
   aList.append(e30.dataval)
   aList.append(e31.dataval)
   aList.append(e32.dataval)
   aList.append(e33.dataval)
   aList.append(e34.dataval)
   aList.append(e35.dataval)
   aList.append(e36.dataval)
   aList.append(e37.dataval)
   aList.append(e38.dataval)
   aList.append(e39.dataval)
   aList.append(e40.dataval)
   aList.append(e41.dataval)
   aList.append(e42.dataval)
   aList.append(e43.dataval)
   aList.append(e44.dataval)
   aList.append(e45.dataval)
   aList.append(e46.dataval)
   aList.append(e47.dataval)
   aList.append(e48.dataval)
   aList.append(e49.dataval)
   aList.append(e50.dataval)
   aList.append(e51.dataval)
   aList.append(e52.dataval)
   aList.append(e53.dataval)
   aList.append(e54.dataval)
   aList.append(e55.dataval)
   aList.append(e56.dataval)
   aList.append(e57.dataval)
   aList.append(e58.dataval)
   aList.append(e59.dataval)
   aList.append(e60.dataval)
   indexValues = duplicatesCheck(aList)
   # Associate firsttime method with the SLinkedList class
   SLinkedList.firsttime = firsttime
   # Associate removeLinkedListNode with the SLinkedList class
   SLinkedList.removeLinkedListNode = removeLinkedListNode
   # remove linked list based on duplicate indices found
   for i in range(0, len(indexValues)):
      mylinkdlist.removeLinkedListNode(indexValues[i]-i)
   #Initialize myanswer to a string of 0 length
   myanswer = ""
   mylinkdlist.listprint()
   #call the firsttime method on mylinkdlist to eliminate duplicates
   myanswer = mylinkdlist.firsttime()
   #Display the Lumos Metaverse hyperlink
   # Expected output -> https://forms.lumoslabs.co/survey/t/65a5a0c3-15b9-42da-a99c-06622e0c7bac/r/o
   print(myanswer)

#Call the MyAnswer function with the created linkdlist with 60 nodes
MyAnswer(linkdlist)
