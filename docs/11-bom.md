# 11. Bill of materials status

Full draft in `hardware/bom/bom_v0.1.csv`. Only two LCSC part numbers have been checked so far.

| Item | Part | Status |
|---|---|---|
| Charger U5 | TI BQ25887RGER (LCSC C2761614) or RGET | Datasheet read; pick whichever has JLCPCB stock |
| Fallback charger | TI BQ25883RGER (LCSC C544362) | Not used; has power path, no balancing |
| Buck U3 | TI TPS62162DSGR (3.3 V fixed, WSON-8 2 x 2 mm) | Family datasheet read; exact LCSC number not checked. Do **not** use the adjustable TPS62160 (FB to GND would give the wrong voltage) |
| MCU U1 | Espressif ESP32-S3-WROOM-1U-N8R8 | Candidate; confirm exact module and stock |
| Mic | INMP441 breakout (prototype) | Check chip availability for production |
| Modem | A7670E-FASE core board | Purchased; bench checks pending |
| Q20 | AO3401A P-FET | Candidate; check Vgs max (about 12 V) |
| Q21, Q30 | 2N7002 | Candidate |
| D20, D21, D30, D31 | BAT54WS | Candidate; low reverse leakage needed |
| L40 | 1 uH (DFE252012F-1R0 used by TI) | Drawn with VLS3012CX footprint: verify Isat of 1.5 A or more |
| L60 | 2.2 uH, Isat 1.4 A or more | VLS3012CX drawn; verify |
| Battery connector U4 | JST XH 3-pin | Candidate |
| Capacitors, resistors | See CSV | Values set; voltage ratings and LCSC numbers to be chosen |

## Not yet in the schematic
USB-C connector (16-pin with data lines recommended), 2 x 5.1 k CC resistors, TVS, ESD chip (USBLC6-2SC6 candidate), 2 x 0 ohm,
microphone connector and parts, modem interface (Q80-Q82, R80-R83, C80, C81, J80), test pads TP1-TP8.

## Prices
Not collected. Only BQ25887 (about $2.29) and BQ25883 (about $3.24) were seen on LCSC.
