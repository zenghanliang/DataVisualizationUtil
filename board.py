# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 17:12:31 2018

@author: liang
"""

import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge, factor_cmap

output_file("periodic.html", mode="inline")

x_coordinate = ["1", "2", "3", "4", "5"]
y_coordinate = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

cmap = {
    "black"   : "#111111",
    "lblack"  : "#333333",
    "orange"  : "#ffcc00",
    "dorange" : "#ff3300",
    "green"   : "#009900",
    "blue"    : "#00ffff",
    "red"     : "#ff2222",
    "white"   : "#ffffff",
}

df = pd.DataFrame({
        'x_coordinate':[
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
                "1", "2", "3", "4", "5", 
            ],
        'y_coordinate':[
                "1", "1", "1", "1", "1", 
                "2", "2", "2", "2", "2", 
                "3", "3", "3", "3", "3", 
                "4", "4", "4", "4", "4", 
                "5", "5", "5", "5", "5", 
                "6", "6", "6", "6", "6", 
                "7", "7", "7", "7", "7", 
                "8", "8", "8", "8", "8", 
                "9", "9", "9", "9", "9", 
                "10", "10", "10", "10", "10", 
                "11", "11", "11", "11", "11", 
                "12", "12", "12", "12", "12", 
                "13", "13", "13", "13", "13", 
                "14", "14", "14", "14", "14", 
            ],
        'val':[
               "askAccum", "ask", "price", "bid", "bidAccum", 
               "", "0", "MARKET", "0", "", 
               "411110", "300000", "OVER", "", "", 
               "111110", "100000", "945.5", "", "", 
               "11110", "10000", "945.4", "", "", 
               "1110", "1000", "945.3", "", "", 
               "110", "100", "945.2", "", "", 
               "10", "10", "945.1", "", "", 
               "", "", "945.0", "20", "20", 
               "", "", "944.9", "200", "220", 
               "", "", "944.8", "2000", "2220", 
               "", "", "944.7", "20000", "22220", 
               "", "", "944.6", "200000", "222220", 
               "", "", "UNDER", "400000", "622220", 
               ],
        'color':[
               cmap["white"], cmap["white"], cmap["white"], cmap["white"], cmap["white"], 
               cmap["blue"], cmap["blue"], cmap["green"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["dorange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["orange"], cmap["red"], cmap["red"],
               cmap["blue"], cmap["blue"], cmap["dorange"], cmap["red"], cmap["red"],
               ],
        'backcolor':[
               cmap["black"], cmap["black"], cmap["black"], cmap["black"], cmap["black"],
               cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"],
               cmap["black"], cmap["black"], cmap["black"], cmap["black"], cmap["black"],
               cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"],
               cmap["black"], cmap["black"], cmap["black"], cmap["black"], cmap["black"],
               cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"],
               cmap["black"], cmap["black"], cmap["black"], cmap["black"], cmap["black"],
               cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"],
               cmap["black"], cmap["black"], cmap["black"], cmap["black"], cmap["black"],
               cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"],
               cmap["black"], cmap["black"], cmap["black"], cmap["black"], cmap["black"],
               cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"],
               cmap["black"], cmap["black"], cmap["black"], cmap["black"], cmap["black"],
               cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"], cmap["lblack"],
               ]
        })

source = ColumnDataSource(df)

p = figure(title="XXXX.T TYO @ yyyy/mm/dd HH:MM:SS.ssssss", plot_width=600, plot_height=450,
           tools="", toolbar_location=None, x_range=x_coordinate, y_range=list(reversed(y_coordinate)))

p.rect("x_coordinate", "y_coordinate", 1.00, 1.00, source=source, fill_alpha=0.8, 
       line_color=cmap["white"], fill_color="backcolor")

text_props = {"source": source, "text_align": "right", "text_baseline": "middle", "x_offset": 50}

r = p.text(x="x_coordinate", y="y_coordinate", text="val", text_color="color", **text_props)
r.glyph.text_font_style="bold"

p.outline_line_color = None
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_standoff = 0
#p.legend.orientation = "horizontal"
#p.legend.location ="top_center"

show(p)