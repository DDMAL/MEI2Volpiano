"""Runs tests for mei2volpiano.py

    Run it with:
    `python3 test.py ../resources/016r_reviewed.mei ../resources/CDN-Hsmu_M2149.L4_003r.mei ../resources/CDN-Hsmu_M2149.L4_003v.mei`
    
"""



import unittest
import argparse
import sys
import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import src.mei2volpiano as mei2volpiano


# import doctest

# either we have a correct file already in
# system or we also have it input the file in the command line

# i know this is nasty will refactor later
# or add in seperate file

# 016r_reviewed
correctOutput = (
    "1---g---fg---f---f---f---fffd---"
    + "f---gf---ef---d---e---gh---gkhjk---k7---k---jk"
    + "---hkghg---fg---gf-fded---d---f---gh-hjkg---g-"
    + "--gfgff---fd-fgfef7---fe7---k---klkk---hjkj---hhg"
    + "---hg---h---k---jlkk-kj---hg---hk---k7---k---k---k-"
    + "--klkkjh-jkj---hg---ghk---kjjhjhgh---hg---d---e---"
    + "gh7---k---kh---k---kj---j---jlkj-kjhjh---kj---k---l"
    + "---kjkk---k7---jkmlk-lml---jlkk---jk---h---mh---m---"
    + "lnml-mkkj---k---k---k---k---k---jklkj7---l---lmlmlk-"
    + "--jkljk---jh---hg---k---lml---mklm---m---mnlk-lml-"
    + "--jlkk---kj7---m---m---m---lm---lk-lmlml-jkj---l-"
    + "--lk---lm---lk---jklk---kj---k---kh7---k---k---"
    + "jklkj---l---lmlmlk---jkljk---jh---h---mh---m7---"
    + "l---j---ln7---l---jkj---jk---l---k---jh---ghkhj--"
    + "-hg---j---glj-lm---l---l---l---klmnmlm7---ml---lk-"
    + "--klm---lmlkjk---kj---jk---l---k---kj---h---"
    + "hklkjklkl---lk7---k---k---jklkjh-hkjh---hjghgh7-"
    + "--hg---l---lmnml---klkkj---k---lj"
)
# CDN-Hsmu_M2149.L4_003r.mei
co = (
    "1---nnln-kln---kl---kl---no---n---o-qo-pr--"
    + "-q---r---pqpo---q7---q---o-qo-q---on---nopop-o-"
    + "nmlnon---op---opo---nopono---on---n---noq7---jh--"
    + "-jhghg---hjkl---k---k---k---k---k---kl---k---k---k-"
    + "j-h7---j---ghg---fegh---gf---c---d---f---fg---f---f-"
    + "--ghf---fe7---fgj---jg-h-j-h-g---g-h-g-f-g-f---f---"
    + "g-hg-h7---g-h---g---g---gh7---g---gkh---klkkj-k---"
    + "lmlm---ml---kj---kl---lj---kl---kl---lkkj-j-h-g7---"
    + "ghkg-hggf---h---k---kj-kh---gfghgfg---g-hg---g---"
    + "gh---g---g7---g---lg---lk---lnlmlklk---l---l-nm---"
    + "no---oq---l---nm---l---o---o-nml7---ml----kl---lml-"
    + "ljkj---jk---l-ml-mnm---l---kkj---hg---ghkhj---hg---"
    + "g---g7---h---g---h---g---f---g---kh---kj-kh---hghjhj"
    + "---jh---l---k7---j---lmlm---kl---lj---l---kj-kl---hg"
    + "---ghkg-hggf---f---hk---kj---l-kkjh---kl7---m-nm-n-m"
    + "-l-m-l---lk---l-lkl---hk---j-klkjh-jkjh---g---ghjh-"
    + "gh---hg---l-m-n-m-l"
)
# CDN-Hsmu_M2149.L4_003v.mei
co3 = (
    "1---k-l-k-k-j---k---kl---k---lj---k-l---k-"
    "l---l-m-nm---ml---mlmlk---kj---kl-ml-m-n-m7---"
    "lklml-m---lkj-kj---l-k7---g-h---hg-hggf---f-h---"
    "hklkj-kl7-jl---lk---k---k---j-k-l---k-j---lkjkj-j-"
    "h-g-hg---kk---kh---jklkj-h-jkjh---gh7---j-h-g-h---"
    "h-g---g---g---lg---lk---lnlmlklk---l---nm-n-o--"
    "-o-p---l7---lnnm---n-o-n---mnm-l-ml-ljkj---jk---"
    "lmlm-n-m---kh---klm---lk---j---ljkj-kjh-g-hg7---g-"
    "--gl---lk-lkh---k---jlkk---k-j---g---g-h---hgggf-h--"
    "-f---hk7---kj---lk-kjh---kl-m-nm-nmlml---l---lk-kh"
    "---k---kjkl---h-g---ghkg-hggf7---kk---hk---jklkjh-"
    "jkjh---ghjhgh---h-g7---l-mnml---kj---klkkj---k---k7"
    "---k-l---k---k---k---k---k---lj---kl---kl---lmnm---"
    "m-l7---klkkj---kl---lm---l---l---l---mlmlk---kj---"
    "k-lmlm-n-m---l-j-l-nl-m7---l-kjkj-g-g-lg7---o---o-"
    "--oprr---r---rrq---p---prrq---orpqpqroomnm---mnp---p"
)

