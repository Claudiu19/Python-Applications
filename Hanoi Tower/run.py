

import random
import subprocess
import sys
import time


H_SCRIPT = "hanoi.py"
H_OUTPUT = "hanoi.txt"

R_OUTPUT = "run.txt"
#R_OUTPUT = None

ALGOS = [
    "backtrack",
    "hillclimb",
    "astar",
    "optrand",
]

RODS_RANGE = (3, 9)
DISKS_RANGE = (3, 9)


def log(string):
    string += "\n"
    stream = open(R_OUTPUT, "a") if R_OUTPUT else sys.stdout
    stream.write(string)
    stream.flush()


def main(argv):

    log(time.ctime())
    log("")

    params = [(3,3),(4,4),(5,5),(6,6)]

    for algo in ALGOS:
        deltas = []
        steps_list = []
        for idx in range(len(params)):
            rods, disks = params[idx]
            print("Running test #{} for {!r} - {} x {}"
                    .format(idx + 1, algo, rods, disks))
            start = time.time()
            pop = subprocess.Popen(["python", H_SCRIPT, rods, disks, algo])
            rcode = pop.wait()
            delta = time.time() - start
            deltas.append(delta if not rcode else -1)
            with open(H_OUTPUT, "r") as stream:
                steps = len(stream.readlines())
            if not rcode:
                steps_list.append(steps)
        good = filter(lambda delta: delta != -1, deltas)
        log(algo)
        good=list(good) #may pop
        log("Success rate: {}/{}".format(len(good), len(deltas)))
        if len(good):
            log("Average steps: {}".format(sum(steps_list) / len(steps_list)))
            log("Average time: {}".format(sum(good) / len(good)))
            log("Total time: {}".format(sum(good)))
        log("")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
