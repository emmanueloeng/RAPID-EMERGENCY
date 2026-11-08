# 06. ESP32-S3 core and GPIO map

**Module:** ESP32-S3-WROOM-1U footprint (U1), N8R8 variant (8 MB flash, 8 MB octal PSRAM). The 1U variant has a u.FL antenna connector
and no PCB antenna. Wi-Fi and Bluetooth are not used, so no antenna is needed. Make sure the ordered part is the 1U N8R8.
Reference: Espressif's minimal-system schematic for the S3-WROOM-1 module (owner's screenshot).

## Minimal circuit as drawn
| Ref | Value | Role |
|---|---|---|
| C3 | 22 uF | 3V3 bulk, at the module pin |
| C1 | 100 nF | 3V3 decoupling, closest to the pin |
| R1 | 10 k | EN pull-up to 3.3v (`[MEMORY]` Espressif guideline) |
| C2 | 1 uF | EN to GND, delays enable |
| SW1 | tactile | EN to GND reset button (**prototype only**, remove for production) |
| U2 | 4-pin header | TXD0, RXD0, GND, GND: serial flashing |
| H2 | 2-pin header | IO0 to GND: short to GND while resetting to enter flashing mode |
| GND | pins 1, 40, 41 | all to ground; exposed pad needs vias on the PCB |

**Removed from the reference:** JTAG header (IO39-42 left unused, test pads optional), 32.768 kHz crystal and its capacitors, UART header 3V3 pin,
the IO47/IO48 1.8 V note (applies to other variants), crystal, flash chip, RF matching and antenna (all inside the module).
Unused pins carry no-connect flags. **IO35, IO36, IO37 must stay unconnected** (octal PSRAM).

## Pins to avoid `[MEMORY]` (confirm in the module datasheet)
GPIO26-32 (flash), GPIO35-37 (octal PSRAM), strapping GPIO0, 3, 45, 46, USB GPIO19 and 20 (used here for native USB), UART0 GPIO43 and 44.

## GPIO map (module pin number in brackets) `[DECISION]`
| Net | GPIO (pin) | Function |
|---|---|---|
| HOLD | IO4 (4) | Latch hold to Q21 |
| BTN | IO5 (5) | Button sense |
| LED | IO6 (6) | Status LED driver (Q30 gate) |
| MODEM_PWR | IO7 (7) | Modem power switch (planned) |
| MODEM_KEY | IO15 (8) | Modem power key (polarity unverified) |
| MODEM_SLEEP | IO16 (9) | Modem sleep/DTR |
| UART_TX | IO17 (10) | To modem RXD |
| UART_RX | IO18 (11) | From modem TXD |
| USB_DM | IO19 (13) | USB D- (optional native USB) |
| USB_DP | IO20 (14) | USB D+ |
| VBAT_SENSE | IO2 (38) | Battery voltage divider |
| SDA | IO9 (17) | Charger I2C |
| SCL | IO10 (18) | Charger I2C |
| CHG_INT | IO11 (19) | Charger interrupt |
| I2S_BCLK | IO12 (20) | Mic clock |
| I2S_WS | IO13 (21) | Mic word select |
| I2S_SD | IO14 (22) | Mic data in |
| CHG_PG | IO21 (23) | Charger power-good |
| IO0 | IO0 (27) | Boot mode pad (H2) |
| TXD0 / RXD0 | pins 37 / 36 | Serial flashing (U2) |

Check the modem board's UART voltage before connecting. The A7670E UART is natively 1.8 V; the core board may include level shifting `[MEMORY]`.

## USB plan
Native USB (IO19/IO20) can flash and debug without a serial adapter. It needs a USB-C receptacle with data pins, ESD protection (candidate ST USBLC6-2SC6 `[MEMORY]`)
and two 0 ohm links. Decision pending (see `13-roadmap.md`). For production, disable JTAG and USB debug with ESP32-S3 eFuses.
