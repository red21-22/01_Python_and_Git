#Quiz 1
import random

num = 1
def random_lotto():
    result = []
    while len(result) < 6:
        num = random.randint(1,45)
        if num not in result:
            result.append(num)
    return result
print(random_lotto())

#Quiz 2
class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1,10):
            print(f"{self.num} X {i} = {self.num * i}")

#Quiz 2 출력
five_dan = Gugudan(5)
five_dan.output()

#Quiz 3
# 게임
class Game:
    # 초기화 함수 (생성자)
    def __init__(self, name, level, HP, MP):
        self.name = name
        self.level = level
        self.HP = HP
        self.MP = MP

    # 캐릭터 정보 출력
    def display_info(self):
        print(f"이름: {self.name}, 레벨: {self.level}, 체력: {self.HP}, 마나: {self.MP}")

    # 공격
    def attack(self, target):
        if self.HP > 0:
            print(f"{self.name}이(가) {target}을(를) 공격했습니다!")
        else:
            print(f"{self.name}은(는) 쓰러져서 공격할 수 없습니다.")

    # 마법 사용
    def cast_spell(self, spell_name):
        if self.MP >= 10:
            self.MP -= 10
            print(f"{self.name}이(가) {spell_name} 마법을 사용했습니다! 남은 마나: {self.MP}")
        else:
            print(f"{self.name}의 마나가 부족합니다.")

    # 체력 회복
    def heal(self, amount):
        self.HP += amount
        print(f"{self.name}이(가) 체력을 {amount}만큼 회복했습니다. 현재 체력: {self.HP}")


# Game 클래스를 사용하여 객체 생성
character1 = Game("전사", 10, 100, 50)
character2 = Game("마법사", 8, 60, 100)

# 각 객체가 사용할 수 있는 메소드 실행
character1.display_info()
character1.attack("오크")
character1.cast_spell("불꽃 공격")
character1.heal(20)

print("\n")

character2.display_info()
character2.attack("고블린")
character2.cast_spell("얼음 화살")
character2.heal(30)