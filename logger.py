import logging

def logger_config(name):
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)

    handler_log = logging.FileHandler(f'logs/{name}.log', mode='w')
    formatter_log = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

    handler_log.setFormatter(formatter_log)
    log.addHandler(handler_log)
    return log