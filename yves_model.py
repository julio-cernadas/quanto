import numpy as np 
from pylab import plt, mpl

plt.style.use('seaborn')
mpl.rcParams["font.family"] = "serif"

def f(x):
    return np.sin(x) + 0.5 * x

def create_plot(x,y,styles,labels,axlabels):
    plt.figure(figsize=(10,6))
    for i in range(len(x)):
        plt.plot(x[i],y[i],styles[i],label=labels[i])
        plt.xlabel(axlabels[0])
        plt.ylabel(axlabels[1])
    plt.legend(loc=0)

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)

create_plot([x],[f(x)],['b'],['f(x)'],['x', 'f(x)'])
plt.show()

