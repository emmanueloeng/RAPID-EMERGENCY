# tools

`check_netlist.py` reads an EasyEDA netlist (`.tel`) and checks the connections this design expects (power nets, latch, buck, charger, LED, ESP32 pins).
It prints errors and warnings and exits non-zero on failure. When you add a block, add its expected nets to the script so future changes cannot silently break it.

    python tools/check_netlist.py hardware/netlists/Netlist_Schematic1_2026-11-08_8048b9.tel
