from pynput.mouse import Button, Listener
from pythonosc import udp_client

ip = input('IPアドレスを入力してください: ')
port = 9000
left_click_parameter_name = 'left_click'
right_click_parameter_name = 'right_click'
middle_click_parameter_name = 'middle_click'

client = udp_client.SimpleUDPClient(ip, port)

def on_click(x, y, button, pressed):
    if button == Button.left:
        click_parameter_name = left_click_parameter_name
    elif button == Button.right:
        click_parameter_name = right_click_parameter_name
    else:
        click_parameter_name = middle_click_parameter_name

    client.send_message(f'/avatar/parameters/{click_parameter_name}', pressed)

with Listener(on_click=on_click) as listener:
    listener.join()
