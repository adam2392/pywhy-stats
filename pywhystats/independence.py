from enum import Enum
from typing import Optional

import numpy as np

from p_value_result import PValueResult


class Methods(Enum):
    AUTO = 0


def independence_test(X: np.ndarray,
                      Y: np.ndarray,
                      condition_on: Optional[np.ndarray] = None,
                      method=Methods.AUTO,
                      **kwargs) -> PValueResult:
    """ Performs an independence test to determine whether X and Y are independent, conditioned on an optional
    set of variables. This is, test whether X _||_ Y | condition_on, where the null hypothesis is that X and Y are
    independent.

    Parameters
    ----------
    X : numpy.ndarray, shape (n, d)
        Data matrix for X.
    Y : numpy.ndarray, shape (n, m)
        Data matrix for Y.
    condition_on : numpy.ndarray or None, shape (n, k), optional
        Data matrix for the conditioning variables. If None is given, an unconditional test is performed.
    method : Methods, optional
        Independence test method from the Methods enum. Default is Methods.AUTO, which will automatically select an
        appropriate method.
    **kwargs : dict or None, optional
        Additional keyword arguments to be passed to the specific test method

    Returns
    -------
    result : PValueResult
        An instance of the PValueResult data class, containing the p-value, test statistic, and any additional
        information related to the independence test.
    """
    pass
