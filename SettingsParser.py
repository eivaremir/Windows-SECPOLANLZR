import xml.etree.ElementTree as ET
import pandas as pd

def readXML(outdir):
    return ET.parse(outdir+"//config.yxwv")

def parseSensitivePermissions(tree):
    root = tree.getroot()
    sp=root.find("./Value[@name='TB_GS_FSAM_SensitivePermissions']")
    return pd.DataFrame(sp.text.split("\n"),columns=["Permission"])

def parseNoAuditLabels(tree):
    root = tree.getroot()
    sp=root.find("./Value[@name='TB_GS_AP_Labels']")
    return pd.DataFrame(sp.text.split("\n"),columns=["Labels"])

def parseControlSettings_01(tree):
    root = tree.getroot()
    sp=root.find("./Value[@name='TB_GS_AP_Labels']")
    return pd.DataFrame(sp.text.split("\n"),columns=["Labels"])