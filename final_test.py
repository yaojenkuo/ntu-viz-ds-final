import pandas as pd
from pandas.testing import assert_frame_equal

class FinalExamTest:
    def __init__(self, answer_list):
        self._answer_list = answer_list
        self._n_questions = len(answer_list)
    def generate_answer_dict(self):
        print("Fetching answers...")
        answer_dict = dict()
        for i, df in enumerate(self._answer_list):
            dict_k = "question_{}".format(i + 1)
            dict_v = df
            answer_dict[dict_k] = dict_v
        self._answer_dict = answer_dict
    def generate_test_dict(self):
        print("Fetching test data...")
        folder_name = 'final-test-df/'
        test_list = [pd.read_feather(folder_name + "test_df_{}.feather".format(i+1)) for i in range(self._n_questions)]
        test_dict = dict()
        for i, df in enumerate(test_list):
            dict_k = "question_{}".format(i + 1)
            dict_v = df
            test_dict[dict_k] = dict_v
        self._test_dict = test_dict
    def run_tests(self):
        print("###### TESTING STARTS ######")
        self.generate_answer_dict()
        self.generate_test_dict()
        summary = dict()
        for i in range(self._n_questions):
            summary['Question {}'.format(i+1)] = 0
        for i in range(self._n_questions):
            dict_key = "question_{}".format(i + 1)
            answer_df = self._answer_dict[dict_key]
            test_df = self._test_dict[dict_key]
            try:
                answer_df_str = answer_df.astype(str)
                test_df_str = test_df.astype(str)
                answer_df.columns = test_df.columns
                answer_df.index = test_df.index
                assert_frame_equal(test_df, answer_df)
                summary["Question {}".format(i + 1)] = 5
                print("Congrats! answer {} passed!".format(i + 1))
            except:
                print("Unfortunately, answer {} did not pass, try again!".format(i + 1))
        print("###### TESTING ENDS ######")
        print("Submission Summary")
        for k, v in summary.items():
            print("{}: {}".format(k, v))
        print("Total Points on Final: {}".format(sum(summary.values())))