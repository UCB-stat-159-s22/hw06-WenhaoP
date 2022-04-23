# Fine-tuning reproduciblity of LIGO Black Hole signal tutorial, Part II

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s22/hw06-WenhaoP/HEAD?labpath=main.ipynb)

**Note:** This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Spring 2022 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science_](https://ucb-stat-159-s22.github.io). Authorship of the original analysis code rests with the LIGO collaboration.

## Installation

To create the conda environment, in the root directory, run

```
mamba env create -f environment.yml -p ~/envs/ligo
```

The command above will automatically install the `ligotools` local package. To separately install the `ligotools` package, in the root directory, run

```
pip install ligotools/.
```

To test the installed `ligotools` package, run

```
pytest ligotools
```

or equivalently but with more details

```
pytest -vv ligotools
```

## Jupyter book

We have a jupyter book of this repository. To access the jupyter book on the hub, go into `ligobook/_build/html/` and run

```
python -m SimpleHTTPServer 8000
```

in the `ligo` conda environment.

Then, open the [link](https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html).