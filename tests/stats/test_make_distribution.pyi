from typing import Literal

import numpy as np

from scipy.stats import distributions, make_distribution
from scipy.stats._distribution_infrastructure import ContinuousDistribution

LogUniform: type[ContinuousDistribution] = make_distribution(distributions.loguniform)

class _DuckRV:
    @property
    def __make_distribution_version__(self) -> Literal["1.16.0"]: ...
    @property
    def parameters(self) -> dict[str, tuple[float, float]]: ...
    @property
    def support(self) -> tuple[float, float]: ...
    def pdf(self, x: float, /, *, quack: float) -> float: ...

class _MultiDuckRV:
    @property
    def __make_distribution_version__(self) -> Literal["1.16.0"]: ...
    @property
    def parameters(self) -> tuple[dict[str, tuple[float, float]], dict[str, tuple[float, float]]]: ...
    def process_parameters(self, quack: float | None = None, swim: float | None = None) -> dict[str, float]: ...
    @property
    def support(self) -> dict[str, tuple[float, float]]: ...
    def pdf(self, x: float, /, *, quack: float, swim: float) -> np.float64: ...

DuckRV: type[ContinuousDistribution] = make_distribution(_DuckRV)
MultiDuckRV: type[ContinuousDistribution] = make_distribution(_MultiDuckRV)
