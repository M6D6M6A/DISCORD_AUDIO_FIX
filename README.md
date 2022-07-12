# discord_audio_fix

## discord_audio_fix - Let's automate the solving of Discord audio problems

> Author:           Philipp Reuter

> Version:          1.0.0

> Generated:        Jul 12, 2022

> Idea based on:    https://www.youtube.com/watch?v=Y9DLLxeY5vo


## Introduction

Since I use the Shure SM7B with the Focusrite Scarlett Solo, I had the problem that my voice sounded robotic. 
Therefore, as described in the video, I always had to change the process manually and for this I wrote the script 
to automatically set everything correctly with one click.

Because it is only supposed to be a small project, I programmed it with pyton 3.10 and converted it to an .exe with pyinstaller, so I can set it from the desktop as a shortcut. It is also useful to set the .exe to always run as admin because that is needed to change the priority and affinity.


## How to use

1. Run the "discord_audio_fix.py" with python3.10+ or the "discord_audio_fix.exe", from folder dist, as admin.
2. The prompt will tell you what to do:
    - "Please run as Administrator!" -> Restart as admin.
    - "audiodg.exe not running!" -> Restart discord.
    - "Changed audiodg.exe to run on Core 2 with high priority!" -> Can be another Core, but microphone should work now.
    - "audiodg.exe is already set up!" -> Should Work, if not, create a Issue.
    - "Error: ..." -> Please report Bug.


## Planned Features

- [ ] Other Solutions
