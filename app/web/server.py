from flask import Flask

class Server(object):
    def __init__(self, **configs):
        self.app = Flask(__name__)
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, rule, endpoint=None, view_func=None, provide_automatic_options=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(rule, endpoint, view_func, provide_automatic_options, methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)
