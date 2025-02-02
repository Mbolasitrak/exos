#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

# import mon_module
from traitementJson import TraitementJson

# globals
listcmd=["bouton1","bouton2"]

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cmd=self.path[1:8]
	# HERE YOU SHOULD PROBABLY DO SOMETHING WITH cmd
        json_trait = TraitementJson("buttons.json")
        json_trait.upjson(cmd)

        message = cmd+' OK\n'
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return

class RouteHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path[1:8] in listcmd:
            return GetHandler.do_GET(self)
        else:
            super(RouteHandler,self).do_GET()

class ThreadingSimpleServer(ThreadingMixIn,HTTPServer): pass

if __name__ == '__main__':
    server=ThreadingSimpleServer(('0.0.0.0',8000),RouteHandler)
    print('Starting server, use <Ctrl-C> to stop')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

