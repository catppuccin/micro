# Comment

class Sample:
    def _init_(sefl, props):
        self.sample_1 = something_1['code_1']
        self.sample_2 = something_2['code_2']

    def function_1(self):
        return self.function_2()

    def function_2(self):
        return self.sample_1 - self.sample_2

# One more comment

Sample_2 = Sample(
    {
        'sample_1' = 'Value_1'
        'sample_2' = 'Value_2'
    }
)
