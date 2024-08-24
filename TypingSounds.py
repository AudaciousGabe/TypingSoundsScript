from pynput import keyboard
import pygame
import os
from tkinter import messagebox


# This script is designed to be either standalone or connected with AA (Audacious App)
# If you want it to connect, turn audacious_app_mode from False to True
# If you do, this script won't play audio, instead it'll create a blank txt file for AA to see if it exists
# When AA sees the blank.txt files existance, it'll play the sound and delete it, so it'll wait for the new txt file to be created
# Doing it like this will allow AA to not access specific keys that you pressed, preventing potential keylogging risks
# AA provides better audio quality, convenience of switching sounds, convenience of auto starting/closing, and more


audacious_app_mode : bool = True


# Change this number to change the volume of the audio, if not using audacious app mode. 0 - 100
volume_percentage : int = 15


# If you are using audacious app mode, replace the path provided in AA here ( Different paths on different OSs' )
audacious_app_text_path : str = "C:/Users/Gabriel/AppData/Roaming/Godot/app_userdata/AudaciousApp/PythonScripts/TextFiles"


# If you are "not" using audacious mode, change this to be the path of your audio file!
# Make sure you include the extension of the audio file in the path, like .mp3, .wav, or .ogg
standalone_sound_path : str = "C:/Users/Gabriel/AppData/Roaming/Godot/app_userdata/" \
	"AudaciousApp/SoundEffects/TypingSounds/CurrentSound.wav"


# This is a list of characters that will play sounds, if you want to ignore some keys, add # to the beginning of it!
characters_keys : list = [
	'a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'0',
'!',
'@',
'#',
'$',
'%',
'^',
'&',
'*',
'(',
')',
'-',
'=',
'[',
']',
'\\',
';',
"'",
',',
'.',
'/',
'`',
'~'
]

# This is a list of special keys that will play sounds, if you want some keys ignored, add # to the beginning of it!
special_keys : list = [
keyboard.Key.space,
keyboard.Key.enter,
keyboard.Key.tab,
keyboard.Key.backspace,
# keyboard.Key.shift,
# keyboard.Key.shift_r,
# keyboard.Key.ctrl_l,
# keyboard.Key.ctrl_r,
# keyboard.Key.alt_l,
# keyboard.Key.alt_r,
keyboard.Key.esc,
keyboard.Key.caps_lock,
keyboard.Key.num_lock,
keyboard.Key.scroll_lock,
keyboard.Key.home,
keyboard.Key.end,
keyboard.Key.page_up,
keyboard.Key.page_down,
keyboard.Key.insert,
keyboard.Key.delete,
keyboard.Key.print_screen,
keyboard.Key.pause,
keyboard.Key.up,
keyboard.Key.down,
keyboard.Key.left,
keyboard.Key.right,
keyboard.Key.f1,
keyboard.Key.f2,
keyboard.Key.f3,
keyboard.Key.f4,
keyboard.Key.f5,
keyboard.Key.f6,
keyboard.Key.f7,
keyboard.Key.f8,
keyboard.Key.f9,
keyboard.Key.f10,
keyboard.Key.f11,
keyboard.Key.f12,
keyboard.Key.menu,
keyboard.Key.media_play_pause,
keyboard.Key.media_next,
keyboard.Key.media_previous,
keyboard.Key.media_volume_mute,
# keyboard.Key.media_volume_up,
# keyboard.Key.media_volume_down

]

# This is the hotkey used to close the script manually, change the keys if you want!
exit_hotkey_combination : str = '<ctrl>+<alt>+\\'

def hotkey_pressed() -> None:
    print("HotKey Pressed! // Exitting TypingSounds Script" )
    os._exit(0)

# This is a list of compatible audio file extensions
compatible_audio_extensions: list = [".mp3", ".ogg", ".wav"]

# If using standalone_mode, it'll check to see if the audio file exists via the path
if not audacious_app_mode:
    if not os.path.exists(standalone_sound_path):
        messagebox.showinfo("No Sound Found", "Exiting TypingSounds Script")
        os._exit(1)

# Loads the audio via pygame if standalone_mode
if not audacious_app_mode:
    pygame.mixer.init()
    pygame.mixer.music.load(standalone_sound_path)
    pygame.mixer.music.set_volume(volume_percentage * 0.01) 



# Key Pressed Handler
def on_pressed(key: keyboard.Key) -> None:
    if isinstance(key, keyboard.KeyCode):
        if key.char.isalpha() and key.char.lower() in characters_keys:
            play_sound()
        elif not key.char.isalpha() and key.char in characters_keys:
            play_sound()

    elif isinstance(key, keyboard.Key) and key in special_keys:
        play_sound()



# Plays the sound based on the mode enabled
def play_sound() -> None:
    if audacious_app_mode:
        open(os.path.join(audacious_app_text_path, "KeyPressed.txt"), "w").close()
    else:
        pygame.mixer.music.play()


hotkey = keyboard.HotKey(
    keyboard.HotKey.parse(exit_hotkey_combination),
    hotkey_pressed
)

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as listener:
    
    with keyboard.Listener(
            on_press=on_pressed,
            on_release=None) as key_listener:
        
        listener.join()
        key_listener.join()