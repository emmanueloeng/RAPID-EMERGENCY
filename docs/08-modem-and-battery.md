# 08. Modem board, battery pack, BMS, connector, sense, planned modem interface

## Modem: SIMCom A7670E-FASE core board (purchased module)
- Variant: **FASE** has GNSS; LASE does not. The owner's listing offers several variants (A7670E-FASE, A7670E-LASE, A7670G-LABE), so check the label after delivery `[LISTING]`.
- Two different seller photos were seen: (a) a board with three u.FL connectors, a 4R7 inductor and a 7-pad edge; (b) a board with micro-USB, a nano-SIM slot,
  a 470 uF tantalum capacitor and a header labelled GND, RXD, TXD, KEY, VCC, GND, SLEEP. **Which board arrives must be confirmed.**
- Seller claims 5-12 V supply input (VCC pin) `[LISTING]`. Other manuals for similar boards say 5-16 V or even 0.8-4.2 V, so treat it as **unverified**.
  Apply a bench supply starting at 5 V before connecting the pack. Check the tantalum capacitor's voltage rating (want 16 V or more on 8.4 V).
- Modem peak current 2 A at its rail, under a millisecond, in 2G bursts `[LISTING]`. KEY pin polarity and timing, UART voltage, idle current, and GNSS presence are unverified.
- Nigeria bands (LTE B3/B7/B20, GSM 900/1800) are `[MEMORY]`, to be checked in the SIMCom datasheet. Carrier not yet chosen.

## Battery pack
- Four cells labelled "XF 40 20 30, 700 mAh, 3.7 V", 2S2P: two parallel pairs in series, about 7.4 V nominal, 8.4 V full. Capacity **unverified**
  (a 4 x 20 x 30 mm pouch cell is normally 150-250 mAh). Discharge rating quoted as 1C. A resistor-discharge test will settle the real capacity.
- Match the two cells in each pair within about 0.05 V before paralleling. Individual cells inside a pair cannot be monitored separately.

## BMS (purchased, prototype 1 only)
- Small 2S board, 24 x 12 mm, listed as "2S BMS 10A 8.4V", silkscreen possibly "YX-514". Thresholds and balancing unknown (assume protection-only).
- Terminals: **B-**, **B1**, **B+**, **C-**. One shared port: charger and load both connect to B+ and C-. Protection FETs are in the negative line.
- Wiring: charger BAT and system VBAT to **B+**, system GND to **C-**, charger MID and CBSET to **B1**.
- Production: replace with a datasheet-backed 2S protection IC on the PCB.

## Battery connector U4 (JST XH 3-pin, B3B-XH-A or side-entry S3B-XH-A) `[MEMORY]` ratings
| Pin | Net | Carries |
|---|---|---|
| 1 | VBAT (B+) | up to about 1.5 A in bursts |
| 2 | MID (B1) | about 0.1 A balancing |
| 3 | GND (C-) | return current |
Use 24 AWG or thicker on pins 1 and 3, 28 AWG on pin 2. Check connector height against the 26 mm enclosure (side-entry is flatter).

## Battery sense
R27 300 k (VSW to VBAT_SENSE), R28 100 k (to GND), C21 100 nF. Gives 1.5 V at 6 V and 2.1 V at 8.4 V into IO2. Fed from VSW so it draws nothing when off.

## Planned modem interface (designators 80-99, not yet drawn)
| Ref | Part | Role |
|---|---|---|
| Q80 | P-FET (same type as Q20) | High-side modem power switch from VSW |
| Q81 | N-FET 2N7002 | Drives Q80 from MODEM_PWR (IO7) |
| Q82 | N-FET 2N7002 | Pulses the modem KEY pin from MODEM_KEY (IO15) |
| R80-R83 | 100 k / 47 k / 10 k as needed | Gate pull-ups, pull-downs, KEY resistor |
| C80 | 150 nF | Soft-start on Q80 |
| C81 | 2000 uF, 16 V or higher (or two 470-1000 uF polymer) | Bulk capacitor at modem VIN, behind Q80. Check physical size |
| J80 | 7-pin connector | VCC, GND, KEY, SLEEP, RXD, TXD, GND to the core board |

Blocked on bench results: KEY polarity, UART voltage (level shifting needed?), VIN range, idle current.
