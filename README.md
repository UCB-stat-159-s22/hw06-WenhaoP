# Fine-tuning reproduciblity of LIGO Black Hole signal tutorial, Part II

** Add Binder badge and link here**

**Note:** This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Spring 2022 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science_](https://ucb-stat-159-s22.github.io). Authorship of the original analysis code rests with the LIGO collaboration.

## Installation

To create the conda environment, in the root directory, run

```
mamba env create -f environment.yml -p ~/envs/ligo
```

Then, to install the `ligotools` package, in the root directory, run

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