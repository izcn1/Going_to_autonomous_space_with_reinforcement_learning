import turtle
import random
import time
# Çevre (environment) oluşturma
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("white")

# Kareyi oluşturma
square = turtle.Turtle()
square.shape("square")
square.color("blue")
square.penup()
square.speed(0)
square.goto(-250, -250)  # Kare başlangıç pozisyonu

# Daireyi oluşturma
circle = turtle.Turtle()
circle.shape("circle")
circle.color("red")
circle.penup()
circle.speed(0)
circle.goto(25,0)  # Daire başlangıç pozisyonu (Daireyi daha merkezi bir konuma taşıdık)

# Başlangıçta ödülü sıfırla
reward = 0

# Q-learning parametreleri
learning_rate = 0.1
discount_factor = 0.9

# Durumları hesaplamak için yardımcı bir fonksiyon
def get_state():
    x, y = square.pos()
    if x < 0:
        x = -1
    else:
        x = 1
    if y < 0:
        y = -1
    else:
        y = 1
    return x, y

# Q-learning algoritması
def q_learning():
    global reward
    state = get_state()
    while state != (1, 1):  # Daire içine girilene kadar devam et
        if random.random() < 0.1:
            action = random.choice(["up", "down", "left", "right"])  # Keşif
        else:
            if state == (-1, -1):
                action = random.choice(["up", "right"])  # Exploitation
            elif state == (-1, 1):
                action = random.choice(["down", "right"])  # Exploitation
            elif state == (1, -1):
                action = random.choice(["up", "left"])  # Exploitation
            else:
                action = random.choice(["down", "left"])  # Exploitation

        if action == "up":
            square.setheading(90)  # Yukarı git
            square.forward(25)  # Kareyi daha küçük adımlarla hareket ettir
        elif action == "down":
            square.setheading(270)  # Aşağı git
            square.forward(25)
        elif action == "left":
            square.setheading(180)  # Sola git
            square.forward(25)
        elif action == "right":
            square.setheading(0)  # Sağa git
            square.forward(25)

        new_state = get_state()

        # Daire içine girildiyse büyük bir ödül
        if new_state == (1, 1):
            reward = 100

        # Q-değerleri güncelleme
        Q[state][action] = Q[state][action] + learning_rate * (reward + discount_factor * max(Q[new_state].values()) - Q[state][action])

        state = new_state

# Q-table'ı başlangıçta sıfırla
Q = {(-1, -1): {"up": 0, "down": 0, "left": 0, "right": 0},
     (-1, 1): {"up": 0, "down": 0, "left": 0, "right": 0},
     (1, -1): {"up": 0, "down": 0, "left": 0, "right": 0},
     (1, 1): {"up": 0, "down": 0, "left": 0, "right": 0}}

# Q-learning'i çalıştır
for episode in range(1000):
    square.goto(-250, -250)  # Kareyi başlangıç pozisyonuna geri getir
    reward = 0  # Ödülü sıfırla
    q_learning()
    time.sleep(1)
    

# Son durumda kareyi görüntüle
wn.mainloop()
