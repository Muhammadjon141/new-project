import Classes_inherten
def komunnal(phone_number, card_number, ismi):
    hudud = input("Hududingizni kiriting: ")
    id = input("Id kiriting: ")
    if hudud and id:
        return Classes_inherten.Users.komunalla(id, hudud, phone_number, card_number, ismi)