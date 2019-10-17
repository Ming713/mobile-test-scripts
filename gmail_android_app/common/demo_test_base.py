import logging
import unittest

import os


logger = logging.getLogger(__name__)

class DemoTestBase(unittest.TestCase):

    def setup(self):
        self.environment = os.getenv('TARGETENV', 'locals')
        if self.environment.upper() not in ("LOCAL", "SAUCELABS"):
            logger.info(
                "Invalid value for VIRTRU_TARGETENV = %s defined, set default value SAUCELABS", self.environment)
            self.environment = "saucelabs"

