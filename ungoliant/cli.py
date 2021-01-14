import datetime
import requests
import sys


def normalise_datetime(s):
    try:
        return datetime.datetime.strptime(s, "%d/%m/%Y %I:%M %p").strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return s


class Outage:
    MAP = {
        "OBJECTID": None,
        "OUTAGETYPE": None,
        "INCIDENTREF": None,
        "ENARNUMBER": None,
        "OUTAGESTARTTIME": normalise_datetime,
        "ESTIMATEDRESTORATIONTIME": normalise_datetime,
        "PLANNEDOUTAGE": None,
        "NOCUSTOMERSIMPACTED": None,
        "AFFECTED_AREA": None,
        "AFFECTED_AREA_NOCUSTOMERS": None,
        "Tags": None,
    }

    def __init__(self, attrs):
        # {'attributes': {'OBJECTID': 218408, 'OUTAGETYPE': 'P', 'INCIDENTREF': 'INCD-403661-h', 'ENARNUMBER': '441940', 'OUTAGESTARTTIME': '04/01/2021 08:25 AM', 'ESTIMATEDRESTORATIONTIME': '14/01/2021 07:00 PM', 'PLANNEDOUTAGE': 'Planned', 'NOCUSTOMERSIMPACTED': 1, 'TIMEADDED': 1610632829000, 'AFFECTED_AREA': 'MALLEE HILL', 'AFFECTED_AREA_NOCUSTOMERS': '1', 'Tags': '', 'SHAPE__Area': 2818.26171875, 'SHAPE__Length': 188.224317526473}}
        for k in self.MAP:
            setattr(self, k.lower(), (self.MAP[k] or (lambda x: x))(attrs[k]))


def get_features():
    response = requests.get(
        "https://services2.arcgis.com/tBLxde4cxSlNUxsM/arcgis/rest/services/WP_Outage_Prod/FeatureServer/0/query?where=1=1&outFields=*&returnGeometry=false&f=json"
    )
    if response.status_code != 200:
        return None
    j = response.json()
    return [
        Outage(feature["attributes"])
        for feature in sorted(j["features"], key=lambda f: f["attributes"]["OBJECTID"])
    ]


def print_feature_table(outages):
    fmt = "{:>16} | {:>16} | {:>5} | {}"
    rule = ["-"] * 80
    rule[17] = rule[36] = rule[44] = "|"
    print(fmt.format("Started", "Est. Restoration", "Cust.", "Affected areas"))
    print("".join(rule))
    for o in outages:
        print(
            fmt.format(
                o.outagestarttime,
                o.estimatedrestorationtime,
                o.nocustomersimpacted,
                o.affected_area,
            )
        )


def main():
    features = get_features()
    if features is None:
        print("unable to contact ArcGIS server", fd=sys.stderr)
        return
    print_feature_table(features)
    print(
        """
Please note: This tool is unoffical.
For more detail: https://www.westernpower.com.au/faults-outages/power-outages/""",
        file=sys.stderr,
    )
