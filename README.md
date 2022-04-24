# Fine-tuning reproduciblity of LIGO Black Hole signal tutorial, Part II

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s22/hw06-WenhaoP/HEAD?labpath=main.ipynb)

**Note:** This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Spring 2022 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science_](https://ucb-stat-159-s22.github.io). Authorship of the original analysis code rests with the LIGO collaboration.

## Installation

To create and activate the conda environment, in the root directory, run

```
mamba env create -f environment.yml -p ~/envs/ligo
conda activate ligo
```

The command above will automatically install the `ligotools` local package in the same environment. 

To separately install the `ligotools` package, in the root directory, run

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

We can a jupyter book of this repository. First in the `ligo` conda environment, run

```
jupyter-book config sphinx .
sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
```

to build the notebook. To access the jupyter book on the hub, go into `_build/html/` and run

```
python -m http.server
```
in the `base` environment. Then, access the [link](https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html) to read the jupyter book.

## GitHub Pages

The GitHub page of this repo can be visited [here](https://ucb-stat-159-s22.github.io/hw06-WenhaoP/)

## Makefile

There are following makefile commands available:

- `env`: create and configure the environment.
- `remove-env`: remove the configured environment.
- `html`: build the JupyterBook normally (calling `jupyterbook build .`). Note this build can only be viewed if the repo is cloned locally, or with the VNC desktop on the hub.
- `html-hub`: build the JupyterBook so that you can view it on the hub with the URL proxy trick as indicated above.
- `clean`: clean up the `figures`, `audio`  and `_build` folders.
- `run-main`: execute the jupyter notebook `main.ipynb`.
