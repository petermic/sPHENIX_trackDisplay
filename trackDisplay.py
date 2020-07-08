import sys
import math
import uproot
import plotly.express as px
import plotly.graph_objects as go

if len(sys.argv) != 2:
    print("Usage: python trackDisplay.py <input ROOT file>")
    sys.exit()

inputfname = sys.argv[1]
print("Opening "+inputfname+"...")

inputfile = uproot.open(inputfname)
print(inputfile.keys())

"""
if "ntp_cluster" not in inputfile.keys():
    print("ERROR: Cluster data not found! Aborting.")
    sys.exit()
"""
info = inputfile["ntp_info"]
nTracks = info.array('ntrk')
print("nTracks: "+str(nTracks))

clusters = inputfile["ntp_cluster"]
cluster_x = clusters.array('x')
cluster_y = clusters.array('y')
cluster_z = clusters.array('z')
cluster_ID = clusters.array('trackID')

print("nClusters: "+str(len(cluster_ID)))

# sort cluster indices into groups with the same trackID (i.e. tracks)
IDs = []
tracks_clusterindex = []
for i,d in enumerate(cluster_ID):
    if not math.isnan(d):
        if d not in IDs:
            IDs.append(d)
            tracks_clusterindex.append([i])
        else:
            ind = IDs.index(d)
            tracks_clusterindex[ind].append(i)

# get (x,y,z) lists for each track
tracks_x = []
tracks_y = []
tracks_z = []
for track in tracks_clusterindex:
    xlist = []
    ylist = []
    zlist = []
    for ind in track:
        xlist.append(cluster_x[ind])
        ylist.append(cluster_y[ind])
        zlist.append(cluster_z[ind])
    tracks_x.append(xlist)
    tracks_y.append(ylist)
    tracks_z.append(zlist)

# plot all clusters
fig = px.scatter_3d(x=cluster_x,y=cluster_y,z=cluster_z)
fig.update_traces(marker=dict(size=1,color='black'))

# plot all tracks
for i in range(len(tracks_clusterindex)):
    fig.add_trace(go.Scatter3d(x=tracks_x[i],y=tracks_y[i],z=tracks_z[i],mode='lines',line=dict(color='green'),showlegend=False))

fig.show()