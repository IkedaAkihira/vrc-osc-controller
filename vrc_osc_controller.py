from pynput.mouse import Button, Listener
from pythonosc import udp_client

ip = '192.168.0.10'
port = 9000
left_click_parameter_name = 'left_click'
right_click_parameter_name = 'right_click'
middle_click_parameter_name = 'middle_click'
scroll_parameter_name = 'attack_type'
scroll_parameter_count = 2

client = udp_client.SimpleUDPClient(ip, port)

def on_click(x, y, button, pressed):
    print(f'Click: {button}, {pressed}')
    if button == Button.left:
        click_parameter_name = left_click_parameter_name
    elif button == Button.right:
        click_parameter_name = right_click_parameter_name
    else:
        click_parameter_name = middle_click_parameter_name

    client.send_message(f'/avatar/parameters/{click_parameter_name}', pressed)

scroll_num = 0

def on_scroll(x, y, dx, dy):
    print('Scroll')
    global scroll_num
    scroll_num += dy
    scroll_num %= scroll_parameter_count
    client.send_message(f'/avatar/parameters/{scroll_parameter_name}', scroll_num)

with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
