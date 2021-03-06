from .app import show


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--demo", action="store_true")

    args = parser.parse_args()

    if args.debug or args.demo:
        from . import mock
        import pyblish.api

        for Plugin in mock.plugins:
            pyblish.api.register_plugin(Plugin)

    show()
