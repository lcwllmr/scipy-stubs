<h1 align="center">scipy-stubs</h1>

<p align="center">
    Precise type hints for <i>all</i> of <a href="https://github.com/scipy/scipy">SciPy</a>.
</p>

<p align="center">
    <a href="https://pypi.org/project/scipy-stubs/">
        <img
            alt="scipy-stubs - PyPI"
            src="https://img.shields.io/pypi/v/scipy-stubs?style=flat&color=olive"
        />
    </a>
    <a href="https://anaconda.org/conda-forge/scipy-stubs">
        <img
            alt="scipy-stubs - conda-forge"
            src="https://anaconda.org/conda-forge/scipy-stubs/badges/version.svg"
        />
    </a>
    <a href="https://github.com/scipy/scipy-stubs">
        <img
            alt="scipy-stubs - Python Versions"
            src="https://img.shields.io/pypi/pyversions/scipy-stubs?style=flat"
        />
    </a>
    <a href="https://github.com/scipy/scipy-stubs">
        <img
            alt="scipy-stubs - license"
            src="https://img.shields.io/github/license/scipy/scipy-stubs?style=flat"
        />
    </a>
</p>
<p align="center">
    <a href="https://github.com/scipy/scipy-stubs/actions?query=workflow%3ACI">
        <img
            alt="scipy-stubs - CI"
            src="https://github.com/scipy/scipy-stubs/workflows/CI/badge.svg"
        />
    </a>
    <a href="https://github.com/scipy/scipy-stubs">
        <img
            alt="scipy-stubs - typed"
            src="https://img.shields.io/pypi/types/scipy-stubs?color=blue&style=flat"
        />
    </a>
    <a href="https://github.com/python/mypy">
        <img
            alt="scipy-stubs - mypy"
            src="https://www.mypy-lang.org/static/mypy_badge.svg"
        />
    </a>
    <a href="https://github.com/microsoft/pyright">
        <img
            alt="scipy-stubs - pyright"
            src="https://microsoft.github.io/pyright/img/pyright_badge.svg"
        />
    </a>
    <a href="https://detachhead.github.io/basedpyright">
        <img
            alt="scipy-stubs - basedpyright"
            src="https://img.shields.io/badge/basedpyright-checked-42b983"
        />
    </a>
    <a href="https://github.com/astral-sh/ruff">
        <img
            alt="scipy-stubs - ruff"
            src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"
        />
    </a>
</p>

______________________________________________________________________

## Highlights

