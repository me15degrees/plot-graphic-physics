import pygame as pg

FPS = 60
SCREEN_SIZE = (700, 1000)

class Background(pg.sprite.Sprite):
    def __init__(
        self, 
        image_path: str, 
        position: tuple[int, int], 
        size: tuple[int,int],
        vel=0.0,
        acc=0.0,
        condition=None,
    ):
        super().__init__()
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(topleft=position)
        self.velocity = vel
        self.acceleration = acc
        self.screen_height = size[1]
        self.condition = condition

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.rect.y += self.velocity * dt

        if self.rect.bottom <= 0:  
            self.rect.top = self.screen_height  

        if self.condition is not None:
            self.acceleration = self.condition(self.velocity, self.acceleration)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

def main():
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption("Elevador")

    # Cria um objeto da classe Background com a imagem do fundo
    background = Background("src/simulation-of-movement/assets/fundo-elevador2.png", (0, 0), SCREEN_SIZE, acc = 2)
    background2 = Background("src/simulation-of-movement/assets/fundo-elevador2.png", (1000, 0), SCREEN_SIZE, acc = 2)
    

    running = True
    while running:
        dt = pg.time.Clock().tick(FPS) / 100  # Delta time em segundos

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        background.update(dt)
        background2.update(dt)
        screen.fill((255, 255, 255))  # Preenche a tela com branco
        background.draw(screen)
        background2.draw(screen)

        pg.display.flip()  

    pg.quit()

if __name__ == "__main__":
    main()
