# some_list = [7, 14, 28, 32, 32, '56']
#
#
# def custom_filter(list_):
#     sum_ = 0
#     for num in list_:
#         if isinstance(num, int) and num % 7 == 0:
#             sum_ += num
#     if sum_ < 83:
#         return True
#     else:
#         return False
#
#
# print(custom_filter(some_list))
'''
Напишите функцию anonymous_filter, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True,
если количество русских букв я не меньше 23 (регистр буквы неважен) и False в противном случае.
Примечание. Вызывать анонимную функцию не нужно. Только дописать ее код.
'''

anonymous_filter = lambda x: len(list(map(str, (i for i in x if i.lower() == 'я')))) > 23

print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))
