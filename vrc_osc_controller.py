from pynput.mouse import Button, Listener
from pythonosc import udp_client

ip = '192.168.0.10'
port = 9000
click_parameter_name = 'beam'
scroll_parameter_name = 'GestureLeft'
scroll_parameter_count = 8

client = udp_client.SimpleUDPClient(ip, port)

def on_click(x, y, button, pressed):
    if pressed:
        client.send_message(f'/avatar/parameters/{click_parameter_name}', 1)
    else:
        client.send_message(f'/avatar/parameters/{click_parameter_name}', 0)

scroll_num = 0

def on_scroll(x, y, dx, dy):
    global scroll_num
    scroll_num += dy
    scroll_num %= scroll_parameter_count
    client.send_message(f'/avatar/parameters/{scroll_parameter_name}', scroll_num)

with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