listCorrectOutputs = [correctOutput, co, co3]

# 016r.mei
listClefs_016r = [
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
]
# CDN-Hsmu_M2149.L4_003r.mei
listClefs_003r = [
    "C",
    "F",
    "F",
    "F",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
]
# CDN-Hsmu_M2149.L4_003v.mei
listClefs_003v = [
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "C",
    "F",
]

listCorrectClef = [listClefs_016r, listClefs_003r, listClefs_003v]

# 016r.mei
listSyls_016r = [
    "es",
    "e",
    "ius",
    "non",
    "e",
    "lon",
    "ga",
    "bun",
    "tur",
    "Mi",
    "se",
    "re",
    "bi",
    "tur",
    "do",
    "mi",
    "nus",
    "ia",
    "cob",
    "et",
    "is",
    "rael",
    "sal",
    "va",
    "bi",
    "tur",
    "Re",
    "ver",
    "te",
    "re",
    "vir",
    "go",
    "is",
    "rael",
    "re",
    "ver",
    "te",
    "re",
    "ad",
    "ci",
    "vi",
    "ta",
    "tes",
    "tu",
    "as",
    "Mi",
    "se",
    "re",
    "Des",
    "cen",
    "det",
    "do",
    "mi",
    "nus",
    "si",
    "cut",
    "plu",
    "vi",
    "a",
    "in",
    "vel",
    "lus",
    "O",
    "ri",
    "e",
    "tur",
    "in",
    "di",
    "e",
    "bus",
    "e",
    "ius",
    "ius",
    "ti",
    "ci",
    "a",
    "et",
    "a",
    "bun",
    "dan",
    "ti",
    "a",
    "pa",
    "cis",
    "Et",
    "a",
    "do",
    "ra",
    "bunt",
    "e",
    "um",
    "om",
    "nes",
    "re",
    "ges",
    "om",
    "nes",
    "gen",
    "tes",
    "ser",
    "vi",
    "ent",
    "e",
    "i",
    "O",
    "ri",
    "e",
    "Ve",
    "ni",
    "do",
    "mi",
    "ne",
    "et",
    "no",
    "li",
    "tar",
    "da",
    "re",
    "re",
    "la",
    "xa",
    "fa",
    "ci",
    "no",
    "ra",
    "ple",
    "bis",
    "tu",
    "e",
    "et",
    "Re",
    "vo",
    "ca",
    "dis",
    "per",
    "sos",
    "in",
    "ter",
    "ram",
    "su",
    "am",
    "A",
    "so",
    "lis",
    "or",
    "tu",
]
# CDN-Hsmu_M2149.L4_003r.mei
listSyls_003r = [
    "ho",
    "nor",
    "et",
    "om",
    "nis",
    "po",
    "pu",
    "lus",
    "tri",
    "bus",
    "et",
    "lin",
    "guae",
    "ser",
    "vi",
    "ent",
    "e",
    "i",
    "Po",
    "te",
    "s",
    "tas",
    "e",
    "jus",
    "po",
    "tes",
    "tas",
    "ae",
    "ter",
    "na",
    "quae",
    "non",
    "au",
    "fe",
    "re",
    "tur",
    "et",
    "reg",
    "num",
    "e",
    "jus",
    "quod",
    "non",
    "cor",
    "rum",
    "pe",
    "tur",
    "Et",
    "da",
    "Mis",
    "sus",
    "est",
    "ga",
    "bri",
    "el",
    "an",
    "ge",
    "lus",
    "ad",
    "ma",
    "ri",
    "am",
    "vir",
    "gi",
    "nem",
    "de",
    "pon",
    "sa",
    "tam",
    "io",
    "seph",
    "nun",
    "ci",
    "ans",
    "e",
    "i",
    "ver",
    "bum",
    "et",
    "ex",
    "pa",
    "ves",
    "cit",
    "vir",
    "go",
    "de",
    "lu",
    "mi",
    "ne",
    "ne",
    "ti",
    "me",
    "as",
    "ma",
    "ri",
    "a",
    "in",
    "ve",
    "nis",
    "ti",
    "gra",
    "ti",
    "am",
    "a",
    "pud",
    "do",
    "mi",
    "num",
    "Ec",
    "ce",
    "con",
    "ci",
    "pi",
    "es",
    "et",
    "pa",
    "ri",
    "es",
    "et",
    "vo",
    "ca",
    "bi",
    "tur",
    "al",
    "tis",
    "si",
    "mi",
    "fi",
    "li",
    "us",
    "A",
]
# CDN-Hsmu_M2149.L4_003v.mei
listSyls_003v = [
    "ve",
    "ma",
    "ri",
    "a",
    "gra",
    "ti",
    "a",
    "ple",
    "na",
    "do",
    "mi",
    "nus",
    "te",
    "cum",
    "A",
    "ve",
    "ma",
    "ri",
    "a",
    "gra",
    "ti",
    "a",
    "ple",
    "na",
    "do",
    "mi",
    "nus",
    "te",
    "cum",
    "spi",
    "ri",
    "tus",
    "san",
    "ctus",
    "su",
    "per",
    "in",
    "ni",
    "et",
    "in",
    "te",
    "et",
    "vir",
    "tus",
    "al",
    "tis",
    "si",
    "mi",
    "o",
    "bum",
    "bra",
    "bit",
    "ti",
    "bi",
    "quod",
    "e",
    "nim",
    "ex",
    "te",
    "nas",
    "ce",
    "tur",
    "san",
    "ctum",
    "vo",
    "ca",
    "bi",
    "tur",
    "fi",
    "li",
    "us",
    "de",
    "i",
    "Quo",
    "mo",
    "do",
    "fi",
    "et",
    "is",
    "tud",
    "quo",
    "ni",
    "am",
    "vi",
    "rum",
    "non",
    "cog",
    "nos",
    "co",
    "et",
    "res",
    "pon",
    "dens",
    "an",
    "ge",
    "lus",
    "di",
    "xit",
    "e",
    "i",
    "Sal",
    "va",
    "to",
    "rem",
    "ex",
    "pec",
    "ta",
    "mus",
    "do",
    "mi",
]

