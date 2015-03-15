from flask import Flask


class Example(Flask):

    thing = None

    def __init__(self, import_name,
                 static_path=None,
                 static_url_path='/static',
                 instance_path=None,
                 instance_relative_config=False):
        """Constructor for Example."""
        super(Example, self).__init__(
            import_name, static_path=static_path,
            static_url_path=static_path,
            instance_path=instance_path,
            instance_relative_config=instance_relative_config)

        self.register_views()

    def register_views(self):
        self.add_url_rule('/', 'index', self.index)

    def index(self):
        return 'Hello.'

    @classmethod
    def create_app(cls, import_name, **kwargs):
        app = cls(import_name, **kwargs)
        return app
