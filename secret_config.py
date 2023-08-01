import os

class LoadSecrets:
    def __init__(self):
        pass

    @staticmethod
    def load_secret():
        key = "#"
        os.environ['OPENAI_API_KEY'] = key
        print("Secrets loaded")