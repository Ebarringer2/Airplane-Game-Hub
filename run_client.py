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
    t = input.Textbox(50, 80, font=pg.font.Font(None, 32), window=screen,
                        enter_command=client.decode_client_key, filler_text="Enter key")
    text = output.Text(window=screen, font=pg.font.Font(None, 32))
    text.write(50, 50, "Room ID:", "room_id")
    mode = "enter_id"
    while not done:
        screen.fill((30, 30, 30))
        for event in pg.event.get():
            t.update(event)
            text.draw()
            if event.type == pg.QUIT:
                done = True
                if client.running:
                    client.close_client()
            pg.display.flip()
        if not client.running and client.key_decoded():
            client.start_client()
            if mode == "enter_id":
                mode = "enter_password"
        if mode == "enter_password":
            text.blit_l["room_id"][1][0] = "Enter Password:"
            t.set_enter_command(client.send_data)
        clock.tick(60)
    pg.quit()