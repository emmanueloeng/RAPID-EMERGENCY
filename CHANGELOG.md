# Changelog

## 2026-11-08
- Netlist checks 1-17 completed. Latest netlist: `Netlist_Schematic1_2026-11-08_8048b9.tel`.
- Fixed: REGN net label (LED supply now joins the charger REGN pin).
- Added: single status LED circuit (D30, D31, R30, Q30, R31, H1).
- Added: charger control pins (TS network, ILIM, PSEL, I2C pull-ups).
- Fixed: R42 value (300 ohm), C44 and C45 (22 uF each), SNS pins joined, VBUS net renamed.
- Added: battery connector U4 (JST XH 3-pin) with VBAT, MID, GND net names matched.
- Added: battery sense divider R27, R28, C21 (R27 now returns to VSW).
- Added: 3.3 V buck U3 (TPS62162), L60, C60, C61, R26.
- Fixed: soft-latch diode orientation, net names VBAT and VSW, switch node X joined.
- Corrected: charger inductor placement (between PMID and SW).
- Decided: accept a solid LED while charging, even if the button is pressed.

## Earlier
- Requirements interview, architecture decisions, charger selection (BQ25887), ESP32 module choice, power budget estimate.
