#!/usr/bin/env python3

from glob import glob
from itertools import chain
from os.path import basename
from re import findall

DIRECTORY = "../text"

contents = {}
words = {}
all_contents = []
all_words = []

for filename in glob(DIRECTORY + "/*.txt"):
    key = basename(filename)
    with open(filename) as f:
        contents[key] = f.read()
        assert contents[key].endswith("\n")
        words[key] = findall(r"[\w']+|[.,!?;]", contents[key])
        all_contents.append(contents[key])
        all_words.extend(words[key])
all_contents = "".join(all_contents)

print("{:35s} {:>5} {:>5} {:>5}".format(
    "FILENAME",
    "BYTES",
    "TOKEN",
    "TYPE",
))
print("-" * 53)
for filename in sorted(contents):
    print("{:35s} {:>5} {:>5} {:>5}".format(
        filename,
        len(contents[filename]),
        len(words[filename]),
        len(set(words[filename])),
    ))
print("-" * 53)
print("{:35s} {:>5} {:>5} {:>5}".format(
    "COLLECTION",
    len(all_contents),
    len(all_words),
    len(set(all_words)),
))

print()

for filename in sorted(contents):
    document_words = set(words[filename])
    other_words = set(
        chain.from_iterable(
            words[other]
            for other in contents.keys() - {filename}
        )
    )

    print("Unique to {}:".format(filename))
    print(document_words - other_words)
    print()
