import yaml
import numpy as np
import matplotlib.pyplot as plt

def main():
    CONFIG =  yaml.load(open('config_global.yaml', 'rU'))
    data  = np.genfromtxt('%s/data.txt' % CONFIG['build']['draw_data'], delimiter=",")

    plt.hist(data)
    plt.savefig('%s/plot.eps' % CONFIG['build']['plot'])

main()
