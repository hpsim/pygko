__version__ = '0.0.0'
try:
    from ._pygko import longest  # noqa
except ImportError:
    def longest(args):
        return max(args, key=len)