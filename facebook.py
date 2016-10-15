import requests

class Graph:
    def __init__(self,token):
        self.BASE_URL = "https://graph.facebook.com/v2.8"
        self.TOKEN = token
    def whoami(self,fields = ['id','name']):
        r = requests.get(self.BASE_URL + "/me" + "?fields=" + ",".join(fields) + "&access_token=" + self.TOKEN)
        return r.text
    def comments(self, id, fields = ['from','comments','created_time','message'], limit=1000):
        r = requests.get(self.BASE_URL + "/" + id +"/comments" + "?fields=" + ",".join(fields) + "&limit" + str(limit) + "&access_token=" + self.TOKEN )
        return r.text
