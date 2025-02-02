#!/usr/bin/env python

# one dimensional chain

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from pythtb_respack import * # import TB model class
import matplotlib.pyplot as plt

# specify model
lat=[[1.0]]
orb=[[0.0]]
my_model=tb_model(1,1,lat,orb,nspin=2)
my_model.set_onsite(-10., 0)
my_model.set_hop(-1., 0, 0, [1])

print(my_model._site_energies.shape)
print(my_model._hoppings.shape)