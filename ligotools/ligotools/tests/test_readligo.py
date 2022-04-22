from ligotools import readligo as rl
import os

def test_loaddata_H1():
  fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
  strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
  assert (strain_H1 is not None) & (time_H1 is not None) & (chan_dict_H1 is not None)

def test_loaddata_L1():
  fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
  strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
  assert (strain_L1 is not None) & (time_L1 is not None) & (chan_dict_L1 is not None)
  
def test_read_hdf5_H1():
  filename = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
  strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(filename)

  assert (strain is not None) & (gpsStart is not None) & (ts is not None) & (shortnameList is not None) & (qmask is not None) & (injmask is not None) & (injnameList is not None) 

def test_read_hdf5_L1():
  filename = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
  strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(filename)

  assert (strain is not None) & (gpsStart is not None) & (ts is not None) & (shortnameList is not None) & (qmask is not None) & (injmask is not None) & (injnameList is not None) 
