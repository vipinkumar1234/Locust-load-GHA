from locust import task, SequentialTaskSet, HttpUser, between, constant
import json

data1 = {
    "metadata": {
        "correlationId": "test-correlation-id"
    },
    "assetVdsId": "eurosport-0",
    "clientProperties": {
        "platform": "internal",
        "device": {
            "browser": {
                "name": "chrome"
            },
            "os": "macos",
            "type": "desktop"
        }
    },
    "contentSubset": "eurosport"
}

data2 = {
    "metadata": {
        "correlationId": "test-correlation-id"
    },
    "assetVdsId": "eurosport-0",
    "clientUseragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "contentSubset": "eurosport"
}

payload1 = json.dumps(data1)
payload2 = json.dumps(data2)
headers = {
    "x-vdp-access-key": "Qm9C25NupHRfTYyIfXMJg7EGlZ476cBP5zEDwUojwZ0xArGI"
}


class MyReqRes(SequentialTaskSet):

    @task
    def getVideoLiveStream(self):
        res = self.client.post('/v3/GetVideoLiveStream',
                               data=payload1,
                               headers=headers
                               )
        print('GetVideoLiveStream: ',res.status_code)          
        

    @task
    def getVideoLiveStreamBackOffice(self):
        res = self.client.post('/v3/GetVideoLiveStreamBackOffice',
                               data=payload2,
                               headers=headers
                               )
        
        print('GetVideoLiveStreamBackOffice: ',res.status_code) 


class LiveStream(HttpUser):
    wait_time = constant(5)
    host = "https://prod.playback.h264.io"
    tasks = [MyReqRes]