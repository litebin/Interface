import requests
def send_request(url):
    r = requests.get(url)
    return r.status_code

def visit_google():
    return send_request('www.google.com')