import xml.etree.ElementTree as ET

def readXML(outdir)
    return ET.parse(outdir+"//config.yxwv")

def parseSensitivePermissions(tree):
    root = tree.getroot()
    sp=root.find("./Value[@name='TB_GS_FSAM_SensitivePermissions']")
    return pd.DataFrame(sp.text.split("\n"),columns=["Permission"])
