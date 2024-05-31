import Class
import json
import user_page
import admin_page
import random
import datetime
import komunnallar

from datetime import datetime
class Users(Class.User):
   def __init__(self, first_name: str, last_name: str, phone_number: str, card_number: str, balanc: float, login: str, password: str, birth_date: str, status: bool) -> None:
        super().__init__(first_name, last_name, phone_number, card_number, balanc, login, password)
        self.birth_date = birth_date
        self.status = f"user"
        self.create_time = f"{datetime.date()}"

   def __str__(self) -> str:
        return f"{super().__str__()} {self.birth_date} {self.create_time}"
    
   @staticmethod
   def uzbek_service():
        phone_number1 = input("Ulangan raqamingizni kiriting: ")
        card_number1 = input("Kartangizni kiriting: ")
        with open("datas.json", encoding="utf-8") as file:
            data = json.load(file)
            for users in data["users"]:
                if users["phone_number"] == phone_number1 and card_number1 == users["card_number"]:
                  a = random.randint(1000, 9999)
                  print(f"Ushbu kodni hech kimga aytmang! {a}")
                  b = input("Kodni kiriting: ")
                  if str(b) == str(a):
                   if users["status"] == "user":
                        ismi = users["first_name"]
                        return user_page.user_page(phone_number1, card_number1, ismi)
                   elif users["status"] == "admin":
                        return admin_page.admin_page()
                  else:
                      print("Jo'natilgan kodni kiriting")
                      return Users.uzbek_service()
            else:
                print("Hatolik Qayta harakat qiling:")
                return Users.uzbek_service()
            
   def uzbek_service_new():
        with open("datas.json", encoding="utf-8") as file:
            date = json.load(file)
        first_name1 = input("Ismingizni kiriting: ")
        last_name1 = input("Familiyangizni kiriting: ")
        phone_number1 = input("Raqamingizni kiriting: +998 >>> ")
        card_number1 = input("Karta raqam kiriting: ")
        bith_date = input("Tugilgan kuningizni kiriting(yil-oy-kun): ")
        new_user ={
                        "first_name": f"{first_name1}",
                        "last_name": f"{last_name1}",
                        "phone_number": f"{phone_number1}",
                        "card_number": f"{card_number1}",
                        "balanc": 0,
                        "birth_date": f"{bith_date}",
                        "status": f"user",
                        "create_time": f"{datetime.now()}"
                    }
        while True:
         date["users"].append(new_user)
         a = random.randint(1000, 9999)
         print(f"Ushbu kodni hech kimga aytmang! {a}")
         b = input("Kodni kiriting: ")
         for users in date["users"]:
                 if str(a) == str(b):
                  if len(phone_number1) == 9:
                   if len(card_number1)  ==16:
                    if users["card_number"] != card_number1 and users["phone_number"] != phone_number1:
                     with open("datas.json", "w") as f:
                      json.dump(date, f, indent=6)
                     print("Muvafaqqiyatli ro'yhatdan o'tdingiz! ")
                     return Users.uzbek_service()
                    else:
                     print("Bunday foydalanuvchi mavjud! ")
                     return Users.uzbek_service_new()
                   else:
                      print("Karta raqam 16xonadan iborat bo'lishi kerak! ")
                      return Users.uzbek_service_new()
                  else:
                      print("Telefon raqam 9xonalik bo'lishi kerak! ")
                      return Users.uzbek_service_new()
         else:
             print("Jo'natilgan kodni kiriting")
             return Users.uzbek_service_new()
    
   @staticmethod
   def check_card_number(card_number1):
       with open("datas.json", encoding="utf-8") as file:
          data = json.load(file)
          for user in data["users"]:
             if user["card_number"] == str(card_number1):
                if len(card_number1) == 16:
                   return user["card_number"]
                else:
                 print("16 xonalik son kiriting!")
                 return Users.check_card_number(card_number1)
          else:
            print("Bunday karta mavjud emas!")
            return Users.uzbek_service()

   @staticmethod         
   def check_phone_number(phone_number1):
       with open("datas.json", encoding="utf-8") as file:
          data = json.load(file)
          for user in data["users"]:
            if user["phone_number"] == phone_number1:
                if len(phone_number1) == 9:
                   return user["phone_number"]
                else:
                 print("9 xonalik son kiriting!")
                 return Users.check_phone_number(phone_number1)
            else:
              print("Bunday telefon raqamli foydalanuvchi mavjud emas!")
              return Users.uzbek_service()
    
   @staticmethod
   def pul_otkaz(phone_number, card_number, ismi):
       kimga = input("Qabul qiluvchi karta raqamini kiriting: ")
       with open("datas.json", encoding="utf-8") as file:
          data = json.load(file)
          for i in data["users"]:
            if i["card_number"] == card_number and i["card_number"] >= str(0):
               kimdan = float(i["card_number"])
               for user in data["users"]:
                    if user["card_number"] == kimga:
                      ism = user["first_name"]
                      print(f"Foydalanuvchi ismi: {ism}")
                      if len(kimga) == 16:
                       miq = input("O'tkazmoqchi bo'lgan miqdorni kiriting: ")
                       miqdor = int(miq)
                       if kimdan >= miqdor:
                        print("yaxshi")
                        for k in range(len(data["users"])):
                         kimgan = float(kimga)
                         if float(data["users"][k]["card_number"]) == kimgan:
                            data["users"][k]["balanc"] = float(data["users"][k]["balanc"]) + miqdor
                         elif float(data["users"][k]["card_number"]) == float(card_number):
                            data["users"][k]["balanc"] = float(data["users"][k]["balanc"]) - miqdor
                            card_number2 = data["users"][k]["card_number"]
                            card_number3 = data["users"][k]["balanc"]
                        print(card_number2, card_number3)
                        with open("datas.json", "w") as f:
                           json.dump(data, f, indent=6)
                        print("O'tkazma muvaffaqiyatli bajarildi ")
                        return user_page.user_page(phone_number, card_number2, ismi)
                       else:
                        print("Sizda yetarlik mablag' mavjud emas")
                        return Users.pul_otkaz(phone_number, card_number, ismi)
                      else:
                       print("Bunday foydalanuvchi yo'q")
                       return Users.pul_otkaz(phone_number, card_number, ismi)
               else:
                 print("Bunday foydalanuvchi yo'q")
                 return Users.pul_otkaz(phone_number, card_number, ismi)

   def balanc(phone_number, card_number, ismi):
       with open("datas.json", encoding="utf-8") as file:
          data = json.load(file)
          for user in data["users"]:
             if user["card_number"] == card_number:
                balans = user["balanc"]
                print(f"Sizning balansingiz: {balans} so'm")
                return user_page.user_page(phone_number, card_number, ismi)
             
   @staticmethod
   def komunalla(id, hudud, phone_number, card_number, ismi):
      with open("dav_data.json", encoding="utf-8") as file:
         data = json.load(file)
         for tashkilot in data["tashkilot"]:
            if tashkilot["id"].lower() == id.lower() and tashkilot["hudud"].lower() == hudud.lower():
               if tashkilot["id"][:2:] == "30":
                  print(f"""
                              Elektr energiya uchun to'lov:""")
               if tashkilot["id"][:2:] == "63":
                  print(f"""
                              Tabiiy gaz uchun to'lov:""")        
               print(f"""
                        Viloyatingiz: {tashkilot["hudud"]}""")
               miqdor = input("O'tkazmoqchi bo'lgan miqdoringizni kiriting: ")
               if miqdor.isdigit():
                  with open("datas.json", encoding="utf-8") as fi:
                     user1 = json.load(fi)
                     for i in range(len(user1["users"])):
                        if user1["users"][i]["card_number"] == card_number:
                           user1["users"][i]["balanc"] = user1["users"][i]["balanc"] - float(miqdor)
                           andi = user1["users"][i]["balanc"]
                           print(andi)
                           with open("datas.json", "w") as f:
                              json.dump(user1, f, indent=6)
                     for k in range(len(data["tashkilot"])):
                        if data["tashkilot"][k]["id"] == id:
                           data["tashkilot"][k]["mablag'"] = data["tashkilot"][k]["mablag'"] + float(miqdor)
                           with open("dav_data.json", "w") as fi:
                              json.dump(data, fi, indent=6)
                              nomi = tashkilot["nomi"]
                              print(f"""
                                          Hurmatli {ismi} sizdan {nomi}ga {miqdor} pul o'tkazmasi
                                          Muvaffaqiyatli amalga oshirildi""")
               else:
                  print("faqat son kiriting!")
                  return komunnallar.komunnal(phone_number, card_number, ismi)
         else:
            print("Bunday tashkilot topilmadi! ")
            return user_page.user_page(phone_number, card_number, ismi)
      