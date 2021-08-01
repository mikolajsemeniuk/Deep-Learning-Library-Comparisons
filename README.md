# Deep-Learning-Library-Comparisons
```sh
cd Deep-Learning-Library-Comparisons
pipenv shell

pipenv install numpy
pipenv install pandas 
pipenv install matplotlib

pipenv install nnfs

mypy forward_comparison/self_forward.py --ignore-missing-imports

pipenv run python ./forward_comparison/self_forward.py
```    