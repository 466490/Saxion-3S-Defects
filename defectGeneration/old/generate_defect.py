import numpy as np
import pandas as pd
from svgpathtools import *
import random


def length(layer,comp_, line_=0):

    line_start_real = layer[comp_][line_].start.real
    line_start_imag = layer[comp_][line_].start.imag

    line_end_real = layer[comp_][line_].end.real
    line_end_imag = layer[comp_][line_].end.imag

    x_len = abs(line_start_real - line_end_real)
    y_len = abs(line_start_imag - line_end_imag)

    return (x_len, y_len)

def direction(layer, comp_, line_=0):
    S = layer[comp_][line_].start
    E = layer[comp_][line_].end

    epsilon = 1e-7 # to avoid division by 0

    real_part = (S-E).real # S - start, E - end
    imag_part = (S-E).imag

    x = round(real_part/abs(real_part + epsilon), 2)
    y = round(imag_part/abs(imag_part + epsilon), 2)

    return x, y


def missing_trace(layer, comp_, line_=0, len_per=0.05):
    xlen, ylen = length(layer,comp_, line_)
    x_direction, y_direction = direction(layer,comp_,line_)

    len_percent = len_per
    x_delta = x_direction * (xlen * len_percent) # some scalar 
    y_delta = y_direction * (ylen * len_percent) 

    line_start_real = layer[comp_][line_].start.real
    line_start_imag = layer[comp_][line_].start.imag

    line_end_real = layer[comp_][line_].end.real
    line_end_imag = layer[comp_][line_].end.imag

    min_error = 1
    y_min_error = 1

    current_line = layer[comp_][line_]

    start = complex(random.uniform(line_start_real-x_delta, line_end_real+x_delta)-min_error, \
                    (random.uniform(line_start_imag-y_delta, line_end_imag+y_delta)-y_min_error))  # Random starting point

    defect_point = complex(random.uniform(start.real, start.real-x_delta)+min_error, \
                    (random.uniform(start.imag, start.imag-y_delta)+y_min_error))

    new_line = Line(current_line.start, start)
    new_endline = Line(defect_point, current_line.end)

    return new_line, new_endline
    # based on length, introduce random error


def membrane_defect(layer, percent):
    copied_layer = layer.copy()
    random_line = random.randint(0,len(layer))
    line_start, line_end = missing_trace(layer, 0, random_line, len_per=percent)
    
    defect_size = line_start.end - line_end.start

    x_len = defect_size.real
    y_len = defect_size.imag

    val = 0

    if random.uniform(0, 1) > 0.5: # whether it goes inside or outside...
        # print('outside')
        val = 50
    else:
        # print('inside')
        val = -50
        
    control1_p = complex(random.uniform(line_start.end.real+5, line_start.end+val), \
                    (random.uniform(line_end.start.imag+5, line_end.start.imag+val)))  # control point 1

    # control2_p = complex(random.uniform(line_start.end.real-60, line_start.end+60), \
    #                 (random.uniform(line_end.start.imag-60, line_end.start.imag+60)))  # control point 2

    new_defect = CubicBezier(start=line_start.end, control1=control1_p, control2=control1_p, end=line_end.start)


    layer[0].extend(Path(line_start, line_end, new_defect))
    return paths2svg.big_bounding_box(new_defect)

def add_artefacts(max_x, max_y, min_x, min_y, R, N_polygons):
    alpha = 360/N_polygons

    rotation_matrix = np.matrix([[np.cos(alpha), -np.sin(alpha)],[np.sin(alpha), np.cos(alpha)]])

    # TODO: still..
# R is more or less the radius
