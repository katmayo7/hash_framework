from hash_framework.kernels.abstract import Kernel
from hash_framework.kernels.families import Families
from hash_framework.kernels.neighborhood import Neighborhood
from hash_framework.kernels.zeros import Zeros
from hash_framework.kernels.ones import Ones
from hash_framework.kernels.ascii import ASCII
from hash_framework.kernels.multicollision import Multicollision
from hash_framework.kernels.minimal import Minimal
from hash_framework.kernels.sha3margins import SHA3Margins
from hash_framework.kernels.sha3differences import SHA3Differences
from hash_framework.kernels.test import Test

all_kernels = {
    'abstract': Kernel,
    'families': Families,
    'neighborhood': Neighborhood,
    'zeros': Zeros,
    'ones': Ones,
    'ascii': ASCII,
    'multicollision': Multicollision,
    'minimal': Minimal,
    'test': Test,
    'sha3margins': SHA3Margins,
    'sha3differences': SHA3Differences
}

def lookup(name):
    return all_kernels[name]
