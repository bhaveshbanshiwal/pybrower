import socket
import sys
import ssl

class URL:
    def __init__(self, url):
        self.scheme, url = url.split("://", 1)
        assert self.scheme in ["http", "https"] # IF scheme is http or 
        if self.scheme == 'http':
            self.port = 80
        elif self.scheme == "https":
            self.port = 443
        # Other verifications
        if "/" not in url:
            url += "/"

        self.host, url = url.split("/", 1)
        self.path = "/" + url
        # Shows that port is included in url and prevous assigned port can be bypassed
        if ":" in self.host:
            self.host, port = self.host.split(":", 1)
            self.port = int(port)


    def request(self):

        skt = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        skt.connect((self.host, self.port)) # 80 = port
        if self.scheme == "https":
            warp_context = ssl.create_default_context()
            skt = warp_context.wrap_socket(skt, server_hostname=self.host)

        req = f"GET {self.path} HTTP/1.0\r\n" # Requesting webpage cdomman in req variable

        req += f"Host: {self.host}\r\n"
        req += "\r\n" # Giving a blank line to stop server from reciving data anymnore

        skt.send(req.encode("utf8")) # Requesting webpage through tcp

        response = skt.makefile("r", encoding="utf8", newline="\r\n")

        status_line = response.readline() # Status line
        version, status , expl = status_line.split(" ", 2)

        response_headers = {}
        while True:
            line = response.readline()
            if line=="\r\n":
                break
            header, value = line.split(":", 1)
            response_headers[header.casefold()] = value.strip() # casefold gives lowercase string


        # encodings must not be present
        # Compression not allowed by server must not be present
        assert "transfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers
        
        # everything seems right got the content
        content = response.read()
        skt.close()

        return content
    
# def show(body):
#     in_tag = False
#     for c in body:
#         print(c, end="")

# def main():
#     obj = URL("https://example.org/")
#     body = obj.request()
#     show(body)


# if __name__ == "__main__":
#     main()

