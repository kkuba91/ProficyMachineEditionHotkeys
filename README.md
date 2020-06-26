# ProficyMachineEditionHotkeys
[![License: GPLv3](https://img.shields.io/badge/license-GPL-blue)](https://github.com/kkuba91/ProficyMachineEditionHotkeys/blob/master/LICENSE)
[![Language: Platform](https://img.shields.io/badge/platform-win--32%20%7C%20win--64-lightgrey)](https://github.com/kkuba91/ProficyMachineEditionHotkeys)
[![Language: Python](https://img.shields.io/badge/python-%3E%3D3.7-blue)](https://github.com/kkuba91/ProficyMachineEditionHotkeys)
[![Build: Passing](https://img.shields.io/badge/buil-passing-brightgreen)](https://github.com/kkuba91/ProficyMachineEditionHotkeys)

Some hotkeys for Proficy Machine Edition (GE-PLC IDE)

Program rus transparently (without frame/console).

## Other package used

 - pynput from here: https://github.com/moses-palmer/pynput

## Important

Proficy Machine Edition Laddes Edit works like spreadsheet. There are no hotkeys inbuild, but keywords making content inside every cell with logical sense.

Unfortunately GE Ide is working slow (interprets content into ladder signs? or what?), so if Your PG is not fast enouth hotkeys will not speed up you inplementing work.

## Isues

[1] On Windows there is a problem with buildin system hotkeys which signals python app to abort (ctrl+z, etc). 

## Usage
When Proficy Machine Edition Ladder is open, start hotkeys.exe and You could try to use hotkeys:

 - [CTRL L] + [F2]      =>  Normally Opened Contact (NOCON)
 - [CTRL_L] + [F3]      =>  Normally Closed Contact (NCCON)
 - [CTRL_L] + [ALT_L]   =>  Coil (COIL)
 - [CTRL_L] + [SHIFT_L] =>  Horisontal Wire (H_WIRE)
 - [CTRL_L] + [F9]      =>  Vertical Wire (V_WIRE)
