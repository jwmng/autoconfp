from configparser import ConfigParser


class AutoConfigParser(ConfigParser):
    def __init__(self, *args, **kwargs):
        self.try_order = (int, float, self._convert_to_boolean, str)
        super(AutoConfigParser, self).__init__(*args, **kwargs)

    def get_raw(self, *args, **kwargs):
        return super(AutoConfigParser, self).get(*args, **kwargs)

    def _get(self, section, conv, option, **kwargs):
        return conv(self.get_raw(section, option, **kwargs))

    def get(self, section, option, *args, **kwargs):
        for conv in self.try_order:
            try:
                return self._get_conv(section, option, conv, *args, **kwargs)
            except ValueError:
                continue
