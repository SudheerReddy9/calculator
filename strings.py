# # # # # # # # # # # # # # # # # # # # a = 'learn'
# # # # # # # # # # # # # # # # # # # # b = 'about'
# # # # # # # # # # # # # # # # # # # # c = 'string'
# # # # # # # # # # # # # # # # # # # # d = 'variable'
# # # # # # # # # # # # # # # # # # # # e = 'in'
# # # # # # # # # # # # # # # # # # # # f = 'python'
# # # # # # # # # # # # # # # # # # # # print(len(d))
# # # # # # # # # # # # # # # # # # # # print(len(d) - 1)
# # # # # # # # # # # # # # # # # # # # print(d[len(d) - 1])
# # # # # # # x = [1,2,3, ['Y' , 'Z'] , 4]
# # # # # # # print(x.pop())
# # # # # # # print(x.pop(3))
# # # # # # # x.append(4)
# # # # # # # print(x)
# # # # # # # def truncate(A, B):
# # # # # # #     if(A < len(B)):
# # # # # # #         return B[1:A]
# # # # # # #     else:
# # # # # # #         return B[A-1]
# # # # # # # s1 = "Three shalt be the number thou shalt count"
# # # # # # # C = truncate(5, s1.split())
# # # # # # # s2 = "King of the Britons"
# # # # # # # D = truncate(4, s2.split())
# # # # # # # #print(s1.split())
# # # # # # # print(C)
# # # # # # # print(D)
# # # # # # # def main():
# # # # # # #     scores = [
# # # # # # #         [77,68,86,73],
# # # # # # #         [96,87,89,81],
# # # # # # #         [70,90,86,81]
# # # # # # #     ]

# # # # # # #     students = len(scores)
# # # # # # #     exams = len(scores[0])
    
# # # # # # #     for i in range(students):
# # # # # # #         for j in range(exams):
# # # # # # #             print(scores[1][3], end = " ")
# # # # # # #         print()
        
# # # # # # # main()
# # # # # # # # # # print(10%3**1**2-8)
# # # # # # # # # # price = int(68.549)
# # # # # # # # # # print(price)
# # courses = {'Sudheer': "Pokala",
# #            'Bhargav': 'Manchina',
# #            'Manish':"Bandreddi",
# #            'Venky':'Jadi',
# #            'Sudheer':"reddy"
# # }

# # # for x ,y in courses.items():
# # #     if x == 'Sudheer':
# # #         print(y)
# # #     else:
# # #         print(x)
# # del courses['Sudheer']
# # print(courses.get('Sudheer','Chotu'))
# # # # # # myString = "spam & essggs"
# # # # # # print(myString.find("s"))
# # # # # # print(myString.rfind("s"))
# # # # # # print(myString[1:3])
# # # # # # # x = 0
# # # # # # # def main():
# # # # # # #     global x
# # # # # # #     trivial()
# # # # # # #     x = x+1
# # # # # # #     print(x)
# # # # # # # def trivial():
# # # # # # #     x = 0
# # # # # # #     x = x+1

# # # # # # # main()
   

# # # # # # my_list = [10,20,1,36,12,12,32,21]
# # # # # # my_list.append(30)
# # # # # # print(my_list)
# # # # # # my_list.extend([30,12])
# # # # # # print(my_list)
# # # # # # my_list.insert(7,30)
# # # # # # print(my_list)
# # # # # # # # # # class Membership():
# # # # # # # # # #     def __init__(self, usertype):
# # # # # # # # # #         self.type = usertype
# # # # # # # # # #         self.extras = str()
# # # # # # # # # #         self.extracost = float()
# # # # # # # # # #         self.dues = float()
    
# # # # # # # # # #     def DetermineBaseCost(self):
# # # # # # # # # #         if self.type == "single":
# # # # # # # # # #             self.dues = 50
# # # # # # # # # #         else:
# # # # # # # # # #             self.dues = 100

# def main():
#     bundles = [30,40,20,10]
#     a(bundles)
#     b(bundles)

# def a(bundles):
#     c = 0
#     for i in range(len(bundles)):
#         c = c + bundles[i]
#     d = c // i

#     print(c)
#     print(d)

# def b(bundles):
#     e = bundles[0]
#     for i in range(len(bundles)):
#         if bundles[i] > e:
#             e = bundles[i]

#     print(e)
# main()










# # # # # # # # # L = ["🥚","🐔", "12"]

# # # # # # # # # L.reverse
# # # # # # # # # print(L[0])

# # # # # # # text = 'bat bAll'


# # # # # # # # print(text.lower())
# # # # # # # # print(text.upper())
# # # # # # # # print(text.title())
# # # # # # # # print(text.capitalize())
# # # # # # # print(text.replace('b', 'ro'))
# # # # # # # print(text)
# # # # # x =range(2,9,2)
# # # # # print(x)
# # # # x = 0
# # # # y = 0
# # # # for x in range(1,3,1):
# # # #     for y in range(3,5,1):
# # # #         print(x *y, end = '')
# # # spam = '7'
# # # spam = spam + "0"
# # # eggs = int(spam) + 3
# # # print(float(eggs))
# candy = input("numbers of candies")
# price = 2.0
# cost = candy * price
# print("you need to $", cost , sep="")
