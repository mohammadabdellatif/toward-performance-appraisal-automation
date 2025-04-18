import unittest

from ds_extractor.comments import CommentPreprocessor


class CommentPreprocessorTest(unittest.TestCase):

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.under_test = CommentPreprocessor(tokens_replacement=[('ph_user', ['nn', 'sozi ahmad','jack jone']),
                                                                  ('ph_name', ['cc', 'bb'])])

    def test_simple_case_1(self):
        self.__do_test(['greetings', 'is it confirmed by your security team ?'],
                       """
        <p>Dear Faiza , </p><p>Is it confirmed by your security team ?</p>
        """)

    def test_simple_case_2(self):
        self.__do_test(["dear sir",
                        "all required files uploaded ( iam folders and ph_file for all ph_user system from production ) ."],
                       """
                           <p>Dear Sir</p><p><br />all required files uploaded ( IAM folders and servr.xml for all NN system from production ) . </p>        
                           """)

    def __do_test(self, expected, text):
        actual = self.under_test.preprocess_comment(text)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
