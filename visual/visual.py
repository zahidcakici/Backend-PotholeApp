# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:02:03 2021

@author: zahid
"""

from plotly import subplots as sbp
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objs as go

class Graph(object):
    
    def __init__(self):
        pass
    
    def plot(self,df):
        
        t = df["Time"]
        gx,gy,gz = df['Gx'],df['Gy'],df['Gz']
        ax,ay,az = df['Ax'],df['Ay'],df['Az']

        gx = go.Scatter(x=t,y=gx,name="gx")
        gy = go.Scatter(x=t,y=gy,name="gy")
        gz = go.Scatter(x=t,y=gz,name="gz")
        
        ax = go.Scatter(x=t,y=ax,name="ax")
        ay = go.Scatter(x=t,y=ay,name="ay")
        az = go.Scatter(x=t,y=az,name="az")

        fig1 = sbp.make_subplots(rows=3,cols=1,shared_xaxes=True)
        fig2 = sbp.make_subplots(rows=3,cols=1,shared_xaxes=True)
		
        fig1.add_trace(gx, 1, 1)
        fig1.add_trace(gy, 2, 1)
        fig1.add_trace(gz, 3, 1)
        
        fig2.add_trace(ax, 1, 1)
        fig2.add_trace(ay, 2, 1)
        fig2.add_trace(az, 3, 1)
        
        fig1['layout'].update(height=600, width=800,
						 title='Gyroscope data plot')
        
        fig2['layout'].update(height=600, width=800,
						 title='Accelrometer data plot')
        return (fig1,fig2)