listCorrectSyls = [listSyls_016r, listSyls_003r, listSyls_003v]


# 016r.mei
listNotes_016r = [
    "g",
    "f",
    "g",
    "f",
    "f",
    "f",
    "f",
    "f",
    "f",
    "d",
    "f",
    "g",
    "f",
    "e",
    "f",
    "d",
    "e",
    "g",
    "a",
    "g",
    "c",
    "a",
    "b",
    "c",
    "c",
    "c",
    "b",
    "c",
    "a",
    "c",
    "g",
    "a",
    "g",
    "f",
    "g",
    "g",
    "f",
    "f",
    "d",
    "e",
    "d",
    "d",
    "f",
    "g",
    "a",
    "a",
    "b",
    "c",
    "g",
    "g",
    "g",
    "f",
    "g",
    "f",
    "f",
    "f",
    "d",
    "f",
    "g",
    "f",
    "e",
    "f",
    "f",
    "e",
    "c",
    "c",
    "d",
    "c",
    "c",
    "a",
    "b",
    "c",
    "b",
    "a",
    "a",
    "g",
    "a",
    "g",
    "a",
    "c",
    "b",
    "d",
    "c",
    "c",
    "c",
    "b",
    "a",
    "g",
    "a",
    "c",
    "c",
    "c",
    "c",
    "c",
    "c",
    "d",
    "c",
    "c",
    "b",
    "a",
    "b",
    "c",
    "b",
    "a",
    "g",
    "g",
    "a",
    "c",
    "c",
    "b",
    "b",
    "a",
    "b",
    "a",
    "g",
    "a",
    "a",
    "g",
    "d",
    "e",
    "g",
    "a",
    "c",
    "c",
    "a",
    "c",
    "c",
    "b",
    "b",
    "b",
    "d",
    "c",
    "b",
    "c",
    "b",
    "a",
    "b",
    "a",
    "c",
    "b",
    "c",
    "d",
    "c",
    "b",
    "c",
    "c",
    "c",
    "b",
    "c",
    "e",
    "d",
    "c",
    "d",
    "e",
    "d",
    "b",
    "d",
    "c",
    "c",
    "b",
    "c",
    "a",
    "e",
    "a",
    "e",
    "d",
    "f",
    "e",
    "d",
    "e",
    "c",
    "c",
    "b",
    "c",
    "c",
    "c",
    "c",
    "c",
    "b",
    "c",
    "d",
    "c",
    "b",
    "d",
    "d",
    "e",
    "d",
    "e",
    "d",
    "c",
    "b",
    "c",
    "d",
    "b",
    "c",
    "b",
    "a",
    "a",
    "g",
    "c",
    "d",
    "e",
    "d",
    "e",
    "c",
    "d",
    "e",
    "e",
    "e",
    "f",
    "d",
    "c",
    "d",
    "e",
    "d",
    "b",
    "d",
    "c",
    "c",
    "c",
    "b",
    "e",
    "e",
    "e",
    "d",
    "e",
    "d",
    "c",
    "d",
    "e",
    "d",
    "e",
    "d",
    "b",
    "c",
    "b",
    "d",
    "d",
    "c",
    "d",
    "e",
    "d",
    "c",
    "b",
    "c",
    "d",
    "c",
    "c",
    "b",
    "c",
    "c",
    "a",
    "c",
    "c",
    "b",
    "c",
    "d",
    "c",
    "b",
    "d",
    "d",
    "e",
    "d",
    "e",
    "d",
    "c",
    "b",
    "c",
    "d",
    "b",
    "c",
    "b",
    "a",
    "a",
    "e",
    "a",
    "e",
    "d",
    "b",
    "d",
    "f",
    "d",
    "b",
    "c",
    "b",
    "b",
    "c",
    "d",
    "c",
    "b",
    "a",
    "g",
    "a",
    "c",
    "a",
    "b",
    "a",
    "g",
    "b",
    "g",
    "d",
    "b",
    "d",
    "e",
    "d",
    "d",
    "d",
    "c",
    "d",
    "e",
    "f",
    "e",
    "d",
    "e",
    "e",
    "d",
    "d",
    "c",
    "c",
    "d",
    "e",
    "d",
    "e",
    "d",
    "c",
    "b",
    "c",
    "c",
    "b",
    "b",
    "c",
    "d",
    "c",
    "c",
    "b",
    "a",
    "a",
    "c",
    "d",
    "c",
    "b",
    "c",
    "d",
    "c",
    "d",
    "d",
    "c",
    "c",
    "c",
    "b",
    "c",
    "d",
    "c",
    "b",
    "a",
    "a",
    "c",
    "b",
    "a",
    "a",
    "b",
    "g",
    "a",
    "g",
    "a",
    "a",
    "g",
    "d",
    "d",
    "e",
    "f",
    "e",
    "d",
    "c",
    "d",
    "c",
    "c",
    "b",
    "c",
    "d",
    "b",
]

