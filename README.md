# sPHENIX_trackDisplay
Diagnostic display for the sPHENIX tracker. Plots all clusters, and draws simple tracks by "connecting the dots" between clusters associated with the same track ID.

Requires `uproot` and `matplotlib` (both can be easily installed with `pip`).

Usage:

`python trackDisplay.py <input ROOT file>`

The input ROOT file is the output of `SvtxEvaluator`. It must contain `ntp_cluster`.
