import pygame as pg

FPS = 60
SCREEN_SIZE = (560, 800)


class Background(pg.sprite.Sprite):
    def __init__(
        self,
        image_path: str,
        position: tuple[int, int],
        size: tuple[int, int],
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

        if self.condition is not None:
            self.acceleration = self.condition(self.velocity, self.acceleration)

        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y -= 2 * SCREEN_SIZE[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        screen.blit(
            self.image, (self.rect.topleft[0], self.rect.topleft[1] - SCREEN_SIZE[1])
        )
        screen.blit(
            self.image, (self.rect.topleft[0], self.rect.topleft[1] + SCREEN_SIZE[1])
        )


def main():
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption("Elevador")

    background = Background(
        "src/simulation-of-movement/assets/fundo-elevador4.png",
        (0, 0),
        SCREEN_SIZE,
        acc=2,
    )
    elevator = Background(
        "src/simulation-of-movement/assets/elevador.png", (0, 0), (256, 256)
    )
    elevator.rect.center = (10 + SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

    running = True
    while running:
        dt = pg.time.Clock().tick(FPS) / 100

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        background.update(dt)
        screen.fill((255, 255, 255))
        background.draw(screen)
        elevator.draw(screen)

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
