from ligotools import readligo as rl

def example_0():
  fn_H1 = "H-H1_LOSC_4_V2-1126259446-32.hdf5"
  strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')