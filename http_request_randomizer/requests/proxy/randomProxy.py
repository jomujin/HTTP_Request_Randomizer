import time
import requests
from typing import List, Any
from fake_headers import Headers
from .requestProxy import RequestProxy
# from HTTP_Request_Randomizer.http_request_randomizer.requests.proxy.requestProxy import RequestProxy


class RandomProxy:

    def __init__(self):
        self.session = requests.Session()
        self.proxy: Any = None
        self.proxy_list: List[Any] = []

    def get_proxy_by_num(
        self,
        count: int = 3,
        max_limit_time: int = 300
    ):
        """
        무작위로 프록시를 생성해서 가져오는 코드
        """

        self.proxy_list: List[Any] = [] # self.proxy_list 리셋
        start_time = time.time()
        while True:
            self.req_proxy = RequestProxy()
            proxy = self.test_proxy() # 잘 작동되는 프록시 선별
            self.proxy_list.append(proxy)
            if (len(self.proxy_list) < count) \
            or (time.time() - start_time < max_limit_time):
                continue
            else:
                break

    def get_proxy_one(self):
        """
        무작위로 프록시를 생성해서 가져오는 코드
        """

        self.proxy: Any = None # self.proxy 리셋
        self.req_proxy = RequestProxy()
        self.proxy = self.test_proxy() # 잘 작동되는 프록시 선별

    def test_proxy(self):
        """
        가져온 프록시중에서 실제로 작동되는 프록시만 하나씩 가져오는 코드
        test_url : 자신의 IP를 확인하는 코드. 여기서 변경된 IP가 나오면 성공적으로 우회가된것
        """
        
        # test_url = 'http://ipv4.icanhazip.com' 
        test_url = 'http://www.nba.com'
        try_no = 0
        while True: # 제대로된 프록시가 나올때까지 무한반복 
            print(try_no)
            requests = self.req_proxy.generate_proxied_request(test_url)

            if requests is not None:
                print('Requests is not None')
                # print("\t Response: ip={0}".format(u''.join(requests.text).encode('utf-8')))
                proxy = self.req_proxy.current_proxy
                try_no += 1
                break

            else:
                try_no += 1
                continue

        return proxy # 잘작동된 proxy를 뽑아준다. 
        
    def create_header(self):
        self.header = Headers(
            browser="chrome",  # Generate only Chrome UA
            os="win",  # Generate ony Windows platform
            headers=True  # generate misc headers
        )
        self.header = self.header.generate()

        self.headers = {
            'Host': 'stats.nba.com',
            'User-Agent': self.header['User-Agent'],
            'Accept': self.header['Accept'], # 'Accept': 'application/json, text/plain, */*',
            # 'Accept-Language': self.header['Accept-Language'], # 'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'x-nba-stats-origin': 'stats',
            'x-nba-stats-token': 'true',
            'Connection': 'keep-alive',
            'Referer': 'https://stats.nba.com/',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

    def get_proxies(self):
        self.proxies = {} # request.get 인자에 넣어줄 딕셔너리 생성 

        if (self.proxy_list) \
        and (len(self.proxy_list) > 0) \
        and (self.proxy) \
        and (self.proxy is not None):
            raise ValueError

        if (self.proxy_list) \
        and (len(self.proxy_list) > 0):
            for proxy in self.proxy_list:
                self.proxies['http'] = 'http://%s' % proxy
                self.proxies['https'] = 'https://%s' % proxy

        if (self.proxy) \
        and (self.proxy is not None):
            self.proxies['http'] = 'http://%s' % self.proxy
            self.proxies['https'] = 'https://%s' % self.proxy


    # def crawling(self):
    #     header = Headers(
    #         browser="chrome",  # Generate only Chrome UA
    #         os="win",  # Generate ony Windows platform
    #         headers=True  # generate misc headers
    #     )
    #     self.headers = header.generate() # 랜덤 유저 에이전트를 생성해주는 함수.
    #     _url = 'https://stats.nba.com/stats/boxscoresummaryv2?GameID=0024900496'

    #     self.proxies = {} # request.get 인자에 넣어줄 딕셔너리 생성 
    #     self.proxies['http'] = 'http://%s' % self.proxy

        # self.html = self.session.get(_url, headers=self.headers,proxies=self.proxies).content
        # get 인자에 프록시와 헤더를 넣어주면 끝.
        
# if __name__ == "__main__":
    
#     RANDOM_PROXY()