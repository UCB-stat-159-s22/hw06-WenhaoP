import matplotlib
matplotlib.use('Agg')
from ligotools.utils import *
from ligotools import readligo as rl
from scipy.interpolate import interp1d
import matplotlib.mlab as mlab
from os.path import exists

eventname = 'GW150914' 
tests_path = "ligotools/ligotools/tests/"

def test_whiten(): 
  strain_H1 = np.load(tests_path + 'strain_H1.npy')
  strain_H1_whiten = np.load(tests_path + 'strain_H1_whiten.npy')
  fs = 4096
  dt = 0.000244140625
  Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = 4*fs)
  psd_H1 = interp1d(freqs, Pxx_H1)
  
  out = whiten(strain_H1,psd_H1,dt)
  
  assert np.array_equal(out, strain_H1_whiten)
  
def test_write_wavefile():
  fs = 4096
  strain_H1_whitenbp = np.load(tests_path + 'strain_H1_whitenbp.npy')
  indxd_0 = np.load(tests_path + 'indxd_0.npy')
  write_wavfile(tests_path + eventname+ "_H1_whitenbp.wav", int(fs), strain_H1_whitenbp[(indxd_0, )])
  assert exists(tests_path + eventname+ "_H1_whitenbp.wav")

def test_reqshift():
  fs = 4096
  fshift = 400.
  strain_H1_whitenbp = np.load(tests_path + 'strain_H1_whitenbp.npy')
  strain_H1_shifted = np.load(tests_path + 'strain_H1_shifted.npy')
  out = reqshift(strain_H1_whitenbp,fshift=fshift,sample_rate=fs)
  assert np.array_equal(out, strain_H1_shifted)
  
def test_plot_changes():
  time = np.load(tests_path + 'time.npy')
  SNR = np.load(tests_path + 'SNR.npy')
  strain_whitenbp = np.load(tests_path + 'strain_whitenbp.npy')
  template_match = np.load(tests_path + 'template_match.npy')
  template_fft = np.load(tests_path + 'template_fft.npy')
  datafreq = np.load(tests_path + 'datafreq.npy')
  d_eff = np.load(tests_path + 'd_eff.npy')
  freqs = np.load(tests_path + 'freqs.npy')
  data_psd = np.load(tests_path + 'data_psd.npy')
  
  plot_changes(time, 1126259462.432373, SNR, 'g', 'L1', eventname, 'png', 1126259462.44,
                     strain_whitenbp, template_match, template_fft, datafreq,
                     999.743130306333, freqs, data_psd, 4096)
  assert exists('figures/' + eventname + '_L1_matchfreq.png')
  assert exists('figures/' + eventname + '_L1_matchtime.png')
  assert exists('figures/' + eventname + '_L1_SNR.png')

  