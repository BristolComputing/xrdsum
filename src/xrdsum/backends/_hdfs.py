from __future__ import annotations

CONF = "/etc/hadoop/conf/hdfs-site.xml"
USER = "xrootd"


def get_namenodes() -> list[str]:
    """
    Get the list of namenodes from the HDFS configuration file.
    """
    import xml.etree.ElementTree as ET

    tree = ET.parse(CONF)
    root = tree.getroot()
    namenodes = []

    for prop in root.findall("property"):
        name = prop.find("name")
        if not name:
            continue
        if str(name.text).startswith("dfs.namenode.http-address"):
            value = prop.find("value")
            if not value:
                continue
            namenodes.append(str(value.text))
    return namenodes
