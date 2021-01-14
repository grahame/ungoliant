# ungoliant: unofficial CLI tool to list Perth power outages

Makes use of Western Power data.

## Installation

For normal usage:
```bash
pip3 install ungoliant
```

For development, clone this repo and then run:

```bash
poetry install
# to run the tool
poetry run ungoliant
```

Example output:

```
         Started | Est. Restoration | Cust. | Affected areas
-----------------|------------------|-------|-----------------------------------
2021-01-14 08:13 | 2021-01-14 16:30 |   297 | GERALDTON,MOUNT TARCOOLA
2021-01-14 08:04 | 2021-01-14 18:30 |   575 | BEDFORDALE,ROLEYSTONE
2021-01-04 08:25 | 2021-01-14 19:00 |     1 | MALLEE HILL
2021-01-14 13:56 | 2021-01-14 16:30 |    43 | DAYTON
2021-01-14 10:26 | 2021-01-14 18:30 |   123 | DAWESVILLE,BOUVARD
2021-01-14 11:17 | 2021-01-14 17:00 |    28 | MILO,MOORIARY,MOUNT ADAMS,YARDARINO
2021-01-14 14:57 | 2021-01-14 17:30 |     6 | HARVEY
2021-01-14 13:34 | 2021-01-14 23:30 |   362 | BAYSWATER,EMBLETON
2021-01-14 00:08 | 2021-01-14 21:04 |    68 | GIDGEGANNUP,BRIGADOON

Please note: This tool is unoffical.
```
