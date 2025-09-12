# # Наследование
# # Родительский/ супер класс
# class Hero:
#
#
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hr = hp
#
#     def action(self,):
#         print(f"{self.name} Base action")
#
# Kirito_1 = Hero("Kirito", 100, 1000)
#
# #Дочерний класс
# class HeroMage(Hero):
#
#     def cast_spell(self):
#         print(f"{self.name} fire!!!")
#
# class HeroWar(HeroMage):
#     pass
#
# Kirito = HeroMage("Kirito", 100, 1000)
#
# asuna = HeroWar("Asuna", 199, 19990)
#
#
# # Kirito.cast_spell()
#

#Полиморфизм
class BaseUser:
      def __init__(self, login, password, user_name):
            self.login = login
            self.password = password
            self.user_name = user_name

      def repost(self, text):
            print(f"{self.user_name} added new report \n {text}")

ardager = BaseUser("ardger", 12344321, "mr.ardager")

class VipUser(BaseUser):
      pass

john = VipUser("john", 123321, "John Doe")

ardager.repost("Aloha")
john.repost("i'm vip John")