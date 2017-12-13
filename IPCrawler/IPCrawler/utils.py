import requests

class Utils(object):

    @staticmethod
    def checkProxy(proxy):
        '''Check the availability of the given proxy

            Args:
                proxy: type#host:port, like HTTP#0.0.0.0:8888

            Returns:
                True when proxy is available, otherwise false
        '''
        httpType, proxy = proxy.split("#")[0].lower(), proxy.split("#")[1]
        proxies = {
            httpType: proxy
        }
        try:
            response = requests.get("http://www.baidu.com", proxies=proxies, timeout=2)
            return response.status_code == 200
        except:
            return False
