import network.client as cl
import utils.input as input
import utils.output as output
import pygame as pg

if __name__ == "__main__":
    client = cl.Client()
    pg.init()
    done = False
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    t = input.Textbox(100, 100, font=pg.font.Font(None, 32), window=screen,
                        enter_command=client.decode_client_key, filler_text="Enter key")
    text = output.Text(window=screen, font=pg.font.Font(None, 32))
    while not done:
        screen.fill((30, 30, 30))
        for event in pg.event.get():
            t.update(event)
            text.write(100, 450, "This is example text")
            text.write(100, 100, "second test")
            if event.type == pg.QUIT:
                done = True
                if client.running:
                    client.close_client()
            pg.display.flip()
        if not client.running and client.key_decoded():
            client.start_client()
        clock.tick(60)
    pg.quit()