- Works out-of-the-box
  - all that's needed is to [install `scipy-stubs`](#installation)
  - does not require a `mypy` plugin or other configuration
  - available on [PyPI](https://pypi.org/project/scipy-stubs/) and [conda-forge](https://anaconda.org/conda-forge/scipy-stubs)
- Improves IDE suggestions and autocompletion
  - ... even if you don't use static typing in your code
  - no additional plugins required
- 0% runtime overhead
  - not even a single import is required
- 100% coverage of the [public SciPy API](https://docs.scipy.org/doc/scipy/reference/index.html)
  - also covers most of the private API
- Precise type-hinting of dtypes and [shape-types](https://github.com/numpy/numpy/issues/16544)
  - works with all "array-likes" and "dtype-likes"
  - many of the functions that return an array are *shape-typed*
  - shape-typing is optional: all functions still accept arrays with unknown shape-type
- Type-checker agnostic
  - works with at least [`mypy`](https://github.com/python/mypy),
    [`pyright`](https://github.com/DetachHead/basedpyright)/pylance and [`ruff`](https://github.com/astral-sh/ruff)
  - ... even in the strict mode
  - compatible with the [Python Typing Spec](https://typing.readthedocs.io/en/latest/spec/index.html)
- [SPEC 0](https://scientific-python.org/specs/spec-0000/) compliant
  - Supports Python ≥ 3.11
  - Supports NumPy ≥ 1.25.2

<!-- NOTE: SciPy permalinks to the following `#installation` anchor; don't modify it! -->

## Installation

The source code is currently hosted on GitHub at [github.com/scipy/scipy-stubs](https://github.com/scipy/scipy-stubs/).

Binary distributions are available at the [Python Package Index (PyPI)](https://pypi.org/project/scipy-stubs/) and on
[conda-forge](https://anaconda.org/conda-forge/scipy-stubs).

### Using pip (PyPI)

To install from the [PyPI](https://pypi.org/project/scipy-stubs/), run:

```bash
pip install scipy-stubs
```

In case you haven't installed `scipy` yet, both can be installed with:

```bash
pip install scipy-stubs[scipy]
```

### Using conda (conda-forge)

To install using Conda from the [conda-forge channel](https://anaconda.org/conda-forge/scipy-stubs), run:

```bash
conda install conda-forge::scipy-stubs
```

It's also possible to install both `scipy` and `scipy-stubs` together through the bundled
[`scipy-typed`](https://anaconda.org/conda-forge/scipy-typed) package:

```bash
conda install conda-forge::scipy-typed
```

### Packages overview

<table>
  <tr>
    <th rowspan="2" colspan="2"></th>
    <th colspan="2">Python packages</th>
  </tr>
  <tr>
    <th><code>scipy-stubs</code></th>
    <th><code>scipy</code> + <code>scipy-stubs</code></td>
  </tr>
  <tr>
    <th>PyPI</th>
    <th align="right"><code>pip install {}</code></th>
    <td><code>scipy-stubs</code></td>
    <td><code>scipy-stubs[scipy]</code></td>
  </tr>
  <tr>
    <th>conda-forge</th>
    <th align="right"><code>conda install conda-forge::{}</code></th>
    <td><code>scipy-stubs</code></td>
    <td><code>scipy-typed</code></td>
  </tr>
</table>

## Versioning and requirements

The versioning scheme of `scipy-stubs` includes the compatible `scipy` version as `{scipy_version}.{stubs_version}`.
Even though `scipy-stubs` doesn't enforce an upper bound on the `scipy` version, later `scipy` versions aren't guaranteed to be
fully compatible.

There are no additional restrictions enforced by `scipy-stubs` on the `numpy` requirements.
For `scipy-stubs==1.16.*` that is `numpy >= 1.25.2`.

Currently, `scipy-stubs` has one required dependency: [`optype`](https://github.com/jorenham/optype).
This is essential for `scipy-stubs` to work properly, as it relies heavily on it for annotating (shaped) array-likes,
scalar-likes, shape-typing in general, and much more.
At the moment, `scipy-stubs` requires the latest version `optype`.

The exact version requirements are specified in the [`pyproject.toml`](pyproject.toml).

## Supported static type-checkers

- [`basedpyright`](https://github.com/DetachHead/basedpyright)
- [`pyright`](https://pyright.readthedocs.io/en/latest/index.html)
- [`mypy`](https://mypy.readthedocs.io/en/stable/index.html)

For validation and testing, `scipy-stubs` primarily uses [`mypy`](https://github.com/python/mypy)
and [`basedpyright`](https://github.com/DetachHead/basedpyright) (a backwards-compatible `pyright` fork).

## `scipy` coverage

The entire public API of `scipy` is **fully annotated** and **verifiably valid**.
For the most part, this can also be said about `scipy`'s private API and other internal machinery.

Note that this does not mean that all annotations are optimal, and some might even be incorrect. If you encounter this, it would
help a lot if you could open an issue or a PR for it.

## Contributing

There are many ways that you can help improve `scipy-stubs`, for example

- reporting issues, bugs, or other unexpected outcomes
- improving the `.pyi` stubs (see [CONTRIBUTING.md](https://github.com/scipy/scipy-stubs/blob/master/CONTRIBUTING.md))
- type-testing (see the `README.md` in [`scipy-stubs/tests`](https://github.com/scipy/scipy-stubs/tree/master/tests) for the
  specifics)
- write new documentation (usage examples, guides, tips & tricks, FAQ, etc.), or e.g. improve this `README.md`
- help spread the word on `scipy-stubs`, so that more can benefit from using it
