#!/usr/bin/env python
# 
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr
from instruments import VNX_Lab_Brick

class VNXLabBrick(gr.sync_block):
    """
    This block for exclsive control of the attenuation 
    of the Vaunix RF Digital Attenuator, model LDA-102.
    It currently has a dummy float input to conform with 
    the gnuradio requirement that a sync block must have at
    least one input or one output. Just attach a constant
    float source and a throttle to this input. 

    """
    def __init__(self, atten=0):
        gr.sync_block.__init__(self,
            name="VNXLabBrick",
            in_sig=[np.float32],
            out_sig=None)
        self.vnx = VNX_Lab_Brick.VNXDigitalAttenuator()
        self.vnx.connect()
        self.vnx.setAttenuation(atten)
        self.currentAttenSetting = atten


    def work(self, input_items, output_items):
        num_input_items = len(input_items[0])
        in0 = input_items[0]
        
        
        return num_input_items

    def set_atten(self,atten):
        self.vnx.setAttenuation(atten)
        self.currentAttenSetting = atten

