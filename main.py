from pynput import keyboard

def on_press(key):
    try:
        print(f'Tecla pressionada: {key.char}')
    except AttributeError:
        print(f'Tecla especial pressionada: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Para o listener ao pressionar Esc
        return False

print("Pressione teclas em qualquer lugar para exibi-las. Pressione Esc para sair.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()