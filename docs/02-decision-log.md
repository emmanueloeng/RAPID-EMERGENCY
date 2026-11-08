# 02. Decision log

| ID | Decision | Alternatives considered | Reason | Status |
|---|---|---|---|---|
| D01 | ESP32-S3 **module** (N8R8) not bare chip | Bare ESP32 chip with crystal, flash, RF matching | Module has crystal, flash, PSRAM, RF and antenna inside; far fewer parts and RF risk | `[DECISION]` |
| D02 | Keep **2S2P** pack | 1S2P (I recommended: simpler charger, no balancing) | Owner's modem board takes 5-12 V (seller claim) and the pack is already bought | `[DECISION]`, modem input range still to bench-test |
| D03 | Charger **BQ25887** (2S boost charger with balancing) | BQ25883 (has power path, no balancing), BQ25798 (1-4S buck-boost, 3.6-24 V in, overkill), BQ25882 (WCSP, hard to assemble) | 5 V in to 2S out, balancing built in, 4 x 4 mm QFN, TI reference design | `[DATASHEET]` |
| D04 | No power path: loads connect straight to the pack | BQ25883 with power path | Simpler for this product, device normally off while charging | `[DECISION]` |
| D05 | Use the modem's **GNSS**; drop the AI-Thinker GP02 | Separate GPS module | Saves space, same antenna-limited performance | `[DECISION]` |
| D06 | **Soft-latch** with P-FET (AO3401A) and N-FET hold (2N7002), ESP32 asserts HOLD | Dedicated power-switch IC | Simple, near-zero standby, independent of button sensing | `[DECISION]` |
| D07 | R21 and R22 stay **47 kohm** | 4.7 kohm | Slower gate pull-down gives soft-start; limits inrush into the 2000 uF capacitor | `[ESTIMATE]` verify on scope |
| D08 | **TPS62162** 3.3 V buck | LDO from 8.4 V | LDO would waste about 60 percent of the power | `[DATASHEET]` |
| D09 | **HTTPS POST** through the modem | MQTT, raw TCP | Owner's server accepts HTTP posts; TLS inside modem keeps ESP32 simple | `[DECISION]` |
| D10 | 8 kHz **IMA-ADPCM**, 20 s segments | Opus, 16 kHz | Small data, low CPU; fits 2G uplink poorly at 32 kbps so Opus is the upgrade path | `[DECISION]` |
| D11 | **No cancel** | Long-press cancel | Attacker could cancel it | `[DECISION]` |
| D12 | Keep the **first 1 MB** when there is no coverage | Keep the latest | Owner's choice | `[DECISION]` |
| D13 | Last-gasp at 3.3 V per cell, hard stop 3.0 V per cell | Run to BMS cutoff | Avoids cell damage and fire risk while squeezing out energy | `[DECISION]` |
| D14 | Prototype 1 uses the current pack as-is | Larger cells | Larger cells will not fit | `[DECISION]` |
| D15 | Keep **INMP441** microphone | ICS-43434 | Already bought | `[DECISION]` |
| D16 | Battery connector **JST XH 3-pin** (VBAT, MID, GND) | JST PH, soldered pads | XH is rated about 3 A per pin; PH is thin for 1.5 A bursts | `[MEMORY]` check JST datasheet |
| D17 | TS pin uses a **fixed 10 kohm** instead of an NTC for prototype 1 | NTC thermistor | No thermistor on the pack. Network gives 58.9 percent of REGN, inside the 44.75-68.25 percent window `[DATASHEET]` | `[DECISION]`, no cell temperature protection |
| D18 | **ILIM = 1.87 kohm** (about 0.59 A input) for prototype 1 | 1.24 kohm (about 0.9 A input) | Cell capacity unverified; keeps charge near 0.37 A | `[ESTIMATE]` |
| D19 | Balance resistor **33 ohm** (about 130 mA) | 9.5 ohm (400 mA, TI example) | 400 mA would dissipate about 1.7 W in a sealed box | `[ESTIMATE]` |
| D20 | **One LED** on two wires (H1), fed from REGN or 3.3 V, sunk by STAT or Q30 | Two LEDs | One discreet hole. Works with ESP32 off while charging | `[DECISION]` |
| D21 | Accept a **solid LED while charging**, even if button pressed | Interrupt charging in firmware to blink | Simplest; also discreet | `[DECISION]` |
| D22 | Modem power switch with a second P-FET (planned) | Rely on modem sleep only | Onboard buck on the core board draws current even when the modem is off | `[DECISION]` to be validated on bench |
| D23 | Designator ranges per block | Free numbering | Prevents clashes (see mistakes doc) | `[DECISION]` |