# CDN-Hsmu_M2149.L4_003r.mei
listNotes_003r = [
    "f",
    "f",
    "d",
    "f",
    "c",
    "d",
    "f",
    "c",
    "d",
    "c",
    "d",
    "f",
    "g",
    "f",
    "g",
    "b",
    "g",
    "a",
    "c",
    "b",
    "c",
    "a",
    "b",
    "a",
    "g",
    "b",
    "b",
    "g",
    "b",
    "g",
    "b",
    "g",
    "f",
    "f",
    "g",
    "a",
    "g",
    "a",
    "g",
    "f",
    "e",
    "d",
    "f",
    "g",
    "f",
    "g",
    "a",
    "g",
    "a",
    "g",
    "f",
    "g",
    "a",
    "g",
    "f",
    "g",
    "g",
    "f",
    "f",
    "f",
    "g",
    "b",
    "b",
    "a",
    "b",
    "a",
    "g",
    "a",
    "g",
    "a",
    "b",
    "c",
    "d",
    "c",
    "c",
    "c",
    "c",
    "c",
    "c",
    "d",
    "c",
    "c",
    "c",
    "b",
    "a",
    "b",
    "g",
    "a",
    "g",
    "f",
    "e",
    "g",
    "a",
    "g",
    "f",
    "c",
    "d",
    "f",
    "f",
    "g",
    "f",
    "f",
    "g",
    "a",
    "f",
    "f",
    "e",
    "f",
    "g",
    "b",
    "b",
    "g",
    "a",
    "b",
    "a",
    "g",
    "g",
    "a",
    "g",
    "f",
    "g",
    "f",
    "f",
    "g",
    "a",
    "g",
    "a",
    "g",
    "a",
    "g",
    "g",
    "g",
    "a",
    "g",
    "g",
    "c",
    "a",
    "c",
    "d",
    "c",
    "c",
    "b",
    "c",
    "d",
    "e",
    "d",
    "e",
    "e",
    "d",
    "c",
    "b",
    "c",
    "d",
    "d",
    "b",
    "c",
    "d",
    "c",
    "d",
    "d",
    "c",
    "c",
    "b",
    "b",
    "a",
    "g",
    "g",
    "a",
    "c",
    "g",
    "a",
    "g",
    "g",
    "f",
    "a",
    "c",
    "c",
    "b",
    "c",
    "a",
    "g",
    "f",
    "g",
    "a",
    "g",
    "f",
    "g",
    "g",
    "a",
    "g",
    "g",
    "g",
    "a",
    "g",
    "g",
    "g",
    "d",
    "g",
    "d",
    "c",
    "d",
    "f",
    "d",
    "e",
    "d",
    "c",
    "d",
    "c",
    "d",
    "d",
    "f",
    "e",
    "f",
    "g",
    "g",
    "b",
    "d",
    "f",
    "e",
    "d",
    "g",
    "g",
    "g",
    "f",
    "e",
    "d",
    "e",
    "d",
    "c",
    "d",
    "d",
    "e",
    "d",
    "d",
    "b",
    "c",
    "b",
    "b",
    "c",
    "d",
    "e",
    "d",
    "e",
    "f",
    "e",
    "d",
    "c",
    "c",
    "b",
    "a",
    "g",
    "g",
    "a",
    "c",
    "a",
    "b",
    "a",
    "g",
    "g",
    "g",
    "a",
    "g",
    "a",
    "g",
    "f",
    "g",
    "c",
    "a",
    "c",
    "b",
    "c",
    "a",
    "a",
    "g",
    "a",
    "b",
    "a",
    "b",
    "b",
    "a",
    "d",
    "c",
    "b",
    "d",
    "e",
    "d",
    "e",
    "c",
    "d",
    "d",
    "b",
    "d",
    "c",
    "b",
    "c",
    "d",
    "a",
    "g",
    "g",
    "a",
    "c",
    "g",
    "a",
    "g",
    "g",
    "f",
    "f",
    "a",
    "c",
    "c",
    "b",
    "d",
    "c",
    "c",
    "b",
    "a",
    "c",
    "d",
    "e",
    "f",
    "e",
    "f",
    "e",
    "d",
    "e",
    "d",
    "d",
    "c",
    "d",
    "d",
    "c",
    "d",
    "a",
    "c",
    "b",
    "c",
    "d",
    "c",
    "b",
    "a",
    "b",
    "c",
    "b",
    "a",
    "g",
    "g",
    "a",
    "b",
    "a",
    "g",
    "a",
    "a",
    "g",
    "d",
    "e",
    "f",
    "e",
    "d",
]

