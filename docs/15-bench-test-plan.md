# 15. Bench test plan for prototype 1

Run in this order. Stop and fix on any failure.

| Step | Test | Pass criterion |
|---|---|---|
| 1 | Resistor-discharge the pack, log current x time | Real capacity measured (decides charge current and runtime) |
| 2 | Pack cell voltages before paralleling | Pairs within 0.05 V |
| 3 | Modem core board on a **bench supply**, 5 V then 6, 7, 8.4 V, current limit 1 A | Boots, answers AT, no heating, record idle current at each voltage |
| 4 | Check core-board TXD idle voltage, KEY pulse polarity and timing | Documented; decide level shifting |
| 5 | AT commands: variant (FASE), GNSS on, bands | GNSS responds; bands include those used in Nigeria |
| 6 | Read the tantalum capacitor marking | Rated 16 V or more |
| 7 | Board power-up with bench supply as battery, Q20 only | VSW rises smoothly, 3.3 V correct, standby draw 15-25 uA |
| 8 | Scope Q20 and Q80 turn-on into the bulk capacitor | Inrush under about 1 A (tune C20, C80) |
| 9 | Press and hold button, release | Latch holds after about 1 s, shuts off when HOLD low |
| 10 | Emergency press sequence timing | Detected per rules, 10 s auto-off works |
| 11 | USB charging with ILIM 1.87 k | About 0.59 A input, about 0.37 A into the pack, STAT LED lit, termination, balancing at top |
| 12 | BMS: over-discharge cut-off and recovery with the charger | Pack recovers; record thresholds |
| 13 | 2 A modem burst: scope VIN at the board and VSW | No dip below the modem's minimum, no ESP32 reset |
| 14 | ESP32 reset while latched | Measure what happens; drives the watchdog design |
| 15 | Real upload test over the Nigerian network, 2G and LTE | Upload speed versus 32 kbps audio, TLS works |
| 16 | GNSS cold and hot start inside the enclosure | Fix time acceptable |
| 17 | Runtime test on the real pack in Phase B and Phase C | Replaces the estimates in `03-power-architecture.md` |
