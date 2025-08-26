import pgzrun
import random
import math
from pygame import Rect  # allowed by the rules

WIDTH = 800
HEIGHT = 480

MENU = "menu"
PLAYING = "playing"
EXIT = "exit"

game_state = MENU
sound_on = True


class Hero:
    def __init__(self, pos):
        self.x, self.y = pos
        self.vx = 0
        self.vy = 0
        self.on_ground = False
        self.direction = 1
        self.frame = 0
        self.timer = 0
        self.images_idle = ["hero_idle1", "hero_idle2"]
        self.images_run = ["hero_run1", "hero_run2"]
        self.current_image = self.images_idle[0]

    def update(self):
        # Horizontal movement
        self.vx = 0
        if keyboard.left:
            self.vx = -2
            self.direction = -1
        elif keyboard.right:
            self.vx = 2
            self.direction = 1

        # Jump
        if keyboard.space and self.on_ground:
            self.vy = -6
            self.on_ground = False
            if sound_on:
                sounds.jump.play()

        # Gravity
        self.vy += 0.3
        if self.vy > 5:
            self.vy = 5

        # Apply velocity
        self.x += self.vx
        self.y += self.vy

        # Floor / platforms (simple ground at y=400)
        if self.y >= 400:
            self.y = 400
            self.vy = 0
            self.on_ground = True

        # Keep hero within screen bounds
        self.x = max(16, min(WIDTH - 16, self.x))

        # Animation
        self.timer += 1
        if self.vx != 0:
            if self.timer % 12 == 0:
                self.frame = (self.frame + 1) % len(self.images_run)
            self.current_image = self.images_run[self.frame]
        else:
            if self.timer % 24 == 0:
                self.frame = (self.frame + 1) % len(self.images_idle)
            self.current_image = self.images_idle[self.frame]

    def draw(self):
        actor = Actor(self.current_image, (self.x, self.y))
        actor.draw()


class Enemy:
    def __init__(self, pos, move_range):
        self.x, self.y = pos
        self.start_x = self.x
        self.range = move_range
        self.speed = 1
        self.frame = 0
        self.timer = 0
        self.images_idle = ["enemy_idle1", "enemy_idle2"]
        self.images_move = ["enemy_move1", "enemy_move2"]
        self.current_image = self.images_idle[0]

    def update(self):
        # Patrol movement within territory
        self.x += self.speed
        if abs(self.x - self.start_x) > self.range:
            self.speed *= -1

        # Animation
        self.timer += 1
        if self.timer % 16 == 0:
            self.frame = (self.frame + 1) % len(self.images_move)
            self.current_image = self.images_move[self.frame]

    def draw(self):
        Actor(self.current_image, (self.x, self.y)).draw()

    def collides_with(self, hero):
        enemy_rect = Rect(self.x - 16, self.y - 16, 32, 32)
        hero_rect = Rect(hero.x - 16, hero.y - 16, 32, 32)
        return enemy_rect.colliderect(hero_rect)


# World objects
hero = Hero((100, 400))
enemies = [
    Enemy((300, 400), 60),
    Enemy((520, 400), 90),
    Enemy((700, 400), 40),
]

# Menu buttons
button_start = Actor("button_start", (WIDTH // 2, 200))
button_sound = Actor("button_sound", (WIDTH // 2, 280))
button_exit = Actor("button_exit", (WIDTH // 2, 360))


def update():
    global game_state
    if game_state == PLAYING:
        hero.update()
        for e in enemies:
            e.update()
            if e.collides_with(hero):
                if sound_on:
                    sounds.hit.play()
                reset_game()


def draw():
    screen.clear()
    if game_state == MENU:
        screen.fill((20, 20, 35))
        screen.draw.text("Platformer Game", center=(WIDTH // 2, 100),
                         fontsize=56, color="white")
        button_start.draw()
        button_sound.draw()
        button_exit.draw()
        screen.draw.text("Start", center=(button_start.x, button_start.y),
                         fontsize=24, color="black")
        screen.draw.text("Sound ON/OFF", center=(button_sound.x, button_sound.y),
                         fontsize=24, color="white")
        screen.draw.text("Exit", center=(button_exit.x, button_exit.y),
                         fontsize=24, color="white")
    elif game_state == PLAYING:
        screen.fill((100, 150, 255))
        # Ground line for reference
        screen.draw.filled_rect(Rect(0, 416, WIDTH, HEIGHT - 416), (60, 180, 80))
        hero.draw()
        for e in enemies:
            e.draw()
    elif game_state == EXIT:
        screen.fill((0, 0, 0))
        screen.draw.text("Thanks for playing!", center=(WIDTH // 2, HEIGHT // 2),
                         fontsize=56, color="yellow")


def on_mouse_down(pos):
    global game_state, sound_on
    if game_state == MENU:
        if button_start.collidepoint(pos):
            game_state = PLAYING
            if sound_on:
                sounds.click.play()
                music.play("music")
        elif button_sound.collidepoint(pos):
            sound_on = not sound_on
            if not sound_on:
                music.stop()
            else:
                music.play("music")
        elif button_exit.collidepoint(pos):
            game_state = EXIT


def reset_game():
    global hero
    hero = Hero((100, 400))


pgzrun.go()
