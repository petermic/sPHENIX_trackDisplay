# sPHENIX_trackDisplay
Diagnostic display for the sPHENIX tracker. Plots all clusters, and draws simple tracks by "connecting the dots" between clusters associated with the same track ID. (This is mainly useful for checking that the seeding algorithm is doing something sensible in the TPC; tracks projected into the INTT and MVTX are not the right shape in the gaps between subdetectors, though they do contain the correct clusters.)

Requires `uproot` and `matplotlib` (both can be easily installed with `pip`).

Usage:

`python trackDisplay.py <input ROOT file>`

The input ROOT file is the output of `SvtxEvaluator`. It must contain `ntp_cluster`.
