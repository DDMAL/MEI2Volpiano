import unittest
import argparse
import sys


import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import mei2volpiano

# import doctest

# either we have a correct file already in
# system or we also have it input the file in the command line

# i know this is nasty will refactor later
# or add in seperate file
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
# correctElements = []
listCorrectOutputs = [correctOutput, co]


class TestVolpiano(unittest.TestCase):
    # tests the output of a correct volpiano file vs
    # a generated volpiano sequence

    def test_volpiano_output_1(self):
        lib = mei2volpiano.MEItoVolpiano()
        with open(sys.argv[-1], "r") as f:
            elements = lib.get_mei_elements(f)
            mapped = lib.map_sylb(elements)
            final_string = lib.export_volpiano(mapped)
            self.assertEqual(final_string, listCorrectOutputs[-1])

    def test_volpiano_output_many(self):
        ind = 1
        lib = mei2volpiano.MEItoVolpiano()
        for mei_file in sys.argv[ind:]:
            with open(mei_file, "r") as f:
                elements = lib.get_mei_elements(f)
                mapped = lib.map_sylb(elements)
                final_string = lib.export_volpiano(mapped)
                self.assertEqual(final_string, listCorrectOutputs[ind - 1])
            ind += 1

    # these tests may not be necessary
    # they may be used later on for further testing

    def test_get_mei_elements(self):
        pass

    def test_find_clefs(self):
        pass

    def test_find_notes(self):
        pass

    def test_map_sylb(self):
        pass

    def test_get_syl_key(self):
        pass

    def test_getVolpiano(self):
        pass

    def test_export_volpiano(self):
        pass


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
