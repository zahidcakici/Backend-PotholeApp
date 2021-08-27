# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:27:40 2021

@author: zahid
"""

import pandas as pd
import numpy as np
import os


class LoadData(object):
    
    def __init__(self):
        pass
    
    def loadData(self,folder='plain_road'):
        
        try:
            path = "../data/" + folder+ "/"
            os.chdir(path)
        except Exception as e:
            if e:
                path = "./data/" + folder + "/"
                os.chdir(path)
        print(path)
        
        files = os.listdir()
        files = sorted(files)
        
        print(files)
        
        df = pd.DataFrame(columns=["Timestamp","Gx","Gy","Gz","Ax","Ay","Az","Lat","Long","Vertical"])
        for i in files:
            file = pd.read_csv(i)
            df = pd.concat([df,file])
        
        df["Time"] = np.arange(0.,df.shape[0]/1000,0.001)
        
        try:
            os.chdir("../../LoadData/")
        except Exception as e:
            if e:
                os.chdir("../../")
        return df
        







