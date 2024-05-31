class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str, card_number: str, balanc: float, login: str, password: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.card_number = card_number
        self.balanc = balanc
        self.login = login
        self.password = password

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.phone_number} {self.card_number} {self.balanc} {self.login} {self.password}"
    