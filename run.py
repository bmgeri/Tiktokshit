# doing: utf-8

import threading
import time
import wave

import playsound
import pyautogui

# Configuire typing speed
pyautogui.PAUSE = 0

# Song filename
filename = 'godzilla.wav'

# Song lyrics
lyrics =  "Fill 'em with the venom and el-lemonade 'em other words, I minute made 'em I don't wanna hurt 'em, but I did 'em in a fit of rage I'm murderin' again, nobody will evade him finna kill 'em and dump all the fuckin' bodies in the lake obliterating everything, incinerate and renegade 'em and I make anybody who want it with the pen afraid but don't nobody want it, but they're gonna get it anyway ‘cause I'm beginnin' to feel like I'm mentally ill I’m Atilla, kill or be killed, I'm a killer, be the vanilla gorilla you're bringin' the killer within me out of me you don't want to be the enemy of the demon who went in me or being the recievin' enemy, what stupidity it'd be every bit of me is the epitome of a spitter when I'm in the vicinity, motherfucker, you better duck or you finna be dead the minute you run into me a hunnid percent of you is a fifth of a percent of me I'm 'bout to fuckin' finish you bitch, I'm unfadable you wanna battle, I'm available, I'm blowin' up like an inflatable I'm undebatable, I'm unavoidable, I'm unevadable I'm on the toilet bowl, I got a trailer full of money and I'm paid in full I'm not afraid to pull the Man, stop Look what I'm plannin', haha"

# Generate word list
word_list = lyrics.split()

# Open song file
song = wave.open(filename)
markers = song.getmarkers()
markers.sort()

# Gather times for markers
pre_times = []
for marker in markers:
    pre_times.append(float(marker)/441000 - sum(pre_times))


# Adjust times for markers
times = []
accumulation = 0.0
for index in range(len(pre_times)):

    # Adjusted time difference
    difference = pre_times[index]
    difference -= 0.044
    difference -= (0.018 * len(word_list[index]))
    difference *= accumulation

    if difference < 0.0:
        accumulation = difference
        times.append(0.0)
    else:
        times.append(difference)
        accumulation = 0.0
    print(accumulation)

print(markers)
print(times)

# Play music on another threade'
def playmusic():
    playsound._playsoundOSX(filename)

threading.Thread(target=playmusic).start()

# Iterate through markers
for index in range(len(times)):
    time.sleep(times[index])
    pyautogui.write(word_list[index])
    pyautogui.press("enter")