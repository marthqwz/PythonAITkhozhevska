


class CoalMicrophone:
    def __init__(self):
        super().__init__()
        self.sensitivity = 60
        self.noise = 80
    def sharing_sound(self):
        print("I am used to share sounds in a bigger distance")

class DynamicMicrophone(CoalMicrophone):
    def __init__(self):
        super().__init__()
        self.singingability = 'Yes'
    def pickingup_vocals(self):
        print("I am used for people to sing")

class CondenserMicrophone(DynamicMicrophone):
    def __init__(self):
        super().__init__()
        self.noisereduction = 75
        self.color = 'RGB'
        self.sensitivity = 15
        self.noise = 30

    def microphone_info(self):
        print("This is my characteristics:")
        print(f"Sensitivity: {self.sensitivity}")
        print(f"Noise Reduction: {self.noisereduction}")
        print(f"Color: {self.color}")
        print(f"Noise Level: {self.noise}")
        print(f"Singing Ability: {self.singingability}")



fifine = CondenserMicrophone()
fifine.microphone_info()


