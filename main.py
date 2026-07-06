import pygame
import random
import colorsys
import math
from pathlib import Path


gravity = 0.01
impulse = 0.8
clock = pygame.time.Clock()

running = True

pygame.init()

screen = pygame.display.set_mode((1920,1080))

images = []


players = [

]
spawn = [940, 1040, 840, 740, 1140, 1240, 640, 540, 1340]

def randomspawn():
    player["x"] = random.choice(spawn)
    player["y"] = 0
    player["x_velocity"] = 0
    player["y_velocity"] = 0

print(players)
hue = 0.0
pygame.mixer.init()
hit = pygame.mixer.Sound('bat_hit.mp3')
hit.set_volume(0.05)
font = pygame.font.Font(None, 34)

loaded_players = set()

hitmarker = pygame.mixer.Sound("hitmarker_2.mp3")
fart = pygame.mixer.Sound("perfect-fart.mp3")
chaching3x = pygame.mixer.Sound("audiojoiner120623175716.mp3")
chaching = pygame.mixer.Sound("cha_ching_register-muska666-173262285.mp3")
ijusthit = pygame.mixer.Sound("i-just-hit-the-jackpot-meme.mp3")

hitmarker.set_volume(0.5)
fart.set_volume(0.5)
ijusthit.set_volume(0.5)
chaching3x.set_volume(0.5)
chaching.set_volume(0.5)
def check_for_new_players():
    for image_path in Path("DiscordImages").glob("*.png"):

        if image_path.name in loaded_players:
            continue

        try:
            image = pygame.image.load(str(image_path)).convert_alpha()
        except (FileNotFoundError, pygame.error):
            # File isn't ready yet
            continue

        loaded_players.add(image_path.name)

        image = pygame.transform.smoothscale(image, (50, 50))

        players.append({
            "name": image_path.stem,
            "image": image,
            "x": random.choice(spawn),
            "y": 0,
            "x_velocity": 0,
            "y_velocity": 0,
            "points": 1.0 ,
            "on_half_platform": False
        })


def round_up_decimals(number, decimals=0):
    pointsmultiplier = 10 ** decimals
    return math.ceil(number * pointsmultiplier) / pointsmultiplier

