#Quiz 1
class new_Id:
    def __init__(self, name, old, phone):
        self.name = name
        self.old = old
        self.phone = phone

    def information(self):
        print(f"이름: {self.name}")
        print(f"나이: {self.old}")
        print(f"전화번호: {self.phone}")


membership = new_Id("계정 이름은 김도영이며", "나이는23이고", "번호는 010-3376-8649입니다")
membership.information()

#Quiz 2
def check_length_of_message(message):
    if message > 20:
        return "100원"
    else:
        return "50원"

user_input_message = input("문자를 입력하세요")
length = len(user_input_message)
print(check_length_of_message(length))
