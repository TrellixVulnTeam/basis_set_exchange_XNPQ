"""
Tests for the BSE main API
"""

import bse
from bse import lut
import pytest
import random
from common_testvars import *

# Use random for getting sets of elements
random.seed(rand_seed, version=2)

@pytest.mark.slow
@pytest.mark.parametrize('basis_name', bs_names)
@pytest.mark.parametrize('fmt', bs_formats)
@pytest.mark.parametrize('unc_gen', true_false)
@pytest.mark.parametrize('unc_seg', true_false)
@pytest.mark.parametrize('unc_spdf', true_false)
@pytest.mark.parametrize('opt_gen', true_false)
def test_slow_get_basis_1(basis_name, fmt, unc_gen, unc_seg, unc_spdf, opt_gen):
    '''Tests getting all basis sets in all formats
       and with every combination of option

       Also tests memoization
    '''

    this_metadata = bs_metadata[basis_name]
    for ver in this_metadata['versions'].keys():
        bs1 = bse.get_basis(basis_name, fmt=fmt, version=ver,
                            uncontract_general=unc_gen,
                            uncontract_segmented=unc_seg,
                            uncontract_spdf=unc_spdf,
                            optimize_general=opt_gen)

        bs2 = bse.get_basis(basis_name, fmt=fmt, version=ver,
                            uncontract_general=unc_gen,
                            uncontract_segmented=unc_seg,
                            uncontract_spdf=unc_spdf,
                            optimize_general=opt_gen)

        assert bs1 == bs2
