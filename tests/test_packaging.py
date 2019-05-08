""" Validate what's available directly on the top-level import. """

import pytest
import veracitools

__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"


@pytest.mark.parametrize(
    ["obj_name", "typecheck"],
    [("ExpectContext", lambda obj: callable(obj) and isinstance(obj, type))])
def test_top_level_exports(obj_name, typecheck):
    """ At package level, validate object availability and type. """
    mod = veracitools
    try:
        obj = getattr(mod, obj_name)
    except AttributeError:
        pytest.fail("Unavailable on {}: {}".format(mod.__name__, obj_name))
    else:
        assert typecheck(obj)
