import cgi
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from urllib.parse import parse_qs

KEYSDOWN = []


class RequestHandler(BaseHTTPRequestHandler):
    def parse_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        return postvars

    def do_GET(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)
        print(self.headers)
        print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        return 200

    def do_POST(self):

        postvars = self.parse_POST()

        string: str = postvars[b"key"][0].decode("utf-8")

        # print(string.split(":")[0])

        if string.split(":")[0] == "KEY DOWN" and postvars[b'key'][0].split(b':')[1].decode('utf-8')[1:] not in KEYSDOWN:
            KEYSDOWN.append(postvars[b'key'][0].split(b':')[1].decode('utf-8')[1:])
        if string.split(":")[0] == "KEY UP" and postvars[b'key'][0].split(b':')[1].decode('utf-8')[1:] in KEYSDOWN:
            KEYSDOWN.remove(postvars[b'key'][0].split(b':')[1].decode('utf-8')[1:])

        print(f"Keys currently pressed down: {''.join(KEYSDOWN)}")


        self.send_response(200)
        self.end_headers()

        return 200

    do_PUT = do_POST
    do_DELETE = do_GET


def main():
    port = 7000
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()

    main()