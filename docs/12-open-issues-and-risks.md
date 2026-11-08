# 12. Open issues and risks

Severity: **H** could stop the product working or cause danger, **M** could cause a redesign, **L** tidy-up.

| # | Sev | Issue | Action |
|---|---|---|---|
| 1 | H | Cell capacity and discharge rating unverified (label 700 mAh, size suggests much less) | Resistor-discharge test; limits charge current and 2 A burst capability |
| 2 | H | Modem board VIN range unverified (sources disagree: 5-16 V, 5-12 V, 0.8-4.2 V). Wrong value destroys it | Bench-supply test from 5 V upward before connecting the pack |
| 3 | H | ESP32 reset drops HOLD and powers the device off mid-emergency | Design a watchdog and rail hold-up strategy |
| 4 | H | BMS thresholds unknown; behaviour when it cuts off with the charger attached unknown | Bench test; use a datasheet-backed protection IC in production |
| 5 | H | Which core-board variant arrives (FASE with GNSS?) | Check label and AT commands on delivery |
| 6 | M | Inrush into the 2000 uF capacitor could trip the BMS | Scope Q20 and Q80 turn-on, tune C20 and C80 |
| 7 | M | Modem sleep and idle current (onboard buck) unknown | Measure; Q80 allows full cut |
| 8 | M | Production datasheet for BQ25887 (SLUSD89B) not re-read; SNS wiring, STAT max voltage unchecked | Read and confirm |
| 9 | M | L40 and L60 (VLS3012CX) saturation currents unchecked | Check datasheets |
| 10 | M | R41 (33 ohm, about 0.5 W when balancing) drawn as 0603 | Change to 1 W 2512 |
| 11 | M | Buck EN tied to VSW: absolute maximum of EN pin not checked; soft-start time not read | Read datasheet section 7 and 8 |
| 12 | M | UART voltage level of the core board unknown | Measure TXD idle level before connecting |
| 13 | M | No temperature protection on the pack (fixed TS resistor) | Add NTC for later builds |
| 14 | M | Tantalum capacitor on the core board may be rated too low for 8.4 V | Read its marking |
| 15 | M | 2G uplink may be slower than the audio rate (32 kbps) | Test real uplink; consider Opus |
| 16 | M | TLS on 2G: certificate chain, cipher support, expiry | Test against the real server |
| 17 | L | SW20 pin 1 unconnected (pins 1 and 2 may be internally joined) | Tie pin 1 to 2 and 3 to 4 |
| 18 | L | Several values blank in the netlist (Q20, Q21, Q30, D20, D21, D30, D31, U1, U3, U5, headers); U1 value reads "2.4GHz" | Fill in |
| 19 | L | Diode pin convention (pin 1 cathode) assumed | Verify in EasyEDA symbol |
| 20 | L | Capacitor voltage ratings (C20 16 V+, C40 25 V, C41 25 V, C60 25 V) not stored in netlist | Choose parts |
| 21 | L | First press must be held about 1 s to power on | Confirm acceptable (owner has not objected) |

## Use and consent risk (raised, set aside by the owner)
A device made to look like a charger that records audio can be misused for stalking or covert surveillance, and recording laws vary by region.
The owner asked to ignore compliance and use controls. Revisit before any distribution: user-owned accounts, no remote activation,
clear consent rules, and the regulatory items (radio certification, battery transport, cell safety standards).