# CDN-Hsmu_M2149.L4_003v.mei
listNotes_003v = [
    "c",
    "d",
    "c",
    "c",
    "b",
    "c",
    "c",
    "d",
    "c",
    "d",
    "b",
    "c",
    "d",
    "c",
    "d",
    "d",
    "e",
    "f",
    "e",
    "e",
    "d",
    "e",
    "d",
    "e",
    "d",
    "c",
    "c",
    "b",
    "c",
    "d",
    "e",
    "d",
    "e",
    "f",
    "e",
    "d",
    "c",
    "d",
    "e",
    "d",
    "e",
    "d",
    "c",
    "b",
    "c",
    "b",
    "d",
    "c",
    "g",
    "a",
    "a",
    "g",
    "a",
    "g",
    "g",
    "f",
    "f",
    "a",
    "a",
    "c",
    "d",
    "c",
    "b",
    "c",
    "d",
    "b",
    "d",
    "d",
    "c",
    "c",
    "c",
    "b",
    "c",
    "d",
    "c",
    "b",
    "d",
    "c",
    "b",
    "c",
    "b",
    "b",
    "a",
    "g",
    "a",
    "g",
    "c",
    "c",
    "c",
    "a",
    "b",
    "c",
    "d",
    "c",
    "b",
    "a",
    "b",
    "c",
    "b",
    "a",
    "g",
    "a",
    "b",
    "a",
    "g",
    "a",
    "a",
    "g",
    "g",
    "g",
    "d",
    "g",
    "d",
    "c",
    "d",
    "f",
    "d",
    "e",
    "d",
    "c",
    "d",
    "c",
    "d",
    "f",
    "e",
    "f",
    "g",
    "g",
    "a",
    "d",
    "d",
    "f",
    "f",
    "e",
    "f",
    "g",
    "f",
    "e",
    "f",
    "e",
    "d",
    "e",
    "d",
    "d",
    "b",
    "c",
    "b",
    "b",
    "c",
    "d",
    "e",
    "d",
    "e",
    "f",
    "e",
    "c",
    "a",
    "c",
    "d",
    "e",
    "d",
    "c",
    "b",
    "d",
    "b",
    "c",
    "b",
    "c",
    "b",
    "a",
    "g",
    "a",
    "g",
    "g",
    "g",
    "d",
    "d",
    "c",
    "d",
    "c",
    "a",
    "c",
    "b",
    "d",
    "c",
    "c",
    "c",
    "b",
    "g",
    "g",
    "a",
    "a",
    "g",
    "g",
    "g",
    "f",
    "a",
    "f",
    "a",
    "c",
    "c",
    "b",
    "d",
    "c",
    "c",
    "b",
    "a",
    "c",
    "d",
    "e",
    "f",
    "e",
    "f",
    "e",
    "d",
    "e",
    "d",
    "d",
    "d",
    "c",
    "c",
    "a",
    "c",
    "c",
    "b",
    "c",
    "d",
    "a",
    "g",
    "g",
    "a",
    "c",
    "g",
    "a",
    "g",
    "g",
    "f",
    "c",
    "c",
    "a",
    "c",
    "b",
    "c",
    "d",
    "c",
    "b",
    "a",
    "b",
    "c",
    "b",
    "a",
    "g",
    "a",
    "b",
    "a",
    "g",
    "a",
    "a",
    "g",
    "d",
    "e",
    "f",
    "e",
    "d",
    "c",
    "b",
    "c",
    "d",
    "c",
    "c",
    "b",
    "c",
    "c",
    "c",
    "d",
    "c",
    "c",
    "c",
    "c",
    "c",
    "d",
    "b",
    "c",
    "d",
    "c",
    "d",
    "d",
    "e",
    "f",
    "e",
    "e",
    "d",
    "c",
    "d",
    "c",
    "c",
    "b",
    "c",
    "d",
    "d",
    "e",
    "d",
    "d",
    "d",
    "e",
    "d",
    "e",
    "d",
    "c",
    "c",
    "b",
    "c",
    "d",
    "e",
    "d",
    "e",
    "f",
    "e",
    "d",
    "b",
    "d",
    "f",
    "d",
    "e",
    "d",
    "c",
    "b",
    "c",
    "b",
    "g",
    "g",
    "d",
    "g",
    "g",
    "g",
    "g",
    "a",
    "c",
    "c",
    "c",
    "c",
    "c",
    "b",
    "a",
    "a",
    "c",
    "c",
    "b",
    "g",
    "c",
    "a",
    "b",
    "a",
    "b",
    "c",
    "g",
    "g",
    "e",
    "f",
    "e",
    "e",
    "f",
    "a",
    "a",
]

