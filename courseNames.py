    def courseNames(self):
        """
        make courses of the same courseNum have the first courseTitle assciated
        with it
        """

        # start dictionary that pairs courseNum with courseTitle
        NumTitlePair = {}
        # find all the unique courseNums and put
        uniqueCourseNum = self.df.courseNum.unique()
        
        # run thru df backwards and assign the latest courseTitle to the courseNum
        for i in reversed(range(len(self.df.index))):
            year = self.df.loc[i,'academicYear']
            if ('MTH2188' in self.df.courseNum[i]) and ('FA' in year):
                self.df.courseTitle[i] = 'Linearity II'
            elif ('MTH2188' in self.df.courseNum[i]) and ('SP' in year):
                self.df.courseTitle[i] = 'Linearity I'
            elif self.df.courseNum[i] in NumTitlePair:
                self.df.courseTitle[i] = NumTitlePair[self.df.courseNum[i]]
            else:
                NumTitlePair[self.df.courseNum[i]] = self.df.courseTitle[i]

        return self.df