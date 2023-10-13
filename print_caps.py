def allcaps(sentence):
    def new_func():
        string = sentence()
        string = string.upper()
        return string
    return new_func
