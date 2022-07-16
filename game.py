import random

def dice():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    if a > b:
        return "패배", 0xFF0000, str(a), str(b)
    elif a == b:
        return "무승부", 0xFAFA00, str(a), str(b)
    elif a < b:
        return "승리", 0x00ff56, str(a), str(b)
        def coin():
    coin_face = random.randrange(0,2)
    if coin_face == 0:
        return "홀"
    elif coin_face == 1:
        return "짝"