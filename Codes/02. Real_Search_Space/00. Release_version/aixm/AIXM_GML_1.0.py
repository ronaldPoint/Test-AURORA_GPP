# -*- coding: utf-8 -*-


from  lxml  import etree as et
import xml_reader as x


# This path is a relative path in a Windows Systems. To use on Linux or Mac, copy the right path for each OS
# FILE = "xml\EA_AIP_DS_FULL_20170701 - Moved_Piombino.xml"    # For AIMX with objects moved from Donlon  to Piombino
FILE = "xml\EA_AIP_DS_FULL_20170701.xml"              # For original AIXM Donlon file 

target_tag = '//aixm:AirspaceVolume'                            # target tag to be extracted

xml = x.xml_aixm(FILE, target_tag)                              # Read aixm (.xml) file 

nsx = {"gml":"http://www.opengis.net/gml/3.2",      # Namespaces definitions
       "aixm":"http://www.aixm.aero/schema/5.1.1", 
       "xsi":"http://www.w3.org/2001/XMLSchema-instance"}


root = et.Element('{http://www.opengis.net/gml/3.2}FeatureCollection', nsmap=nsx)

def getid(node):                                                # get the Id for node extracted
    try:
        return node.attrib['{http://www.opengis.net/gml/3.2}id']
    except:
        return ''

def addchild(parent, node):                                     # Add child tags to create structure
    for child in node:
        parent.append(child)

## Gnereate the whole structure for GML file
for i in xml.paths[:]:
    member = et.Element("{http://www.opengis.net/gml/3.2}member")
    member.attrib['{http://www.opengis.net/gml/3.2}id'] = getid(i)    
    addchild(member, i)
    root.append(member)

tree = et.ElementTree(root)                                     # Create the tree gml structure

# Save data in GML file
tree.write('GML_demo_output.gml', pretty_print = True, xml_declaration = True, encoding='utf-8')

# #############################################################
# ## If is needed to use the shape file creation from aixm file

# import pandas as pd

# FILE_SHP = "./data/test0001"
# # path = '//aixm:AirspaceVolume'
# xml = x.xml_aixm(FILE, target_tag)

# xml.repair_tags()
# tags_full = []

# df = pd.DataFrame(columns = xml.tags_columns)

# xml.xml_to_df()
# d = xml.data

# for i in d.iterrows():
#     cc= i[1].to_dict()
#     break

# alp = x.data_shp(FILE_SHP, d, cc)
