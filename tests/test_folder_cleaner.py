from unittest.mock import patch
from src.main import showFolder

class TestFolderCleaner():
        @patch('os.scandir')
        @patch('os.listdir')
        def test_empty_folder(self,mock_scandir):
            mock_scandir.return_value.__iter__.return_value = []
            result = showFolder("/fake/path")
            assert result == "Folder is empty"
    