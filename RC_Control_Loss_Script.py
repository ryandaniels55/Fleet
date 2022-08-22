#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:53:13 2022

@author: ryan
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

recentFlightLogID = '8QMMR9'

os.chdir('/home/ryan/Code/Fleet/csv/8QMMR9/')

vehiclestatus0 = recentFlightLogID+'_vehicle_status_0.csv'
# vehiclestatusdata = output+'/'+vehiclestatus0

vsdata = pd.read_csv(vehiclestatus0)

RC_control_loss = vsdata.loc[vsdata['rc_signal_lost'] == 1]

if RC_control_loss.empty:
    
    print('No loss of RC control detected')
    
if RC_control_loss.empty != True:
    
    print('RC controll loss detected')