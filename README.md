Module to turn a RTL-SDR software-defined radio into a 21cm receiver,
and observe the neutral hydrogen signal from the Milky Way!
Not only can you detect the Milky Way signal, but you can identify the various spiral arms,
and measure the rotation profile via the Doppler effect.

The setup is: 
WIFI antenna --> LNA --> RTL-SDR --> mini PC running Kubuntu.

## Installing the dependencies on Kubuntu:

### rtl-sdr package

I installed the rtl-sdr command line tools:
```
sudo apt install rtl-sdr
```
Then the commands
```
rtl_test
rtl_power
```
both worked.

I was able to power on and off the LNA, via the bias T on the RTL-SDR:
To activate the bias T:
```
rtl_biast -b 1
```
To deactivate it:
```
rtl_biast -b 0
```

### pyrtlsdr python package

```
sudo apt-get install librtlsdr-dev
pip install pyrtlsdr
```
(got a warning that this version of pyrtlsdr does not provide [lib])

### rtlobs python package

This github repo is great for this application:
https://github.com/evanmayer/rtlobs .
I forked it to tweak it,
and cloned it from my github:
https://github.com/EmmanuelSchaan/rtlobs.git .
I haven't installed it: I just give its path to my python codes that use it...

### PyIndi client, to communicate with devices on INDI server in python

Thisis not needed for drift scan observations. 
I only use it to communicate with my go-to mount and camera, so that I can point at specific RA and Dec, and plate solve.
I installed the dependencies described in https://github.com/indilib/pyindi-client
```
sudo apt-add-repository ppa:mutlaqja/ppa
sudo apt-get -y install python3-indi-client
sudo apt-get install libindi-dev swig libcfitsio-dev libnova-dev
```
Then:
```
git clone https://github.com/indilib/pyindi-client.git
cd pyindi-client
python setup.py install
```
I then checked that I could import it from my conda python:
```
ipython
import PyIndi
```
