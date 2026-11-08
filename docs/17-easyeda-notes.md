# 17. EasyEDA notes for this project

## Designator ranges
ESP32 1-19, latch 20-39, charger 40-59, buck 60-79, modem interface 80-99, microphone 100-109.
(Some parts drawn earlier break this: C4 is the charger BAT capacitor, R2 is the TS resistor, U1 to U5 are ICs and the connector. They are listed in `hardware/designators.csv`.)

## Net names currently in use (exact spelling)
`VBAT`, `GND`, `MID`, `VSW`, `3.3v`, `REGN`, `VBUS`, `STAT`, `HOLD`, `BTN`, `LED`, `EN`, `VBAT_SENSE`, `SDA`, `SCL`, `CHG_INT`, `CHG_PG`,
`I2S_BCLK`, `I2S_WS`, `I2S_SD`, `MODEM_KEY`, `MODEM_PWR`, `MODEM_SLEEP`, `UART_TX`, `UART_RX`, `USB_DM`, `USB_DP`, `TXD0`, `RXD0`.
Labels on text only do not make a net. Use a real net label. Spaces, brackets and different capitalisation make a different net.

## Capacitor and resistor package sizes
Imperial code and size: 0201 (0.6 x 0.3 mm, avoid), 0402 (1.0 x 0.5 mm), 0603 (1.6 x 0.8 mm, default), 0805 (2.0 x 1.25 mm), 1206 (3.2 x 1.6 mm).
The same number in metric means a different size (metric 0603 is imperial 0201). EasyEDA and JLCPCB use imperial.
Choose: value, then voltage rating (at least double the working voltage), then dielectric (X7R or X5R, never Y5V), then package (bigger holds more capacitance at high voltage), then JLCPCB stock (prefer Basic parts).

## Exporting and reviewing
Design, then Export Netlist (`.tel`). A netlist shows exactly which pins share a net, which a screenshot does not.
Run `python tools/check_netlist.py hardware/netlists/<file>.tel`.

## Library tips
- Check the pin names and numbers on every symbol against the datasheet.
- Check the footprint size in the preview.
- Record the LCSC part number (C followed by digits) for the BOM.
- Use JLCPCB library footprints for QFN and WSON exposed pads.
