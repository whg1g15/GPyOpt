# Copyright (c) 2016, the GPyOpt Authors
# Licensed under the BSD 3-clause license (see LICENSE.txt)

from .base import EvaluatorBase
from .sequential import Sequential
from .batch_random import RandomBatch
from .batch_predictive import Predictive
from .batch_local_penalization import LocalPenalization
from .adversarial import Adversarial
from .target import Target

def select_evaluator(name):
    if name == 'sequential':
        return Sequential
    elif name == 'random':
        return RandomBatch
    elif name == 'predictive':
        return Predictive
    elif name == 'local_penalization':
        return LocalPenalization
    elif name == 'adversarial':
        return Adversarial
    elif name == 'target':
        return Target
    else:
        raise Exception('Invalid acquisition evaluator selected.')
