# AI and engineer handoff

Read this before changing anything. It tells you how this project has been run, what is already decided, and what to do next.

## Ground rules (these were agreed with the project owner)
1. **Do not invent specifications.** If a number was not read from a datasheet or listing, tag it `[MEMORY]` or `[ESTIMATE]` and say so.
2. **Verify against datasheets.** Prefer manufacturer reference circuits. Say which parts of a reference were adopted unchanged and which were modified.
3. **Check every connection.** The owner exports a netlist from EasyEDA (`.tel` file) after each change. Read it directly (do not trust screenshots), run `tools/check_netlist.py`, and report errors before moving on.
4. **Do not re-open settled decisions** listed in `docs/02-decision-log.md` unless you find a technical fault. The owner dislikes long interviews. Ask only questions that block the next step, and ask at most a few at a time.
5. **Show, do not only tell.** The owner works best from pictures plus a pin-by-pin table. Give a diagram and a table for every block.
6. **Own mistakes.** When a past statement was wrong, say so and log it in `docs/14-mistakes-and-corrections.md`.
7. **Be honest about uncertainty.** The device is for emergencies. A wrong assumption can cost a life, so flag risks plainly.

## How the owner works
- Draws schematics in **EasyEDA** (JLCPCB parts library). Prototype 1 is built on a JLCPCB-assembled board.
- Sends the exported netlist (`Netlist_Schematic1_<date>_<hash>.tel`) for checking.
- Writes in capitals and short messages. Often sends screenshots. Wants direct answers.

## Conventions
- **Designator ranges:** ESP32 block 1-19, soft-latch 20-39, charger 40-59, buck 60-79, modem interface 80-99, microphone 100-109.
  Never reuse a designator across blocks. (A clash with R1 and C2 caused a real error, see mistakes doc.)
- **Net names must match exactly** across sheets (case, punctuation). The current names are listed in `docs/17-easyeda-notes.md`.
- **Power nets:** `VBAT` (pack positive, BMS B+), `GND` (system ground, BMS C-), `MID` (cell midpoint, BMS B1),
  `VSW` (switched battery after Q20), `3.3v` (buck output, lowercase v), `REGN` (charger internal 4.7 V rail), `VBUS` (USB 5 V).
- **Confidence tags:** `[DATASHEET]`, `[LISTING]`, `[MEMORY]`, `[ESTIMATE]`, `[DECISION]`.

## Current state (2026-11-08)
Netlist in `hardware/netlists/` passes `tools/check_netlist.py`. Drawn: ESP32 core, soft-latch, 3.3 V buck, BQ25887 charger,
single status LED, battery connector, battery sense.

## Next task
Draw the remaining blocks in this order (details in `docs/13-roadmap.md`):
1. USB-C input (7 parts). Decision pending: 16-pin receptacle with data lines (recommended for prototype 1) or power-only.
2. Microphone connector (3 parts).
3. Modem interface (10 parts). Partly blocked until the modem core board is on the bench (KEY polarity, UART levels, VIN range).
4. Test pads (8).
5. Fix the small items in `docs/12-open-issues-and-risks.md`, set all part values, assign LCSC part numbers, then ERC and PCB layout.

## Things an AI should not do
- Do not assume the modem board accepts 8.4 V until the bench test passes (`docs/15-bench-test-plan.md`).
- Do not raise the charge current above the ILIM-set value until the real cell capacity is measured.
- Do not describe any circuit as production-proven. Everything is a prototype-1 design until validated.
