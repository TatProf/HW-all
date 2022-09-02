# hw 9.08
#на вход программа получает 2 числа через пробел, не иначе.
# выведите сумму этих двух чисел .Воспользуйтесь функцией map
# elems=[int(i) for i in input("Enter nums: ").split()]
#
# rez= (map(lambda x:sum(elems),elems))
# print(*rez)


# hw 11.08

# HT_14_1
# создать класс Dog.
# класс имеет 4 атрибута:
# height,weight,name,age.
# класс имеет 3 метода: jump,run,bark.
# каждый метод выводит сообщение на экран.
# создать объект класс Dog,вызвать все методы объекта
# и вывести на экран все его атрибуты.


# class Dog:
#     def __init__ (self,height,weight,name,age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#
#     def jump(self):
#         print(f'{self.name}, прыгает')
#
#     def run (self):
#         print(f'{self.name},бегает')
#
#     def bark (self):
#         print(f'{self.name}, гав-гав')
#
#     def change_name(self,new_name):
#         self.name=new_name
#         return (new_name)
#
#
# bolonka=Dog('28cm ','3 kg','Mina','2 year',)
# print(bolonka.__dict__)
# bolonka.jump()
# bolonka.run()
# bolonka.bark()
# HT_14_2
# добавит в класс Dog метод change_name.
# Метод принимает на входе новое имя и меняет атрибут у имени объекта.
# создать объект класса .вывести имя.вызватт метод change_name. вывести имя
#
#
# chow= Dog('50cm ','20 kg','Flip','5 year',)
# print((chow.__dict__))
# print(chow.change_name('Pilot'))
# print((chow.__dict__))
# #

