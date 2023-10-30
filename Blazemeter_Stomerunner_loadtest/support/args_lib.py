import argparse
def get_run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-run', '--run', required=True, help='Choose blazemeter or stomerunner')
    args = parser.parse_args()
    run  = args.run
    return run