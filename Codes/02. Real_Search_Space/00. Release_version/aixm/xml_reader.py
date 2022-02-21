# -*- coding: utf-8 -*-

from lxml import etree as et
import pandas as pd 
import shapefile as sf

# Class to read xml file and translate to dataframe and field dicitonary
class xml_aixm:
    
    def __init__(self, file, path):
        self.xml = file
        self.path = path        
        self.tree = et.parse(self.xml).getroot()
        self.namespaces = {'aixm':'http://www.aixm.aero/schema/5.1.1','gml':'http://www.opengis.net/gml/3.2'}
        self.get_paths()
        self.get_tags()
        self.repair_tags()
        self.data = pd.DataFrame(columns = self.tags_columns) 
        
    def get_paths(self):
        self.paths = self.tree.xpath(self.path, namespaces= self.namespaces)
    
    def get_tags(self):
        tagfields = []
        tags_full = []
        for elem in self.paths:
            if len(elem):
                childs = elem.findall(".//")
                for e in childs:
                    tag = str(e.tag).replace('{'+self.namespaces['aixm']+'}', '').replace('{'+self.namespaces['gml']+'}', '')          
                    tagfields.append(tag)
                    tags_full.append(e.tag)
        self.tags_columns = pd.unique(tagfields)  # solo los tag sin namespaces
        self.tags_full_df = pd.unique(tags_full)
# Reconstruct the tags with the namespaces for gml file                
    def repair_tags(self):
        self.tags = []
        for i in self.tags_full_df:
            value_ns = self.get_key(i[i.find('{')+1:i.find('}')])
            value_tag = i[i.find('}')+1:]
            self.tags.append(value_ns + ':' + value_tag)

# get the key value from the namesapces            
    def get_key(self, val):
        for key, value in self.namespaces.items():
            if val == value:
                return key
# get path to the tag inside of xml file    
    def get_path(self, tag):
        for i in self.tags:
            if ':'+tag in i:
                return i
        return None
# clean the tab and return values form the text    
    def clean_text(self, text):
        #poslist = []
        r = text.replace('\t','')
        r = r.replace(' \n','\n')
        return r
                
    # def posList_to_coords(self, value):
    #     return 0
# Take required data from xml file and generate a pandas dataframe     
    def xml_to_df(self):
        d = pd.DataFrame()     
        try:
            for i in self.paths: # each parent tag
                child_id = i.xpath('./@gml:id',  namespaces = self.namespaces)
                d['gml_id'] = child_id
                for j in self.tags_columns:
                    element = i.xpath('.//'+self.get_path(j) , namespaces = xml.namespaces)
                    
                    try:                    
                        if j != 'posList' :
                            d[j] = [self.clean_text(element[0].text)]
                        else:
                            d[j] = element[0].text
                    except:
                        pass # If doesn't come any data  
                self.data = self.data.append(d, ignore_index = True)
        except:
            pass


## Class to handle shape files 
class data_shp():
    def __init__(self, file, data, dict_fields):
        self.file_path = file
        self.data = data
        self.fields = dict_fields        
        self.write_shp = sf.Writer(self.file_path)
        self.create_fields()
        self.save_data()
        self.print_data()
        self.save_xyz()
        self.save_xyz_2()
        
    def __del__(self):
        try:
            self.write_shp.close()
        except:
            pass
    # Method to create polygons    
    def create_poly(self, t):
        try:
            l = t.replace('\t','').split('\n')
            r = [x.split(' ') for x in l]            
            s = []
            for i in r:
                t = []
                for j in i[:2]: # trunc each coordinate to two first elements (x,y)
                    t.append(float(j))
                s.append(t)
            return [s]
        except:
            return False

    # Take the posList info and create fields for shape file     
    def create_fields(self):
        for i,j in self.fields.items():
            if i == 'posList':
                self.write_shp.field(i, fieldType = 'C')
            else:
                self.write_shp.field(i, fieldType = 'C')
    
    # Write data in shape file     
    def save_data(self):
        for i in self.data.iterrows():
            try:
                d = i[1].to_dict()
                self.poly = self.create_poly(d['posList'])
                if self.poly:
                    self.write_shp.record(d)
                    self.write_shp.poly(self.create_poly(d['posList']))
            except:
                pass
                print('Error in id : ' + d['gml_id'])
        self.write_shp.close()
    # Print in the console the data inside the shapefile    
    def print_data(self):
        with sf.Reader(self.file_path) as shp:            
            print(shp.bbox)
            
# Clean text extracted. Tab, spaces, new line jumps, nan    
    def clean_text(self, text):
        r = str(text).replace('\t','')
        r = r.replace(' \n','|')
        r = r.replace('\n','|')
        r = r.replace('|','\n')
        r = r.replace('nan','')
        return r if r != '\n' else '' 
# Save all information extracted in a .txt file     
    def save_xyz(self):
        #print(len(self.fields))
        with open('.//datos100.txt','w') as f:
            for i in self.data.iterrows():
                dic = i[1].to_dict()
                print(i)
                for key, value in dic.items():
                    if len(key) > 0:                       
                        f.write(self.clean_text(key)+'='+self.clean_text(value) +'\n' )
# Save the information selected from the target_tag to a .txt file
    def save_xyz_2(self):
        li = ['gml_id', 'upperLimit', 'lowerLimit','posList']   # Child tags that are required to get info for the .txt file
        with open('.//datos100b.xyz','w') as f:
            for i in self.data.iterrows():
                dic = i[1].to_dict()
                for key, value in dic.items():
                    if key in li:                       
                        f.write(self.clean_text(key)+'='+self.clean_text(value) +'\n' )
                f.write('\n')
    