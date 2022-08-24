#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:53:13 2022

@author: ryan
"""
import os
from pyulog import ulog2csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def RC_control_loss(recentFlightLogID):
    
    # recentFlightLogID = 'Q6MR1S'
    
    # os.chdir('/home/ryan/Code/Fleet/csv/Q6MR1S''/')
    
    vehiclestatus0 = recentFlightLogID+'_vehicle_status_0.csv'
    # vehiclestatusdata = output+'/'+vehiclestatus0
    
    vsdata = pd.read_csv(vehiclestatus0, index_col=False)
    
    vsdata_timestamp = vsdata['timestamp']
    vsdata_seconds = (vsdata['timestamp']-vsdata['timestamp'].iloc[0])/1e6
    vsdata['timestamp'] = vsdata_seconds
    vsdata.rename(columns={'timestamp':'seconds'}, inplace = True)
    RC_control_loss = vsdata.loc[vsdata['rc_signal_lost'] == 1]
    
    if RC_control_loss.empty:
        
        print('No loss of RC control detected')
        
    if RC_control_loss.empty != True:
        
        
        vsdata_RClost = vsdata.loc[vsdata['rc_signal_lost'] == 1]
        RClost_start = vsdata_RClost.iloc[1]
        RClost_start = RClost_start['seconds']
        RClost_end = vsdata_RClost.iloc[-1,0]
        RClost_duration = vsdata_RClost.iloc[-1,0] - vsdata_RClost.iloc[1]
        RClost_duration = '{:.2f}'.format(RClost_duration['seconds'])
        
        RClost_message = 'RC control loss detected {} seconds after flight began for a duration of {} seconds'.format(RClost_start, RClost_duration)
        
        f = open(recentFlightLogID+'.txt','w+')
        
        print(RClost_message)
        
        def convertTuple(tup):
                # initialize an empty string
            str = ''
            for item in tup:
                str = str + item
            return str
        
        line1 = RClost_message
        
        line1 = convertTuple(line1)
        
        f.write(line1)
        
        f.close()
        
if __name__ == '__main__':
            
    RC_control_loss()
        
    # seconds = vsdata_RClost['seconds']
    # RClost_start = vsdata_RClost.head(1)
    # RClost_start = RClost_start['seconds']
    # RClost_start = RClost_start.astype(float)
    # RClost_duration = seconds['seconds'].tail(1)-seconds['seconds'].head(1)
    # RClost_time = vsdata_RClost.loc[vsdata_RClost.head(1),vsdata_RClost.loc['seconds']]
    # RC_lost = 'RC control loss detected {} seconds after flight began for a duration of {} seconds'.format()
    # print('RC control loss detected at vsdata_RClost.iloc[vsdata_RClost['seconds'] == 1'])
    