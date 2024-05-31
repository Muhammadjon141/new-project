import Classes_inherten
import komunnallar
import uzbek_service
def user_page(phone_number, card_number, ismi):
    xizmat = input(f"""
                   Assalomu aleykum {ismi}
                   1. Pul o'tkazish
                   2. Balansni ko'rish
                   3. Kommunal to'lovlar
                   0. Orqaga
                       >>> """)
    if xizmat == "1":
        return Classes_inherten.Users.pul_otkaz(phone_number, card_number, ismi)
    elif xizmat == "2":
        return Classes_inherten.Users.balanc(phone_number, card_number, ismi)
    elif xizmat == "3":
        return komunnallar.komunnal(phone_number, card_number, ismi)
    elif xizmat == "0":
        return uzbek_service.uzbek_service()
    else:
        print("Bunday xizmat mavjud emas!")
        return user_page(phone_number, card_number, ismi)