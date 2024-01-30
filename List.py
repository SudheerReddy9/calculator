# # # nums = [6, 1, 8, 9,26,12]
# # # print(nums)
# # # [6, 1, 8, 9, 26, 12]
# # # print(nums[4])
# # # 26
# # # print(nums[-1])
# # # 12
# # # names = ['Sudheer', 'Bhargav', 'Manish', 'Randeep']
# # # print(names)
# # # ['Sudheer', 'Bhargav', 'Manish', 'Randeep']
# # # value = [nums, names]
# # # print(value)
# # # [[6, 1, 8, 9, 26, 12], ['Sudheer', 'Bhargav', 'Manish', 'Randeep']]
# # # nums.append(18)
# # # print(nums)
# # # [6, 1, 8, 9, 26, 12, 18]
# # # nums.insert(9,65)
# # # print(nums)
# # # [6, 1, 8, 9, 26, 12, 18, 65]
# # # nums.remove(18)
# # # print(nums)
# # # [6, 1, 8, 9, 26, 12, 65]
# # # nums.pop(1)
# # # 1
# # # print(nums)
# # # [6, 8, 9, 26, 12, 65]
# # # nums.pop()
# # # 65
# # # print(nums)
# # # [6, 8, 9, 26, 12]


# # # del nums[3:]
# # # print(nums)
# # # [6, 8, 9]
# # # nums.extend([25, 12, 99, 87])
# # # print(nums)
# # # nums =[6, 88, 9, 25, 12, 99, 87]
# # # #nums1 = [6,[9, 26, 6,[12,10]], 65]
# # # print(nums.reverse())
# # #print(nums[1][3][1])
# # line = ['Sudheer', 'Bhargav', 'Manish', 'Randeep', 'venky', '']
# # print("@gmail.com ".join(line))
# words = ["banana", "cherry", "apricot", "coconut", "kiwi", "avocado", "apple"]
# for word in words:
#     if word.startswith("A") or word.startswith("a"):
#         print(word)
#         break
my_list = ['a',1,2,'c',3]
new_list = 'b'
my_list.insert(2, new_list)
print(my_list)