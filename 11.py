# import os
#
# file_path_1 = os.path.join(os.getcwd(), "1.txt")
# file_path_2 = os.path.join(os.getcwd(), "2.txt")
# file_path_3 = os.path.join(os.getcwd(), "3.txt")
# list_file = [file_path_1, file_path_2, file_path_3]
#
#
# def new_file (files):
#     file_dict = {}
#     for file in file_path:
#         count = 0
#         name = os.path.basename(file)
#         with open(file, encoding='utf-8') as f:
#             for line in f:
#                 count +=1
#             file_dict[name] = count
#     come_dict = reader(list_file)
#     sort_list = list(come_dict.items())
#     sort_list.sort(key=lambda i: i[1])
#     with open('new_file.txt', 'w', encoding='utf-8') as f:
#         for id in sort_list:
#             f.write(f'{id[0]}\n')
#             f.write(f'{id[1]}\n')
#             with open(id[0], encoding='utf-8') as fl:
#                 data = fl.read()
#                 f.write(f'{data}\n')
#
# new_file(list_file)
#
# with open ('new_file.txt', encoding='utf-8') as f:
#     print(f.read())
#
#
#
# import os
#
# file_path_1 = os.path.join(os.getcwd(), "1.txt")
# file_path_2 = os.path.join(os.getcwd(), "2.txt")
# file_path_3 = os.path.join(os.getcwd(), "3.txt")
# list_file = [file_path_1, file_path_2, file_path_3]
#
# def reader (file_path):
#     file_dict = {}
#     for file in file_path:
#         count = 0
#         name = os.path.basename(file)
#         with open(file, encoding='utf-8') as f:
#             for line in f:
#                 count +=1
#             file_dict[name] = count
#
#     return file_dict
#
#
# come_dict = reader(list_file)
# sort_list = list(come_dict.items())
# sort_list.sort(key=lambda i: i[1])
#
#
# with open ('new_file.txt', 'w', encoding='utf-8') as f:
#     for id in sort_list:
#         f.write(f'{id[0]}\n')
#         f.write(f'{id[1]}\n')
#         with open(id[0], encoding='utf-8') as fl:
#             data = fl.read()
#             f.write(f'{data}\n')
#
#
# with open ('new_file.txt', encoding='utf-8') as f:
#     print(f.read())