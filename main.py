import pygame

scale = 3

width, height = 128 * scale, 64 * scale

screen = pygame.display.set_mode((width, height))
pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)

# screen.fill(white)
running = True

font = pygame.font.Font('metropolis.regular.ttf', 15 * scale)

# pygame.display.flip()

### Define PyGame Buttons ### 

UP = pygame.K_UP
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
A = pygame.K_a
B = pygame.K_s

class Display:
    def setSelected(self, row):
        pass

    def writeLine(self, text):
        pass

class Menus:
    def __init__(self):
        self.menus = [
            {'name': 'Now Playing', 'function': menu_function},
            {'name': 'Browse', 'function': menu_function},
            {'name': 'Queue', 'function': menu_function},
            {'name': 'Search', 'function': menu_function},
            {'name': 'Bluetooth', 'function': menu_function}
        ]

        self.selected = 0

        self.display = Display()

    def addItem(self, item):
        pass

    def writeToScreen(self):
        pass

    


def menu_function():
    pass


def writeLine(position, text, inverted):
    if position < 0 or position > 2:
        raise "Not a valid text position"

    x = 5 * scale
    y = (height / 3) * position + (5 * scale)

    if inverted == False:
        img = font.render(text, True, black)
    else:
        img = font.render(text, True, white)
        img.fill(black)
        
    screen.blit(img, (x,y))


def getMenuLines(index):
    output = []
    for i in range(index, index + 3):
        if i == selected:
            flag = True
        else:
            flag = False
        output.append({'text': menus[i]['name'], 'selected': flag})

    return output

def displayMenu(index):
    i = 0
    for line in getMenuLines(index):
        writeLine(i, line['text'], line['selected'])
        i += 1

    return

new_to_display = True

index = 0
selected = 0

while running:
    if new_to_display is True:
        screen.fill(white)
        displayMenu(index)
        pygame.display.update()
        pygame.display.flip()

        new_to_display = False


    for event in pygame.event.get():
        print(selected)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == UP:
                if index != 0:
                    index -= 1
                    new_to_display = True

            elif event.key == DOWN:
                if index < len(menus):
                    index += 1
                    new_to_display = True


