# coding:utf-8

client_node = NodeManager('localhost', 3002, 2222)
client_node.ping(client_node.server.socket, 1111, ('localhost', 3001))

client_node.server.serve_forever()