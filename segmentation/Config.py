import yaml

class Config(object):
    def __init__(self):
        with open('../resource/config.yaml') as file:
            self.config = yaml.load(file, Loader=yaml.Loader)


    def getPathDataTrainInput(self):
        return self.config.get('datasets').get('path').get('train').get('input')

    def getPathDataTrainMask(self):
        return self.config.get('datasets').get('path').get('train').get('mask')

    def getPathDataTestInput(self):
        return self.config.get('datasets').get('path').get('test').get('input')

    def getPathDataTestOutput(self):
        return self.config.get('datasets').get('path').get('test').get('output')