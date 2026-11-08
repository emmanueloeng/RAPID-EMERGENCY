# 13. Roadmap

## Done
- [x] Requirements and decisions (`01`, `02`)
- [x] ESP32 core, GPIO map
- [x] Soft-latch and button
- [x] 3.3 V buck
- [x] Charger (power stage, control pins)
- [x] Single status LED
- [x] Battery connector and sense
- [x] Netlist checks up to 2026-11-08

## Schematic still to draw (about 20 parts plus 8 test pads)
- [ ] **USB-C input (7 parts):** J50 receptacle, R51 and R52 5.1 k (CC1, CC2 to GND), D50 TVS on VBUS, U50 ESD chip on D+/D-, R53 and R54 0 ohm links.
      Decision needed: 16-pin with data (recommended) or power-only.
- [ ] **Microphone (3 parts):** J100 6-pin header for the INMP441 breakout (3V3, GND, SCK, WS, SD, L/R to GND), C100 100 nF, optional R100 22-33 ohm on BCLK.
- [ ] **Modem interface (10 parts):** see `08-modem-and-battery.md`. Finish after the bench test.
- [ ] **Test pads TP1-TP8:** VBAT, VSW, 3.3v, GND, EN, HOLD, SDA, SCL.

## Then
1. Fix the items in `12-open-issues-and-risks.md` marked L and M that are schematic changes.
2. Set every part value, choose real LCSC parts (voltage ratings!), regenerate the BOM.
3. Run EasyEDA ERC, export a netlist, run `tools/check_netlist.py`.
4. Design the watchdog and hold-up for ESP32 resets.
5. PCB layout per `10-pcb-guidelines.md`, then layout review.
6. Bench tests (`15-bench-test-plan.md`), then firmware.
7. Second revision: NTC, protection IC replacing the purchased BMS, faster charge current, production notes (eFuses).
