import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import sys

def run():
    with open(sys.argv[1]) as f:
        data = f.readlines()
        data = [d.strip("\n") for d in data]

        counts = Counter(data)
        df = pd.DataFrame.from_dict(counts, orient="index", columns=["count"])
        df.sort_values(by="count", inplace=True, ascending=False)

        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(16,5))

        df.plot(kind="bar", ax=ax)

        fig.tight_layout()
        fig.savefig("analysis.pdf")

if __name__ == "__main__":
    run()
