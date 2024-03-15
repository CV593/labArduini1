import serial
from serial.tools.list_ports import comports
from tkinter import Tk, Canvas
from time import sleep
estado_leds = [0, 0, 0, 0]
def setup_serial():
    global puerto
    puerto = serial.Serial(comports()[0].device, 9600)
    sleep(2) 
def draw():
    canvas.delete("all")
    color = ["#e62e1b","#FFEA00","#00d221","#e62e1b"]
    apagados = ["#6a3739","#e5e619","#88a86e","#6a3739"]
    for i, estado in enumerate(estado_leds):
        x = 50 + i * 150
        fill_color = color[i] if estado_leds[i] == 1 else apagados[i]
        if i == 0:
            tag = "led1"
        elif i == 1:
            tag = "led2"
        elif i == 2:
            tag = "led3"
        else:
            tag = "led4"
        canvas.create_oval(x, 100, x + 100, 200, fill=fill_color, tags=(tag))
def toggle_led(pin):
    estado_leds[pin] = 1 - estado_leds[pin] 
    puerto.write(f"{pin},{estado_leds[pin]}\n".encode())
    draw()  
def toggle_led_1(event):
    toggle_led(0)
def toggle_led_2(event):
    toggle_led(1)
def toggle_led_3(event):
    toggle_led(2)
def toggle_led_4(event):
    toggle_led(3)
root = Tk()
width = 800 
height = 500
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()
setup_serial()
draw()
canvas.create_oval(50, 100, 150, 200, fill="#6a3739", tags=("led1",))
canvas.tag_bind("led1", "<Button-1>", toggle_led_1)
canvas.create_oval(200, 100, 300, 200, fill="#e5e619", tags=("led2",))
canvas.tag_bind("led2", "<Button-1>", toggle_led_2)
canvas.create_oval(350, 100, 450, 200, fill="#88a86e", tags=("led3",))
canvas.tag_bind("led3", "<Button-1>", toggle_led_3)
canvas.create_oval(500, 100, 600, 200, fill="#6a3739", tags=("led4",))
canvas.tag_bind("led4", "<Button-1>", toggle_led_4)
root.mainloop()

