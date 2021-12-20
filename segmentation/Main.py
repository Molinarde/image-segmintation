from Config import Config
from Unet import Unet

def main():
    config = Config()
    trainInput = config.getPathDataTrainInput()
    maskTrain = config.getPathDataTrainMask()
    testInput = config.getPathDataTestInput()
    testOutput = config.getPathDataTestOutput()

    unet = Unet()
    model = unet.get_unet()

    # unet.train()
    unet.segmintationImage()
    unet.save_img()



if __name__ == '__main__':
    main()
