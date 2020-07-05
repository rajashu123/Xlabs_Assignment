import logging
import logging.handlers
import os
logging.basicConfig(filename='api_test.log')
LOGGER = logging.getLogger('ROOT')
COMPONENT = None



class SetupLogger(object):
    """
        Class to Setup Logger
    """
    @classmethod
    def initialize(cls, component, path=None):
        def _init_formatter(component):

            return logging.Formatter(
                '%(levelname)5s - %(asctime)s  - ' + component + ' - '
                '%(filename)s - %(name)s - %(funcName)s - %(lineno)s : '
                '%(message)s'
            )

        def _register_component(component):

            global COMPONENT
            COMPONENT = component
            return True

        def _init_log_handler(logger, component):
            """
                Init Log File Handler
            """
            _handler = logging.StreamHandler()
            _handler.setFormatter(_init_formatter(component))


            logger.addHandler(_handler)


        def _init_log_level_stats(logger):
            """
                Init new Log Level Stats
            """

            logging.STATS = 15
            logging.addLevelName(logging.STATS, "STATS")
            logging.Logger.stats = (
                lambda inst, msg, *args, **kwargs: (
                    inst.log(logging.STATS, msg, *args, **kwargs)
                )
            )
            logger.setLevel(logging.STATS)

            return True

        # INIT
        valid = True

        valid = valid and _register_component(component)
        valid = valid and _init_log_handler(LOGGER, component)
        valid = valid and _init_log_level_stats(LOGGER)

        return valid

