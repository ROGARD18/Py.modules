import pandas
# import request as rq
# import numpy as np
# import matplotlib as mpl
# import sys
# import importlib as ipl


def loading() -> None:
    df = pandas.read_csv('data.csv')

    print(df.to_string())


if __name__ == "__main__":
    loading()
