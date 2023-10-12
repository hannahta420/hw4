def allcaps(sentence):
    def new_func():
        string = sentence()
        string = string.upper()
        print(string)
    return new_func
