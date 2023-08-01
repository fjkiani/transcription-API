import os

class LoadSecrets:
    def __init__(self):
        pass

    @staticmethod
    def load_secret():
        key = "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"
        os.environ['OPENAI_API_KEY'] = key
        print("Secrets loaded")