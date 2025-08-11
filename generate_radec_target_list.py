import numpy as np
import matplotlib.pyplot as plt

import astropy.units as u
from astropy.coordinates import SkyCoord

pathOut = "./output/radec_target_lists/"

# Create longitudes: 0, +5, -5, +10, -10, ..., +175, -175, +180
step = 5 # [deg]
max_offset = 180  # [deg]
offsets = []
for i in range(0, max_offset + 1, step):
    if i == 0 or i == 180:
        offsets.append(i)
    else:
        offsets.extend([i, -i])

# Wrap into [-180, +180) for plotting / continuity
Lon = np.array([(o + 180) % 360 - 180 for o in offsets])
Lat = np.zeros_like(Lon)

# Galactic coordinates
galCoord = SkyCoord(l=Lon * u.degree, b=Lat * u.degree, frame='galactic')

# Convert to equatorial coordinates
equaCoord = galCoord.icrs

# Save coordinates
l_wrapped = (galCoord.l.wrap_at(180 * u.deg)).deg  # get longitudes in [-180, 180)
data = np.column_stack((l_wrapped, galCoord.b.deg, equaCoord.ra.deg, equaCoord.dec.deg))
header = "Galactic coordinates and corresponding Equatorial coordinates\n"
header += "longitude l [deg], latitude b [deg], RA [deg], Dec [deg]"
np.savetxt(pathOut + "lb_radec_list_centered.txt", data, fmt='%1.5f', header=header)
