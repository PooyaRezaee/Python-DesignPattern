"""
    Fecade
        - Packing Code
"""

class Request:
    def __init__(self,url):
        print("Sended Request")
        self.response = "This is response"
    def get_response(self):
        return self.response

class WriteInFile:
    def __init__(self,text):
        self.text = text
    def write(self):
        print(f'Writed "{self.text}" In File')

class WriteInDatabase:
    def __init__(self,text):
        self.text = text
    def write(self):
        print(f'Writed "{self.text}" In Database')

class SendRequestAndSave: # Fecade
    def __init__(self,url):
        self.url = url

    def do(self):
        request = Request(self.url)
        response = request.get_response()

        wf = WriteInFile(response)
        wf.write()

        wd = WriteInDatabase(response)
        wd.write()

        print("Finished")


task = SendRequestAndSave('localhost')
task.do()

