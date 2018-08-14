class ProgressBar:
    def __init__(self, iteration, total, prefix='Progress', suffix='Complete', decimals=1, length=100, fill='█'):
        '''
        Call in a loop to create terminal progress bar
        :param iteration: - Required : start iteration (int)
        :param total: - Required : total iterations (int)
        :param prefix: - Optional : prefix string (Str)
        :param suffix: - Optional : suffix string (Str)
        :param decimals: - Optional : positive number of decimals in percent complete (int)
        :param length: - Optional : character length of bar (int)
        :param fill: - Optional : bar fill character (str)
        '''
        self.iteration = iteration
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.percent = None
        self.bar = None
        self.__create_progress_bar()

    def __create_progress_bar(self):
        self.percent = ('{0:.' + str(self.decimals) + 'f}').format(100 * self.iteration / float(self.total))
        filled_length = int(self.length * self.iteration // self.total)
        self.bar = self.fill * filled_length + '-' * (self.length - filled_length)

    def __print_progress_bar(self):
        print('\r%s |%s| %s%% %s' % (self.prefix, self.bar, self.percent, self.suffix), end='\r')
        if self.iteration == self.total:
            print()

    def initial_print(self):
        '''
        Initial call to print 0% progress
        '''
        self.__print_progress_bar()

    def current_print(self, current_iteration):
        '''
        Update Progress Bar
        :param current_iteration: current iteration (int)
        :return:
        '''
        self.iteration = current_iteration
        self.__create_progress_bar()
        self.__print_progress_bar()
