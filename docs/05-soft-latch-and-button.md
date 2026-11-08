# 05. Soft-latch power switch and button

## Idea
Q20 (P-FET) connects the battery (VBAT) to the rest of the device (VSW). The button turns it on. Once the ESP32 boots it drives HOLD high,
which keeps Q20 on, so the button can be released. When the ESP32 drives HOLD low, Q20 turns off and the device loses power.
The button-sense path (D21) is independent of the hold path (Q21).

## Parts (as drawn)
| Ref | Value | Connection | Role |
|---|---|---|---|
| Q20 | AO3401A P-FET (SOT-23) | Source VBAT, drain VSW, gate GATE net | Main switch |
| R20 | 100 k | VBAT to GATE | Holds Q20 off |
| R21 | 47 k | GATE to D20 anode | Button pull-down path |
| D20 | BAT54WS | Anode R21, cathode node X | One-way button path |
| SW20 | Tactile TS6635PA | Node X to GND (pins 2 and 4 used) | Button |
| Q21 | 2N7002 | Drain via R22 to GATE, source GND, gate HOLD | ESP32 hold switch |
| R22 | 47 k | GATE to Q21 drain | |
| R23 | 100 k | HOLD to GND | Keeps latch off until ESP32 drives HOLD |
| D21 | BAT54WS | Anode BTN, cathode node X | Lets ESP32 read the button |
| R24 | 100 k | BTN to 3.3v | BTN pull-up |
| C20 | 150 nF | GATE to VSW | Slows turn-on (soft-start) |
| R25 | 100 k | VSW to GND | Drains VSW when off |
| R26 | 100 k | 3.3v to GND | Stops 3.3v floating through D21 when off |

Diode pin convention used: BAT54WS (SOD-323) pin 1 = cathode, pin 2 = anode `[MEMORY]`; verify in the EasyEDA symbol.

## Operation
1. **Off:** R20 holds gate = source, Q20 off. Nothing draws current.
2. **Press:** current flows VBAT, R20, R21, D20, button, GND. R20/R21 divide the gate to about one third of VBAT.
   Vgs is about **-4.1 V at 6 V and -5.7 V at 8.4 V** (check the AO3401A allows about 12 V `[MEMORY]`). Q20 turns on.
3. **Boot:** VSW rises, buck makes 3.3 V, ESP32 boots. The user must **keep holding about 1 second** until HOLD is asserted.
4. **Latch:** ESP32 sets HOLD (IO4) high. Q21 turns on and pulls R22 low, so the gate stays low without the button.
5. **Read button:** R24 pulls BTN high. A press pulls node X low and D21 pulls BTN to about 0.3 V.
6. **Off:** ESP32 sets HOLD low. Q21 off, R20 pulls gate up, Q20 off, R25 drains VSW.
7. **Soft-start:** C20 feeds VSW's rise back to the gate, limiting inrush into the 2000 uF modem capacitor (aim under 1 A; tune on a scope).

Why two diodes: D20 lets the button pull the gate down but stops anything on the button side pushing it up. D21 stops the floating node X
(near battery voltage while off) reaching the ESP32 BTN pin.

## Firmware rules
- Assert HOLD as early as possible (bootloader hook).
- Ignore the first press until released. Debounce about 30 ms.
- After release: two or more further presses, each within 2 s of the last, inside a 10 s window = emergency. Otherwise release HOLD at 10 s.

## Risk: ESP32 reset kills power
HOLD is pulled low by R23 when the ESP32 resets or browns out, so the **whole device switches off** and only the button restarts it.
During an emergency this could silently end recording. Candidate mitigations: careful watchdog handling, extra 3.3 V capacitance,
or a small hardware change so the latch survives a short reset. **Not yet designed.**

## Sizing note
R21/R22 stay 47 k. With 4.7 k the gate falls about ten times faster, soft-start becomes ineffective and inrush into the 2000 uF capacitor
could be several amps and trip the BMS short-circuit protection `[ESTIMATE]`.
