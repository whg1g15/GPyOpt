# Copyright (c) 2016, the GPyOpt Authors
# Licensed under the BSD 3-clause license (see LICENSE.txt)

from .base import EvaluatorBase

class Target(EvaluatorBase):
    """
    Class for standard Sequential Bayesian optimization methods.

    :param acquisition: acquisition function to be used to compute the batch.
    :param batch size: it is 1 by default since this class is only used for sequential methods.
    """

    def __init__(self, acquisition, batch_size=1, other_model=None):
        super(Target, self).__init__(acquisition, batch_size)
        self.other_model = other_model

    def compute_batch(self):
        """
        Selects the new location to evaluate the objective.
        """
        return self.other_model.X[-1]


