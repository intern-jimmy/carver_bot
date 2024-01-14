import unittest
import configparser

import src.config as cfg

class TestConfig(unittest.TestCase):
    def test_creation_loads_a_configfile(self):
        # Arrange
        config = configparser.ConfigParser()
        expected = config.read('config.ini')

        # Act
        actual = cfg.Config()

        # Assert
        """ Figure out how to test this """
        self.assertEqual(1, 1)

    def test_update_of_non_existant_item(self):
        # Arrange
        config = cfg.Config()

        # Act
        config.set('DEFAULT', 'ping', 'pong')

        # Assert
        self.assertEqual(config.get('DEFAULT', 'ping'), 'pong')

    def test_update_existing_option(self):
        # Arrange
        config = cfg.Config()

        # Act
        config.set('DEFAULT', 'interval', '10')

        # Assert
        self.assertEqual(config.get('DEFAULT', 'interval'), '10')

    def test_get_sections(self):
        # Arrange
        config = cfg.Config()
        expected = ['bot', 'Serendale1.0', 'Crystalvale', 'Serendale2.0']
        # Act
        actualSections = config.getSections()
        # Assert
        self.assertTrue(expected == actualSections)

    def test_get_options(self):
        # Arrange
        config = cfg.Config()
        expected = ['interval', 'sendtweets', 'senddiscord', 'debug', 'carvers', 'onehourmessage']
        # Act
        actualOptions = config.getOptions('bot')
        # Assert
        self.assertTrue(expected == actualOptions)

    def test_remove_section(self):
        # Arrange
        config = cfg.Config()
        # Act
        config.removeSection('bot')
        actualOptions = config.getSections()
        # Assert
        self.assertFalse('bot' in actualOptions)

    def test_remove_option(self):
        # Arrange
        config = cfg.Config()
        # Act
        config.removeOption('bot', 'interval')
        actualOptions = config.getOptions('bot')
        # Assert
        self.assertFalse('bot' in actualOptions)

    def test_add_section(self):
        # Arrange
        config = cfg.Config()
        expected = ['bot', 'Serendale1.0', 'Crystalvale', 'Serendale2.0', 'test']
        #Act
        config.addSection('test')
        actualSections = config.getSections()
        #Assert
        self.assertTrue(expected == actualSections)
    
    def test_display(self):
        # Arrange
        config = cfg.Config()
        expected = {
            'bot': {
                'interval': '60',
                'sendtweets': 'False',
                'senddiscord': 'True',
                'debug': 'True',
                'carvers': "['Crystalvale', 'Serendale2.0']",
                'onehourmessage': '{"Crystalvale": "False", "Serendale2.0": "False"}'
            },
            'Serendale1.0': {
                'rpc': 'https://api.harmony.one',
                'address': '0xfFB8a55676edA75954AB45a6Ce16F88b119dC511'
            },
            'Crystalvale': {
                'rpc': 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc',
                'address': '0xc32A0e963e50AAAED273A75425fC39902b0d0b3b'
            },
            'Serendale2.0': {
                'rpc': 'https://klaytn-rpc.gateway.pokt.network/',
                'address': '0x2A4906925b168C6983BdD777B034e566675ac7B3'
            }
        }

        # Act
        actual = config.display()

        # Assert
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
