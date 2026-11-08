# 10. PCB guidelines (JLCPCB), not yet laid out

| Item | Recommendation |
|---|---|
| Size | About 40 x 28 mm main board; pack (40 x 30 x 8 mm) beneath, modem board beside or above |
| Layers | 4 layers: top signal and parts, solid GND, power pours (VSW, 3.3 V), bottom signal. A 2-layer board is possible but harder because of the boost converter and two antennas |
| Assembly | Parts on the top side only for prototype 1 (cheaper) |
| Power traces | At least 1 mm (or pours) on the pack, VSW and modem path |
| Charger | Tight loop: PMID capacitor, SW node and L40. Via array under the exposed pad |
| Balance resistor R41 | About 0.5 W while balancing: use 1 W 2512 and keep at least 5 mm from the cells (note: currently drawn as 0603, change it) |
| Buck | C60 next to U3 pin 2, C61 and L60 close to pin 7 |
| ESP32 | C3 and C1 as close as possible to pin 2; antenna end clear of copper if a PCB-antenna module is used (1U needs no keep-out) |
| Microphone | Away from inductors; sound hole aligned to the enclosure hole; short I2S traces; consider 22-33 ohm series on BCLK |
| Antennas | GNSS patch facing up, away from the cells; LTE antenna at the opposite end; keep an air gap from the cells; test inside the real enclosure |
| USB-C | At the board edge; ESD and TVS on VBUS and data |
| Spare | NTC footprint (unpopulated), test pads on VBAT, VSW, 3.3v, GND, EN, HOLD, SDA, SCL |
| Package sizes | See `17-easyeda-notes.md` |
