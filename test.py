import unittest
import mei2volpiano
import argparse

# import doctest

# either we have a correct file already in
# system or we also have it input the file in the command line
correctOutput = "1---g---fg---f---f---f---fffd---f---gf---ef---d---e---gh---gkhjk---k7---k---jk---hkghg---fg---gf-fded---d---f---gh-hjkg---g---gfgff---fd-fgfef7---fe7---k---klkk---hjkj---hhg---hg---h---k---jlkk-kj---hg---hk---k7---k---k---k---klkkjh-jkj---hg---ghk---kjjhjhgh---hg---d---e---gh7---k---kh---k---kj---j---jlkj-kjhjh---kj---k---l---kjkk---k7---jkmlk-lml---jlkk---jk---h---mh---m---lnml-mkkj---k---k---k---k---k---jklkj7---l---lmlmlk---jkljk---jh---hg---k---lml---mklm---m---mnlk-lml---jlkk---kj7---m---m---m---lm---lk-lmlml-jkj---l---lk---lm---lk---jklk---kj---k---kh7---k---k---jklkj---l---lmlmlk---jkljk---jh---h---mh---m7---l---j---ln7---l---jkj---jk---l---k---jh---ghkhj---hg---j---glj-lm---l---l---l---klmnmlm7---ml---lk---klm---lmlkjk---kj---jk---l---k---kj---h---hklkjklkl---lk7---k---k---jklkjh-hkjh---hjghgh7---hg---l---lmnml---klkkj---k---lj"
correctElements = []


class TestVolpiano(unittest.TestCase):
    # tests the output of a correct volpiano file vs
    # a generated volpiano sequence
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()

    def test_volpiano_output_1(self):
        filename = args[-1]
        elements = mei2volpiano.MEI2Volpiano.get_mei_elements(filename)
        mapped = mei2volpiano.MEI2Volpiano.map_sylb(elements)
        final_string = mei2volpiano.MEI2Volpiano.export_volpiano(mapped)
        self.assertEqual(final_string, correctOutput)


if __name__ == "__main__":
    unittest.main()
