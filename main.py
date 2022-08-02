#https://www.youtube.com/watch?v=hDu8mcAlY4E
#pygame tut

#Function Imports
import pygame, sys, random,time
#COLOUR WHITE
WHITE = (255, 255, 255)

#Mies Class
class Mies(pygame.sprite.Sprite):
  def __init__(self,picture_path, pos_x, pos_y):
    super().__init__()
    self.image = pygame.image.load(picture_path)
    self.rect = self.image.get_rect()
    self.rect.center = [pos_x,pos_y]

#Zombie Class
class Zombie(pygame.sprite.Sprite):
  def __init__(self,picture_path,pos_x,pos_y,zombieSpeed):
    super().__init__()
    self.image = pygame.image.load(picture_path)
    self.rect = self.image.get_rect()
    self.rect.center = [pos_x,pos_y]

#Bullet Class
class Bullet(pygame.sprite.Sprite):
  def __init__(self,picture_path, pos_x, pos_y):
    super().__init__()
    self.image = pygame.image.load(picture_path)
    self.rect = self.image.get_rect()
    self.rect.center = [pos_x, pos_y]


#Wall Class
class Wall(pygame.sprite.Sprite):
  def __init__(self,picture_path,pos_x,pos_y):
    super().__init__()
    self.image = pygame.image.load(picture_path)
    self.rect = self.image.get_rect()
    self.rect.center = [pos_x,pos_y]

#Healthbar Class
class Health(pygame.sprite.Sprite):
    def __init__(self,picture_path, pos_x, pos_y):
      super().__init__()
      self.image = pygame.image.load(picture_path)
      self.rect = self.image.get_rect()
      self.rect.center = [pos_x,pos_y]

#Background class
class Background(pygame.sprite.Sprite):
    def __init__(self,picture_path,):
      super().__init__()
      self.image = pygame.image.load(picture_path)
      self.rect = self.image.get_rect()

#death function
def death(): 
  print("---GAME OVER---")
  print("FINAL SCORE:" + str(score))
  font = pygame.font.Font('freesansbold.ttf', 24)
  text2 = font.render(f"""GAME OVER            SCORE: {score}""", True, WHITE)
  text2Rect = text2.get_rect()
  text2Rect.center = (512,256)
  screen.blit(text2, text2Rect)
  pygame.display.flip()
  time.sleep(15)
  pygame.quit()

# General Setup
pygame.init()
clock = pygame.time.Clock()
timer = 0

#game screen
screen_height = 512
screen_width = 1024
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.mouse.set_visible(False)



#Mies Group Initialization
mies = Mies("Human Mies Left.png", 450, 250)
mies_group = pygame.sprite.Group()
mies_group.add(mies)
mies_speed=[0,0]
prev_key = "l"

#Zombie group initialization
zombies = []
zombieSpeed = [1,0]
zombie_group = pygame.sprite.Group()
zombiePerTimer = 2

#bullet group initialization
bullet = Bullet("Bullet Right.png",-6000,-6000)
bullet_group = pygame.sprite.Group()
bullet_group.add(bullet) 
bulletDirection = [0,0]

#Wall group initialization
wall= Wall("Fort Wall.png", 992, 256)
wall_group = pygame.sprite.Group()
wall_group.add(wall)

#health bar group initialization
healthBarImage = "Health Bar-1.png"
healthBar = Health(healthBarImage,950,32)
healthBar_group = pygame.sprite.Group()
healthBar_group.add(healthBar)
healthDown = 4  
health = 4

#background group initialization
background = Background("background.png")
background_group = pygame.sprite.Group()
background_group.add(background)

#Zombie Kill Count
score = 0

