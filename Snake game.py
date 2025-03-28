from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 1000
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,
                                             y,
                                             x + SPACE_SIZE,
                                             y + SPACE_SIZE,
                                             fill=SNAKE_COLOR,
                                             tag = 'snake')
            self.squares.append(square)

class Food:
    def __init__(self):
        self.new_food()

    def new_food(self):
        self.position = (random.randint(0, (GAME_WIDTH // SPACE_SIZE - 1)) * SPACE_SIZE,
                         random.randint(0, (GAME_HEIGHT // SPACE_SIZE - 1)) * SPACE_SIZE)
        canvas.create_oval(self.position[0], self.position[1],
                           self.position[0] + SPACE_SIZE, self.position[1] + SPACE_SIZE,
                           fill=FOOD_COLOR, tag='food')



def next_turn(snake,food):
    x,y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x,y) )

    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.position[0] and y == food.position[1]:

        global score

        score += 1

        label.config(text='Score: {}'.format(score))

        canvas.delete('food')

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    
    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED,next_turn,snake,food)




def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
    


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print('GAME OVER!')
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER!")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True



def game_over():


    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                        canvas.winfo_height()/2,
                        font = ('consolas',70),
                        text = 'GAME OVER!',
                        fill = 'red',
                        tag = 'Game Over')




window = Tk()

def toggle_fullscreen(event=None):
    fullscreen_state = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not fullscreen_state)

window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', toggle_fullscreen)

window.title('Snake Game')
window.attributes('-fullscreen', True)
window.resizable(True, True)



score = 0 
direction = 'down'

label = Label(window,text="Score:{}".format(score), font= ('consolas', 40))
label.pack()

canvas = Canvas(window, bg= BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()  
screen_height = window.winfo_screenheight()  

x = int(((screen_width / 2) - (window_width / 2)))
y = int(((screen_height / 2) - (window_height / 2)))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<w>', lambda event: change_direction('up'))
window.bind('<a>', lambda event: change_direction('left'))
window.bind('<s>', lambda event: change_direction('down'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Right>', lambda event: change_direction('right'))

snake = Snake()
food = Food()

next_turn(snake,food)

window.mainloop()