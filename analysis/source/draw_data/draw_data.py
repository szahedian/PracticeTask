import yaml
import numpy as np
from random import gauss

def main():
    mean = [0, 0]
    cov = [[1, 0], [0, 1]]
    size = int(1e4)
    samples = np.random.multivariate_normal(mean=mean, cov=cov, size=size)

    CONFIG = yaml.load(open('config_global.yaml', 'rU'))
    np.savetxt("%s/data.txt" % CONFIG['build']['draw_data'], samples, delimiter=",")

main()