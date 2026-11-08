# 14. Mistakes and corrections

Kept so that nobody repeats them.

| # | What went wrong | Who | Fix |
|---|---|---|---|
| 1 | Said the BQ25887 was "the same family" as the BQ25883 with a power path. It has **no power path and no OTG** | Assistant | Read the datasheet comparison table; design uses loads on the pack directly |
| 2 | First charger pin table put the inductor "SW to battery side". In a boost it sits **between PMID and SW** | Assistant | Corrected after re-reading TI Figure 73; netlist now right |
| 3 | Reused designators R1 and C2 in the latch table that already existed on the ESP32 sheet | Assistant | Per-block designator ranges (`AI_HANDOFF.md`) |
| 4 | Specified 1N5819WS diodes in the latch. Power Schottky has high reverse leakage, which could leak into the unpowered 3.3 V net | Assistant | Changed to BAT54WS (low leakage) |
| 5 | Soft-latch diodes drawn reversed (twice) | Owner | Fixed after netlist review |
| 6 | Net names did not match (`VBAT (+B)` vs `VBAT`, `GND (C-)` vs `GND`, `REGN` vs `$1N95`), leaving islands | Owner | Names must match exactly (`17-easyeda-notes.md`) |
| 7 | Battery-sense divider top end left floating (R27 on its own net) | Owner | Joined to VSW |
| 8 | R42 drawn as 33 ohm instead of 300 ohm; C44 and C45 entered as 44 uF each; SNS pins on separate nets | Owner | Corrected in later netlists |
| 9 | Single LED wired so STAT could only turn it off, and D1 had a DO-41 footprint | Owner | Replaced with the two-supply circuit (`07-status-led.md`) |
| 10 | Early assumption that 5 V USB can charge 2S directly | Owner | Boost charger required |
| 11 | Initial "interview" took nine rounds before any design | Assistant | Later rounds delivered diagrams and tables every turn |
| 12 | Suggested 2 x 4.7 k to the gate network question without noting soft-start loss until asked | Assistant | Answered with numbers; kept 47 k |
| 13 | Sense cap given as 44 uF "effective" without noting DC bias | Assistant | Two 22 uF, 16 V+ |

## Still unconfirmed assumptions
Diode pin numbering, MOSFET pin numbering (G, S, D = 1, 2, 3 for AO3401A and 2N7002 `[MEMORY]`), JST ratings, ESP32-S3 reserved pins, INMP441 sample-rate limits.
