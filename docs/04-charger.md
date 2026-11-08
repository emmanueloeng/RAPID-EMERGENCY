# 04. Charger (U5 BQ25887)

**Part:** TI BQ25887RGER or RGET (same chip, 4 x 4 mm 24-pin VQFN; R/E suffix is reel size, choose whichever JLCPCB stocks).
LCSC lists the RGER as C2761614 `[LISTING]`.
**Datasheet used:** SLUSD89 (the uploaded copy is the February 2019 advance-information revision). A production revision SLUSD89B (November 2019)
exists: re-check pin and register details against it before release.

## Why this part `[DATASHEET]`
2-cell I2C charger, boosts a 5 V USB input to charge a 2S pack, integrates all MOSFETs, current sensing, loop compensation, and
**cell balancing (400 mA)**. It has **no power path and no OTG** (the datasheet title says "with power path" but its comparison table and description say no).
It charges autonomously in default mode (no host needed) with a 12 hour safety timer.

## Defaults that matter `[DATASHEET]`
- Default **charge current 1.5 A**, 4.2 V per cell, termination 150 mA, 12 h timer. With the ESP32 off nothing can lower the 1.5 A default.
  **The ILIM resistor is therefore the hardware cap** (input current limit, which limits charge current).
- ILIM: input current = KILIM / RILIM, KILIM 1030-1192 A*ohm (typical 1111). Minimum supported 500 mA.
- PSEL pin: low = 3 A default input limit (ICO disabled), high = 500 mA (ICO enabled). We tie PSEL low and let ILIM set the cap.
- REGN output 4.7-4.8 V, 50 mA max.

## Pin-by-pin (as drawn) `[DATASHEET]`
| Pin | Name | Connection |
|---|---|---|
| 1 | PG | CHG_PG net, R51 10 k to 3.3v |
| 2 | STAT | Net STAT: LED cathode (H1.2), Q30 drain. See `07-status-led.md` |
| 3 | CD | Open |
| 4 | SDA | SDA net, R52 10 k to 3.3v |
| 5 | SCL | SCL net, R53 10 k to 3.3v |
| 6 | INT | CHG_INT net, R50 10 k to 3.3v |
| 7 | TS | R2 5.23 k to REGN, R44 30.1 k to GND, R45 10 k (fixed, replaces NTC) to GND |
| 8 | ILIM | R46 1.87 k to GND |
| 9 | MID | R42 300 ohm to MID net (J40 pin 2) |
| 10 | CBSET | R41 33 ohm to MID net |
| 11 | REGN | C43 4.7 uF to GND, net REGN |
| 12 | BTST | C42 47 nF to SW |
| 13, 14 | BAT | VBAT net, C4 10 uF to GND |
| 15, 16 | SNS | Net SNS: C44 and C45 22 uF each to GND, no other connection |
| 17, 18 | SW | L40 pin 1, C42 |
| 19, 20, pad 25 | GND | GND |
| 21, 22 | PMID | L40 pin 2, C41 10 uF to GND |
| 23 | VBUS | VBUS net, C40 1 uF to GND |
| 24 | PSEL | GND |

**Inductor L40 sits between PMID and SW** (boost topology). An earlier draft had this wrong; see `14-mistakes-and-corrections.md`.

## Choices that differ from TI's example
| Item | TI example | Ours | Why |
|---|---|---|---|
| ILIM | 383 ohm (about 2.9 A) | 1.87 kohm | Cap charge current while cell capacity is unverified |
| RCBSET | 9.5 ohm (400 mA) | 33 ohm (about 130 mA) | 400 mA would dissipate about 1.7 W in a closed box |
| TS network | 10 k NTC (103AT-2) | Fixed 10 k | No thermistor on the pack: no temperature protection |
| STAT LED | pull-up to logic rail | Fed from REGN or 3.3 V | Logic rail is absent while the ESP32 is off |
| SNS capacitance | 44 uF | 2 x 22 uF 16 V+ | Allow for DC-bias loss |

## Planned changes
- ILIM 1.24 kohm (about 0.9 A input, about 0.55 A charge) after cell capacity is measured.
- Add an NTC footprint (103AT-2) in a later revision.

## Unverified `[MEMORY]` or open
- That SNS is capacitor-only externally (read from TI Figure 73; confirm on TI's EVM schematic).
- Inductor L40 (VLS3012CX footprint) saturation current (want 1.5 A or more). TI's curves used DFE252012F-1R0.
- STAT pin maximum voltage (node K can float near 4.4 V when the LED is off).
- Behaviour when the BMS opens: the charger then sees no battery. Test on the bench.
