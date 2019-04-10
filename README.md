# AMES - House Prices: Advanced Regression Techniques

This repository contains tests of the [AlignmentRepaPy repository](https://github.com/caiks/AlignmentRepaPy) using data from the [Ames Housing dataset](http://jse.amstat.org/v19n3/decock.pdf) compiled by Dean De Cock. Full details of the dataset are in [Kaggle Data Set - House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data). The AlignmentRepaPy repository is a fast Haskell implementation of some of the *practicable inducers* described in the paper *The Theory and Practice of Induction by Alignment* at https://greenlake.co.uk/. 

## Documentation

There is an analysis of this dataset [here](https://greenlake.co.uk/pages/dataset_python_AMES), with sections (a) [predicting sale price without modelling](https://greenlake.co.uk/pages/dataset_python_AMES#Predicting_sale_price_without_modelling) and (b) [induced modelling of sale price](https://greenlake.co.uk/pages/dataset_python_AMES#Induced_modelling_of_sale_price). 

## Installation

The `AMES` executables require the `AlignmentRepaPy` module which is in the [AlignmentRepaPy repository](https://github.com/caiks/AlignmentRepaPy). See the AlignmentRepaPy repository for installation instructions of the Python compiler and libraries.

Then download the zip files or use git to get the `MUSHPy` repository and the underlying `AlignmentPy` and `AlignmentRepaPy` repositories -
```sh
cd
git clone https://github.com/caiks/AlignmentPy.git
git clone https://github.com/caiks/AlignmentRepaPy.git
git clone https://github.com/caiks/AMESPy.git
```

## Usage

To experiment with the dataset in the interpreter,
```sh
cd AMESPy
export PYTHONPATH=../AlignmentPy:../AlignmentRepaPy
python3
```
```py
from AMESDev import *

(uu,aa) = amesIO()
vv = uvars(uu)
vvl = sset([VarStr("edible")])
vvk = vv - vvl

hr = aahr(uu,aa)

(wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed) = ((9*9*10), 8, (9*9*10), 10, (10*3), 3, (9*9*10), 1, 3, 3, 5)

(uu1,df1) = decomperIO(uu,vvk,hr,wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed)

open("df.json","w").write(decompFudsPersistentsEncode(decompFudsPersistent(df1)))

summation(mult,seed,uu1,df1,hr)
(61302.44944051167, 26729.333546815153)
```
The *practicable model induction* is described [here](https://greenlake.co.uk/pages/dataset_python_AMES_model).
