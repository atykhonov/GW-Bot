from unittest import TestCase

from pbx_gs_python_utils.utils.Files import Files

from gw_bot.api.API_OSS_Bot import API_OSS_Bot
from gw_bot.helpers import Lambda_Helpers
from gw_bot.helpers.Test_Helper import Test_Helper


class test_Lambda_Helpers(Test_Helper):
    def setUp(self):
        super().setUp()
        self.result = None

    def test_log_info(self):
        Lambda_Helpers.log_info('test info!!!')

    def test_log_debug(self):
        Lambda_Helpers.log_debug('test debug!!!')

    def test_log_error(self):
        self.result = Lambda_Helpers.log_error('test error!!!')

    def test_slack_message(self):
        self.result = Lambda_Helpers.slack_message('test message', channel = 'DRE51D4EM')

    def test_screenshot_from_url(self):
        url = 'https://www.google.com'
        self.result = Lambda_Helpers.screenshot_from_url(url)