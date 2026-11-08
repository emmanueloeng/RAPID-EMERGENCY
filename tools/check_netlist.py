#!/usr/bin/env python3
"""Check an EasyEDA netlist (.tel) against the connections this design expects.

Usage: python tools/check_netlist.py hardware/netlists/<file>.tel
Exit code 0 when every check passes (known open items are only warnings).
"""
import sys

def parse(path):
    text = open(path, encoding="utf-8", errors="ignore").read().replace("\r", "")
    entries, buf, in_nets = [], "", False
    for line in text.split("\n"):
        if line.startswith("$NETS"):
            in_nets = True
            continue
        if not in_nets:
            continue
        if line.startswith("$"):
            break
        if line[:1] in (" ", "\t", ","):
            buf += " " + line.strip()
        else:
            if buf:
                entries.append(buf)
            buf = line.strip()
    if buf:
        entries.append(buf)
    nets = {}
    for e in entries:
        name, _, pins = e.partition(";")
        name = name.strip().strip("'")
        nets[name] = {p for p in pins.replace(",", " ").split() if "." in p}
    return nets

def net_of(nets, pin):
    for n, pins in nets.items():
        if pin in pins:
            return n, pins
    return None, set()

EXPECTED_NAMED = {
    "VBAT": "Q20.2 R20.2 U4.1 U5.13 U5.14 C4.2",
    "VSW": "C20.1 C60.1 Q20.3 R25.2 R27.2 U3.2 U3.3",
    "3.3v": "U1.2 U3.6 L60.2 C61.1 R26.2 R1.2 R24.1 D31.2 R50.1 R51.1 R52.1 R53.1 C1.2 C3.2",
    "GND": "U1.1 U1.40 U1.41 U3.1 U3.4 U3.5 U3.9 U5.19 U5.20 U5.24 U5.25 U4.3 Q21.2 Q30.2 SW20.4 R23.1 R25.1 R26.1 R28.2 R31.2 R44.1 R45.1 R46.1",
    "REGN": "U5.11 C43.1 R2.2 D30.2",
    "STAT": "U5.2 Q30.3 H1.2",
    "LED": "U1.6 Q30.1 R31.1",
    "HOLD": "U1.4 Q21.1 R23.2",
    "BTN": "U1.5 D21.2 R24.2",
    "EN": "U1.3 R1.1 C2.1 SW1.2",
    "MID": "U4.2 R41.2 R42.2",
    "VBUS": "U5.23 C40.2",
    "VBAT_SENSE": "U1.38 R27.1 R28.1 C21.1",
    "SDA": "U1.17 U5.4 R52.2",
    "SCL": "U1.18 U5.5 R53.2",
    "CHG_INT": "U1.19 U5.6 R50.2",
    "CHG_PG": "U1.23 U5.1 R51.2",
    "TXD0": "U1.37 U2.1",
    "RXD0": "U1.36 U2.2",
}
# Nets that have no usable name: located through one known pin.
EXPECTED_BY_PIN = {
    "gate net": ("Q20.1", "R20.1 R21.2 R22.2 C20.2"),
    "switch node X": ("D20.1", "D21.1 SW20.2"),
    "Q21 drain via R22": ("Q21.3", "R22.1"),
    "D20 anode to R21": ("D20.2", "R21.1"),
    "PMID node": ("U5.21", "U5.22 L40.2 C41.1"),
    "SW node": ("U5.17", "U5.18 L40.1 C42.1"),
    "BTST node": ("U5.12", "C42.2"),
    "SNS node": ("U5.15", "U5.16 C44.1 C45.1"),
    "TS node": ("U5.7", "R2.1 R44.2 R45.2"),
    "ILIM node": ("U5.8", "R46.2"),
    "MID pin resistor": ("U5.9", "R42.1"),
    "CBSET pin resistor": ("U5.10", "R41.1"),
    "buck switch node": ("U3.7", "L60.1"),
    "LED node A": ("D30.1", "D31.1 R30.2"),
    "LED to H1": ("H1.1", "R30.1"),
    "IO0 pad": ("U1.27", "H2.1"),
}
GPIO_ONLY = {"I2S_BCLK": "U1.20", "I2S_WS": "U1.21", "I2S_SD": "U1.22", "MODEM_KEY": "U1.8",
             "MODEM_PWR": "U1.7", "MODEM_SLEEP": "U1.9", "UART_TX": "U1.10", "UART_RX": "U1.11",
             "USB_DM": "U1.13", "USB_DP": "U1.14"}
KNOWN_OPEN = ["SW20.1"]

def main(path):
    nets = parse(path)
    errors, warnings = [], []
    for name, req in EXPECTED_NAMED.items():
        have = nets.get(name)
        if have is None:
            errors.append(f"net '{name}' is missing")
            continue
        missing = set(req.split()) - have
        if missing:
            errors.append(f"net '{name}' lacks {sorted(missing)}")
    for label, (anchor, req) in EXPECTED_BY_PIN.items():
        n, pins = net_of(nets, anchor)
        if n is None:
            errors.append(f"{label}: pin {anchor} is not on any net")
            continue
        missing = set(req.split()) - pins
        if missing:
            errors.append(f"{label} (net '{n}', has {anchor}) lacks {sorted(missing)}")
    for name, pin in GPIO_ONLY.items():
        if name not in nets or pin not in nets[name]:
            errors.append(f"GPIO net '{name}' should contain {pin}")
    for name, pins in nets.items():
        if len(pins) == 1 and name not in GPIO_ONLY:
            warnings.append(f"net '{name}' has a single pin {sorted(pins)}")
    for pin in KNOWN_OPEN:
        if net_of(nets, pin)[0] is None:
            warnings.append(f"known open item: {pin} is unconnected")
    print(f"Parsed {len(nets)} nets from {path}")
    for w in warnings:
        print("WARNING:", w)
    for e in errors:
        print("ERROR:  ", e)
    print("PASS" if not errors else f"FAIL ({len(errors)} errors)")
    return 1 if errors else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
