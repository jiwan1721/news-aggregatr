from urllib.parse import urlparse
def get_host_name(url):    
    url_parse = urlparse(url)
    
    return url_parse.scheme+'://' +url_parse.netloc
    
    