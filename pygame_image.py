import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")

    bard = pg.image.load("ex01/fig/3.png")
    bard = pg.transform.flip(bard, True, False)

    bardList = [pg.transform.rotate(bard, i/2) for i in range(20)] 
    bardList += [pg.transform.rotate(bard, i/2) for i in range(20, 0, -1)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return



        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])

        screen.blit(bardList[tmr%len(bardList)], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()