list2 = ["f", "f", "d", "f", "c", "d", "f","c", "d", "c", "d", "f", ‘g’, "f", ‘g’, ‘b’, ‘g’, ‘a’, "c", ‘b’, "c", ‘a’, ‘b’, ‘a’, ‘g’, ‘b’, ‘b’, ‘g’, ‘b’, ‘g’, ‘b’, ‘g’, "f", "f", ‘g’, ‘a’, ‘g’, ‘a’, ‘g’,"f", ‘e’, "d", "f", ‘g’, "f", ‘g’, ‘a’, ‘g’, ‘a’, ‘g’, "f", ‘g’, ‘a’, ‘g’, "f", ‘g’, ‘g’, "f", "f","f", ‘g’, ‘b’, ‘b’, ‘a’, ‘b’, ‘a’, ‘g’, ‘a’, ‘g’, ‘a’, ‘b’,"c", "d","c", "c", "c","c", "c", "c", "d", "c", "c", "c", ‘b’, ‘a’, ‘b’, ‘g’, ‘a’, ‘g’, "f", ‘e’, ‘g’, ‘a’, ‘g’, "f", ‘c’, "d", "f", "f", ‘g’, "f","f", ‘g’, ‘a’, "f", "f", ‘e’, "f", ‘g’, ‘b’, ‘b’, ‘g’, ‘a’, ‘b’, ‘a’, ‘g’, ‘g’, ‘a’, ‘g’, "f", ‘g’,"f", "f", ‘g’, ‘a’, ‘g’, ‘a’, ‘g’, ‘a’, ‘g’, ‘g’, ‘g’, ‘a’, ‘g’, ‘g’, ‘c’, ‘a’, ‘c’, "d", ‘c’, ‘c’, ‘b’, ‘c’,"d", ‘e’, "d", ‘e’, ‘e’, "d", ‘c’, ‘b’, ‘c’, "d", "d", ‘b’, ‘c’, "d", ‘c’, "d", "d", ‘c’, ‘c’, ‘b’, ‘b’, ‘a’, ‘g’, ‘g’, ‘a’, ‘c’, ‘g’, ‘a’, ‘g’, ‘g’, "f", ‘a’, ‘c’, ‘c’, ‘b’, ‘c’, ‘a’, ‘g’, "f", ‘g’, ‘a’, ‘g’, "f", ‘g’, ‘g’, ‘a’, ‘g’, ‘g’, ‘g’, ‘a’, ‘g’, ‘g’, ‘g’, "d", ‘g’, "d", ‘c’, "d", "f", "d", ‘e’, "d", ‘c’, "d", ‘c’, "d", "d", "f", ‘e’, "f", ‘g’, ‘g’, ‘b’, "d", ‘f’, ‘e’, "d", ‘g’, ‘g’, "f", ‘e’, "d", ‘e’, "d", ‘c’, "d", "d", ‘e’, "d", "d", ‘b’, ‘c’, ‘b’, ‘b’, ‘c’, "d", ‘e’, "d", ‘e’, "f", ‘e’, ‘"d", ‘c’, ‘c’, ‘b’, ‘a’, ‘g’, ‘g’, ‘a’, ‘c’, ‘a’, ‘b’, ‘a’, ‘g’, ‘g’, ‘g’, ‘a’, ‘g’, ‘a’, ‘g’, "f", ‘g’, ‘c’, ‘a’, ‘c’, ‘b’, ‘c’, ‘a’, ‘a’, ‘g’, ‘a’, ‘b’, ‘a’, ‘b’, ‘b’, ‘a’,"d", ‘c’, ‘b’, "d", ‘e’,"d", ‘e’, ‘c’, "d", "d", ‘b’,"d", ‘c’, ‘b’, ‘c’, "d", ‘a’, ‘g’, ‘g’, ‘a’, ‘c’, ‘g’, ‘a’, ‘g’, ‘g’, ‘f’, ‘f’, ‘a’, ‘c’, ‘c’, ‘b’, "d", ‘c’, ‘c’, ‘b’, ‘a’, ‘c’, "d", ‘e’, ‘f’, ‘e’, ‘f’, ‘e’, "d", ‘e’, "d","d", ‘c’, "d", "d", ‘c’, "d", ‘a’, ‘c’, ‘b’, ‘c’, "d", ‘c’, ‘b’, ‘a’, ‘b’, ‘c’, ‘b’, ‘a’, ‘g’, ‘g’, ‘a’, ‘b’, ‘a’, ‘g’, ‘a’, ‘a’, ‘g’,"d", ‘e’, ‘f’, ‘e’, "d"]

