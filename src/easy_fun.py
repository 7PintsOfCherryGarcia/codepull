import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go

COLORS = ['rgba(0,0,0,.7)',
          'rgba(255,0,0,.7)',
          'rgba(200,0,255,.7)',
          'rgba(0,0,255,.7)',
          'rgba(255,122,27,.7)',
          'rgba(43,244,255,.7)',
          'rgba(0,156,29,.7)',
          'rgba(0,0,0,.7)']


def easy_loadtable(infilename):
    infile = open(infilename, "r")
    indata = []
    for line in infile:
        dataline = line.rstrip().split('\t')
        data = [float(i) for i in dataline[1:]]
        indata.append(data)
    return np.array(indata)



def easy_loadmetadata(infilename):
    infile = open(infilename, "r")
    indata = []
    for line in infile:
        dataline = line.rstrip().split('\t')
        indata.append(dataline)
    return indata



def easy_scatter(dim1, dim2, metadata, colnum, bname):
    data = []
    colidx = 0
    datadict = {}
    coloridx = []
    colidx = 0
    for label in [i[colnum] for i in metadata]:
        if label not in datadict:
            datadict[label] = COLORS[colidx]
            colidx += 1
            if (colidx == len(COLORS)):
                colidx = 0
            coloridx.append(datadict[label])
        else:
            coloridx.append(datadict[label])

    trace = go.Scattergl(x=dim1,
                         y=dim2,
                        mode='markers',
                        text=[i[colnum] for i in metadata],
                        marker=dict(size=30,
                                    color=coloridx),
                        )
    data.append(trace)
    layout = go.Layout(title="",
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       font=dict(size=15, family='arial'),
                       showlegend=True,
                       titlefont=dict(size=15,
                                      family='arial'),
                       margin=dict(b=100,
                                   t=100,
                                   l=100,
                                   r=100),
                       xaxis=dict(title='',
                                  tickfont=dict(size=15)),
                       yaxis=dict(title='',
                                  tickfont=dict(size=15)),
                       )

    fig = go.Figure(data=data, layout=layout)

    plot(fig,
         filename=bname + ".html",
         image='svg',
         image_width=1600,
         image_height=1600,
         output_type='file',
         auto_open=False)