while running:
    screen.fill((0, 0, 0))
    check_for_new_players()
    platform_data = [
        (960, 200), (960, 300), (960, 400),
        (960, 500), (960, 600), (960, 700),
        (960, 800),

        (1060, 250), (1060, 350), (1060, 450),
        (1060, 550), (1060, 650), (1060, 750),
        (1060, 850),

        (860, 250), (860, 350), (860, 450),
        (860, 550), (860, 650), (860, 750),
        (860, 850),

        (760, 200), (760, 300), (760, 400),
        (760, 500), (760, 600), (760, 700),
        (760, 800),

        (1160, 200), (1160, 300), (1160, 400),
        (1160, 500), (1160, 600), (1160, 700),
        (1160, 800),

        (1260, 250), (1260, 350), (1260, 450),
        (1260, 550), (1260, 650), (1260, 750),
        (1260, 850),

        (660, 250), (660, 350), (660, 450),
        (660, 550), (660, 650), (660, 750),
        (660, 850),

        (560, 200), (560, 300), (560, 400),
        (560, 500), (560, 600), (560, 700),
        (560, 800),

        (1360, 200), (1360, 300), (1360, 400),
        (1360, 500), (1360, 600), (1360, 700),
        (1360, 800),

    ]


    platforms = [pygame.Rect(x, y, 20, 20) for x, y in platform_data]
    platforms.extend([
        pygame.Rect(510, 0, 20, 1980),
        pygame.Rect(1410, 0, 20, 1980),
        pygame.Rect(1015, 950, 10, 130),
        pygame.Rect(915, 950, 10, 130),
        pygame.Rect(815, 950, 10, 130),
        pygame.Rect(715, 950, 10, 130),
        pygame.Rect(615, 950, 10, 130),
        pygame.Rect(1115, 950, 10, 130),
        pygame.Rect(1215, 950, 10, 130),
        pygame.Rect(1315, 950, 10, 130),
        pygame.Rect(1415, 950, 10, 130),

    ])

    for player in players:
        hitbox = pygame.Rect(
            player["x"],
            player["y"],
            player["image"].get_width(),
            player["image"].get_height()
        )

        # Horizontal movement
        player["x"] += player["x_velocity"]
        hitbox.x = player["x"]


        for platform in platforms:
            if hitbox.colliderect(platform):
                pygame.mixer.Sound.play(hit)
                if player["x_velocity"] > 0:
                    player["x"] = platform.left - hitbox.width

                elif player["x_velocity"] < 0:
                    player["x"] = platform.right

                player["x_velocity"] *= -1
                hitbox.x = player["x"]

        player["y_velocity"] += gravity
        player["y"] += player["y_velocity"]
        hitbox.y = player["y"]
        for platform in platforms:
            if hitbox.colliderect(platform):
                pygame.mixer.Sound.play(hit)
                if player["y_velocity"] > 0:
                    player["y"] = platform.top - hitbox.height
                    player["y_velocity"] *= -0.6
                    player["x_velocity"] = random.uniform(-2, 2)

                elif player["y_velocity"] < 0:
                    player["y"] = platform.bottom
                    player["y_velocity"] = 0

                hitbox.y = player["y"]

        multiplier_platforms = [
            (pygame.Rect(920, 1040, 100, 20), 0.2 , fart),
            (pygame.Rect(1020, 1040, 100, 20), 0.5, hitmarker),
            (pygame.Rect(820, 1040, 100, 20), 0.5, hitmarker),
            (pygame.Rect(1120, 1040, 100, 20), 1.2, chaching3x),
            (pygame.Rect(720, 1040, 100, 20), 1.2, chaching3x),
            (pygame.Rect(1220, 1040, 100, 20), 2.8, chaching),
            (pygame.Rect(620, 1040, 100, 20), 2.8, chaching),
            (pygame.Rect(1320, 1040, 100, 20), 6, ijusthit),
            (pygame.Rect(520, 1040, 100, 20), 6, ijusthit),
        ]

        touching_multiplier = False

        for rect, multiplier, sound in multiplier_platforms:
            if hitbox.colliderect(rect):
                touching_multiplier = True
                if not player["on_half_platform"]:
                    player["points"] *= multiplier
                    player["points"] = round_up_decimals(player["points"], 1)
                    pygame.mixer.Sound.play(sound)
                    player["on_half_platform"] = True

                break

        if not touching_multiplier:
            player["on_half_platform"] = False

        if player["y"] > 1080:
            randomspawn()
        screen.blit(player["image"], (player["x"], player["y"]))

    sorted_players = sorted(players, key=lambda p: p["points"], reverse=True)

    y_offset = 10

    for player in sorted_players:
        screen.blit(player["image"], (1460, y_offset))

        text = font.render(
            f'{player["name"]}: {player["points"]}',
            True,
            (255, 255, 255)
        )

        screen.blit(text, (1520, y_offset + 10))

        y_offset += 60



    for i in range(len(platforms)): pygame.draw.rect(screen, (255, 255, 255), platforms[i])

    hue += 0.003
    if hue > 1:
        hue = 0

    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

    text_color = (int(r * 255), int(g * 255), int(b * 255))


    gamblefont = pygame.font.Font(None, 40)
    text05x = gamblefont.render("0.2x", True, (255,255,0))
    text15x = gamblefont.render("0.5x", True, (255, 0, 0))
    text3x = gamblefont.render("1.2x", True, (0, 255, 0))
    text5x = gamblefont.render("2.8x", True, (0, 0, 255))
    text10x = gamblefont.render("6x", True, text_color)

    screen.blit(text05x, ( (screen.get_width() // 2)- 15 , 980))
    screen.blit(text15x, ((screen.get_width() // 2) - 110, 980))
    screen.blit(text15x, ((screen.get_width() // 2) + 90, 980))
    screen.blit(text3x, ((screen.get_width() // 2) + 190, 980))
    screen.blit(text3x, ((screen.get_width() // 2) - 210, 980))
    screen.blit(text5x, ((screen.get_width() // 2) + 290, 980))
    screen.blit(text5x, ((screen.get_width() // 2) - 310, 980))
    screen.blit(text10x, ((screen.get_width() // 2) + 390, 980))
    screen.blit(text10x, ((screen.get_width() // 2) - 410, 980))

    explaintext = font.render("type !join in VC chat to join", True, (255,255,255))
    screen.blit(explaintext, (100, 180))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.WINDOWFOCUSLOST:
            print("Lost focus")

        elif event.type == pygame.WINDOWFOCUSGAINED:
            print("Focused again")
    clock.tick(165)
pygame.quit()