listNotes = [listNotes_016r, listNotes_003r, listNotes_003v]


class TestVolpiano(unittest.TestCase):
    # tests the output of a correct volpiano file vs
    # a generated volpiano sequence

    def test_volpiano_output_1(self):
        lib = mei2volpiano.MEItoVolpiano()
        with open(sys.argv[-1], "r") as f:
            final_string = lib.convert_mei_volpiano(f)
            self.assertEqual(final_string, listCorrectOutputs[-1])

    def test_volpiano_output_many(self):
        lib = mei2volpiano.MEItoVolpiano()
        ind = 1
        for mei_file in sys.argv[ind:]:
            with open(mei_file, "r") as f:
                final_string = lib.convert_mei_volpiano(mei_file)
                self.assertEqual(final_string, listCorrectOutputs[ind - 1])
            ind += 1

    # these tests may not be necessary
    # they may be used later on for further testing

    def test_find_clefs(self):
        lib = mei2volpiano.MEItoVolpiano()
        ind = 1
        for mei_file in sys.argv[ind:]:
            with open(mei_file, "r") as f:
                elements = lib.get_mei_elements(mei_file)
                listC = lib.find_clefs(elements)
                self.assertEqual(listC, listCorrectClef[ind - 1])
            ind += 1

    def test_find_notes(self):
        lib = mei2volpiano.MEItoVolpiano()
        ind = 1
        for mei_file in sys.argv[ind:]:
            with open(mei_file, "r") as f:
                elements = lib.get_mei_elements(mei_file)
                listN = lib.find_notes(elements)
                self.assertEqual(listN, listNotes[ind - 1])
            ind += 1

    def test_find_syls(self):
        lib = mei2volpiano.MEItoVolpiano()
        ind = 1
        for mei_file in sys.argv[ind:]:
            with open(mei_file, "r") as f:
                elements = lib.get_mei_elements(mei_file)
                listS = lib.find_syls(elements)
                self.assertEqual(listS, listCorrectSyls[ind - 1])
            ind += 1


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
