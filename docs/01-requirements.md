# 01. Requirements

## Product
A discreet emergency alert and tracking device that looks like a small phone charger. It is meant to help a person in danger
(abduction, assault, robbery) by sending audio and location to a company server. All electronics must fit in the enclosure.

## Enclosure and pack `[DECISION]`
- Enclosure: about **45 mm tall, 48 mm wide, 26 mm thick** (outer, from the owner).
- Pack: four cells in **2S2P**, label reads "XF 40 20 30, 700 mAh, 3.7 V", each about 4 x 20 x 30 mm, stacked to about 40 x 30 x 8 mm.
  The 700 mAh label is **unverified** (a cell this size is normally much smaller). See `docs/12-open-issues-and-risks.md`.
- Modem core board about 25-28 mm x 24-25 mm x 7 mm. Space for the rest of the circuit is the remaining volume.

## Behaviour `[DECISION]`
- No power use while inactive. A hardware soft-latch switch connects the battery only after the button is pressed.
- **First press** powers the device. **Two or more further presses**, each within 2 s of the last and inside a 10 s window, mean emergency.
- If no emergency presses arrive within 10 s, the device switches itself off.
- **No cancel function** (an attacker could use it).
- **Phase B (first 30 minutes):** record continuously in 20 s segments, upload as they complete, send GPS and device status. Start recording immediately; do not wait for GPS.
- **Phase C (after 30 minutes):** ESP32 awake, microphone on, silence discarded, GPS intermittent, cellular off between sends.
  Send when 5 minutes have passed, 20 s of meaningful audio has accumulated, or position changed beyond a threshold (50 m starting value, with filtering).
- **No coverage:** keep trying to send the alert and location only. Keep recording but store at most the **first 1 MB** of audio.
- **Low battery:** "last-gasp" mode at 3.3 V per cell (alert and GPS only, long sleeps), hard stop at 3.0 V per cell. No deliberate over-discharge.
- Only the button triggers an emergency (no motion or tamper sensing).

## Communications `[DECISION]`
- Modem: SIMCom **A7670E-FASE** core board (LTE Cat-1 with 2G fallback, onboard GNSS). Country: **Nigeria**; 2G fallback accepted.
- Transport: **HTTPS POST** (binary audio body, JSON metadata), TLS done inside the modem. What the server does with data is out of scope.

## Audio `[DECISION]`
- INMP441 I2S microphone (already purchased, kept). Speech must be intelligible, not high quality.
- 8 kHz IMA-ADPCM, about 4 KB/s (32 kbps). Opus is a later option.
- Silence gate: amplitude threshold with hangover, configurable in testing. Voice detection later if CPU allows.

## Charging `[DECISION]`
- USB-C, 5 V input. Slow and steady is fine (3 to 5 hours). The device need not operate while charging, but may if the button is pressed.

## Indicators `[DECISION]`
- One discreet LED: brief blink on the first button press, solid while charging.

## Out of scope (by the owner)
- Safety and regulatory certification, server behaviour, accelerometer/tamper detection.
