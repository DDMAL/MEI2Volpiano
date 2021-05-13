import unittest
import argparse
import sys
import os
import inspect
import mei2volpiano

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

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

# input like this:
# python3 ./tests/test.py ./resources/016r_reviewed.mei ./resources/CDN-Hsmu_M2149.L4_003r.mei ./resources/CDN-Hsmu_M2149.L4_003v.mei
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
    "mi",
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
listSyls_003r = []
# CDN-Hsmu_M2149.L4_003v.mei
listSyls_003v = []

listCorrectSyls = [listSyls_016r, listSyls_003r, listSyls_003v]


class TestVolpiano(unittest.TestCase):
    # tests the output of a correct volpiano file vs
    # a generated volpiano sequence

    def test_volpiano_output_1(self):
        lib = mei2volpiano.MEItoVolpiano()
        with open(sys.argv[-1], "r") as f:
            final_string = lib.convert_mei_volpiano(f)
            self.assertEqual(final_string, listCorrectOutputs[-1])

    def test_volpiano_output_many(self):
        ind = 1
        lib = mei2volpiano.MEItoVolpiano()
        for mei_file in sys.argv[ind:]:
            with open(mei_file, "r") as f:
                final_string = lib.convert_mei_volpiano(mei_file)
                self.assertEqual(final_string, listCorrectOutputs[ind - 1])
            ind += 1

    # these tests may not be necessary
    # they may be used later on for further testing

    def test_find_clefs(self):
        ind = 1
        lib = mei2volpiano.MEItoVolpiano()
        for mei_file in sys.argv[ind:]:
            with open(mei_file, "r") as f:
                elements = lib.get_mei_elements(mei_file)
                listC = lib.find_clefs(elements)
                self.assertEqual(listC, listCorrectClef[ind - 1])
            ind += 1

    def test_find_notes(self):
        pass

    def test_find_syls(self):
        ind = 1
        lib = mei2volpiano.MEItoVolpiano()
        for mei_file in sys.argv[ind:]:
            with open(mei_file, "r") as f:
                elements = lib.get_mei_elements(mei_file)
                listS = lib.find_syls(elements)
                self.assertEqual(listC, listCorrectSyls[ind - 1])
            ind += 1

    def test_getVolpiano(self):
        pass


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
