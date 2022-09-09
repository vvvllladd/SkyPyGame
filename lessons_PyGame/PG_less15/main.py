import pygame

pygame.init()


class GameObject:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = RED
        self.size = 20
        self.speed = 5
        self.has_image = False
        self.image = None

    def draw(self):
        if not self.has_image:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))
        else:
            self.screen.blit(self.image, (self.x, self.y))

    def add_image(self, path_to_image):
        my_image = pygame.image.load(path_to_image)
        self.image = pygame.transform.scale(my_image, (self.size, self.size))
        self.has_image = True

    def rotate_image(self, degree):
        self.image = pygame.transform.rotate(self.image, degree)



class Enemy(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = RED
        self.pattern_x = 1
        self.start_x = x

    def move(self):
        self.x -= self.speed * self.pattern_x
        if self.x <= self.start_x - 40:
            self.pattern_x = -1
        if self.x >= self.start_x + 60:
            self.pattern_x = 1
            self.y += self.speed


class Hero(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.color = GREEN
        self.size = 50

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def shoot(self, projectiles):
        projectile = Projectile(self.x + self.size//2, self.y - self.size / 2 + 30, screen)
        projectile.add_image('images\\projectile.png')
        projectile.rotate_image(-130)
        projectiles.append(projectile)


class Projectile(GameObject):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.size = 5
        self.color = BLUE

    def move(self):
        self.y -= self.speed

    def check_collision(self, enemy_list):
        for enemy in enemy_list:
            if enemy.y - enemy.size / 2 <= self.y <= enemy.y + enemy.size / 2:
                if enemy.x - enemy.size / 2 <= self.x <= enemy.x + enemy.size / 2:
                    enemy_list.remove(enemy)


WIDTH = 720
HEIGHT = 480

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 30
clock = pygame.time.Clock()

is_game_active = True

enemies = list()
projectiles = list()

for i in range(16):  # Количество противников в одном ряду
    for j in range(6):  # Количество рядов противников
        enemy = Enemy(40 + i * 40, 40 + j * 40, screen)
        enemy.add_image('images\\enemy.png')
        enemies.append(enemy)

hero = Hero(WIDTH / 2, HEIGHT - 50, screen)
hero.add_image('images\\hero.png')

is_left = False
is_right = False
is_shoot = False

background_image = pygame.image.load('images\\background.png')
scale_background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

while is_game_active:
    screen.fill(BLACK)
    screen.blit(scale_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                is_left = True
            if event.key == pygame.K_d:
                is_right = True
            if event.key == pygame.K_SPACE:
                is_shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                is_left = False
            if event.key == pygame.K_d:
                is_right = False
            if event.key == pygame.K_SPACE:
                is_shoot = False

    if is_left:
        hero.move_left()
    if is_right:
        hero.move_right()
    if is_shoot:
        hero.shoot(projectiles)

    for enemy in enemies:
        enemy.move()
        enemy.draw()

    hero.draw()

    for projectile in projectiles:
        projectile.move()
        projectile.check_collision(enemies)
        projectile.draw()

    pygame.display.update()
    clock.tick(FPS)