#Game Run Process
while True:
  #Mies Movement
  mies.rect = mies.rect.move(mies_speed)

  #Zombie Spawning Process
  if timer % 60 == 0:
    for zombie in range(zombiePerTimer):
      new_zombie = Zombie("Zombie Will.png",-64,random.randrange(0,screen_height),[1,0])
      zombie_group.add(new_zombie)
      zombies.append(new_zombie)

  #Zombie Movement
  for z in zombies:
    z.rect = z.rect.move(zombieSpeed)

    
  #Pygame Events
  for event in pygame.event.get():
    #System termination
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    #Key Press Functions
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN: # down key rotate player
        if prev_key == "u":
          mies.image = pygame.transform.rotate(mies.image, 180)
        elif prev_key == "l":
          mies.image = pygame.transform.rotate(mies.image, 90)
        elif prev_key == "r":
          mies.image = pygame.transform.rotate(mies.image, -90)
        prev_key = "d"
      elif event.key == pygame.K_UP: # up key rotate player
        if prev_key == "d":
          mies.image = pygame.transform.rotate(mies.image, 180)
        elif prev_key == "l":
          mies.image = pygame.transform.rotate(mies.image, -90)
        elif prev_key == "r":
          mies.image = pygame.transform.rotate(mies.image, 90)
        prev_key = "u"
      if event.key == pygame.K_RIGHT: # right key rotate player
        if prev_key == "u":
          mies.image = pygame.transform.rotate(mies.image, -90)
        elif prev_key == "d":
          mies.image = pygame.transform.rotate(mies.image, 90)
        elif prev_key == "l":
          mies.image = pygame.transform.rotate(mies.image, 180)
        prev_key = "r"
      elif event.key == pygame.K_LEFT: # left key rotate player
        if prev_key == "u":
          mies.image = pygame.transform.rotate(mies.image, 90)
        elif prev_key == "d":
          mies.image = pygame.transform.rotate(mies.image, -90)
        elif prev_key == "r":
          mies.image = pygame.transform.rotate(mies.image, 180)
        prev_key = "l"
      if event.key == pygame.K_s: # "s" down key rotate and move player
        mies_speed[1] = 4
        if prev_key == "u":
          mies.image = pygame.transform.rotate(mies.image, 180)
        elif prev_key == "l":
          mies.image = pygame.transform.rotate(mies.image, 90)
        elif prev_key == "r":
          mies.image = pygame.transform.rotate(mies.image, -90)
        prev_key = "d"
      
      elif event.key == pygame.K_w: # "w" up key rotate and move player
        mies_speed[1] = -4
        if prev_key == "d":
          mies.image = pygame.transform.rotate(mies.image, 180)
        elif prev_key == "l":
          mies.image = pygame.transform.rotate(mies.image, -90)
        elif prev_key == "r":
          mies.image = pygame.transform.rotate(mies.image, 90)
        prev_key = "u"
      if event.key == pygame.K_d: # "d" right key rotate and move player
        mies_speed[0] = 4
        if prev_key == "u":
          mies.image = pygame.transform.rotate(mies.image, -90)
        elif prev_key == "d":
          mies.image = pygame.transform.rotate(mies.image, 90)
        elif prev_key == "l":
          mies.image = pygame.transform.rotate(mies.image, 180)
        prev_key = "r"
      elif event.key == pygame.K_a: # "a" left key rotate and move player
        mies_speed[0] = -4
        if prev_key == "u":
          mies.image = pygame.transform.rotate(mies.image, 90)
        elif prev_key == "d":
          mies.image = pygame.transform.rotate(mies.image, -90)
        elif prev_key == "r":
          mies.image = pygame.transform.rotate(mies.image, 180)
        prev_key = "l"

      if event.key == pygame.K_SPACE: # Space bar shoot bullet
        if prev_key == "l":
          bulletDirection = [-100,0]
          bulletImage = "Bullet Left.png"
          newBullet = Bullet(bulletImage, mies.rect.center[0], mies.rect.center[1])
          bullet_group.add(newBullet)
        elif prev_key == "r":
          bulletDirection = [100,0]
          bulletImage = "Bullet Right.png"
          newBullet = Bullet(bulletImage, mies.rect.center[0], mies.rect.center[1])
          bullet_group.add(newBullet)
        elif prev_key == "u":
          bulletDirection = [0,-100]
          bulletImage = "Bullet Up.png"
          newBullet = Bullet(bulletImage, mies.rect.center[0], mies.rect.center[1])
          bullet_group.add(newBullet)
        elif prev_key == "d":
          bulletDirection = [0,100]
          bulletImage = "Bullet Down.png"
          newBullet = Bullet(bulletImage, mies.rect.center[0], mies.rect.center[1])
          bullet_group.add(newBullet)
    #Key up functions
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_s: # "s" down key
        mies_speed[1] = 0
      elif event.key == pygame.K_w: # "w" up key
        mies_speed[1] = 0
      if event.key == pygame.K_d: # "d" right key
        mies_speed[0] = 0
      elif event.key == pygame.K_a: # "a" left key
        mies_speed[0] = 0

  #Timer for controlling spawn rates
  timer += 1
  if timer > 1500:
    zombiePerTimer = int(timer//750)
  if timer > 200: 
    zombieSpeed[0] = timer//200

  #collisions system
  for z in zombies:
    if z.rect.colliderect(wall.rect):
      health-=1
      zombie_group.remove(z)
      zombies.remove(z)
    if mies.rect.colliderect(z.rect):
      death()
    for b in bullet_group:
      if z.rect.colliderect(b.rect):
        bullet_group.remove(b)
        zombie_group.remove(z)
        zombies.remove(z)
        time.sleep(0.1)
        score += 1
        
  #bullet despawning 
  for b in bullet_group:
    b.rect = b.rect.move(bulletDirection)
    if b.rect.center[0] < 0:
      bullet_group.remove(b)
    elif b.rect.center[0] > 1024:
      bullet_group.remove(b)
    elif b.rect.center[1] < 0:
      bullet_group.remove(b)
    elif b.rect.center[1] > 512:
      bullet_group.remove(b)

  #player collision against wall
  if mies.rect.colliderect(wall.rect):
    mies_speed[0] = -1

  #health bar system
  if health == 4 and healthDown == 4:
    healthBarImage = "Health Bar-1.png"
    healthBar = Health(healthBarImage,950,32)
    healthBar_group = pygame.sprite.Group()
    healthBar_group.add(healthBar)
    healthDown = 3
  if health == 3 and healthDown == 3:
    healthBarImage = "Health Bar-2.png"
    healthBar = Health(healthBarImage,950,32)
    healthBar_group = pygame.sprite.Group()
    healthBar_group.add(healthBar)
    healthDown = 2
  if health == 2 and healthDown == 2:
    healthBarImage = "Health Bar-3.png"
    healthBar = Health(healthBarImage,950,32)
    healthBar_group = pygame.sprite.Group()
    healthBar_group.add(healthBar)
    healthDown = 1
  if health == 1 and healthDown == 1:
    healthBarImage = "Health Bar-4.png"
    healthBar = Health(healthBarImage,950,32)
    healthBar_group = pygame.sprite.Group()
    healthBar_group.add(healthBar)
    healthDown = 0
  if health == 0 and healthDown == 0:
    healthBarImage = "Health Bar-5.png"
    healthBar = Health(healthBarImage,950,32)
    healthBar_group = pygame.sprite.Group()
    healthBar_group.add(healthBar)
    death()
    
   

  #Score Display
  font = pygame.font.Font('freesansbold.ttf', 24)
  text = font.render("Score: " + str(score), True, WHITE)
  textRect = text.get_rect()
  textRect.center = (64,32)
  screen.blit(text, textRect)


  #Character and image blitting
  pygame.display.flip()
  background_group.draw(screen)
  zombie_group.draw(screen)
  mies_group.draw(screen)
  wall_group.draw(screen)
  bullet_group.draw(screen)
  healthBar_group.draw(screen)
  clock.tick(60)