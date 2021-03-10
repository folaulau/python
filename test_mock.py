
from mock import MagicMock
import functions


if __name__ == '__main__':
    functions.multiply = MagicMock()
    functions.multiply.return_value = 9
    functions.multiply.assert_called_with(2,3)