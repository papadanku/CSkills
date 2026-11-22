
# Unit Testing & Mocking Guide - Project Reality Python

Project Reality includes a custom unit test suite located in `unit_tests/` utilizing Python's `unittest` module and the `pmock` mocking library.

## 1. Test File Structure (`*_spec.py`)

Test files reside in `unit_tests/tests/` (or subdirectories like `realityadmin/`) and follow the `*_spec.py` naming convention.

```python
import unittest
import game.realitystats as realitystats
import bf2
import pmock

class realitystats_onPlayerConnectMaxPlayers(unittest.TestCase):
    oldPlayerManager = None
    playerCount = 10
    playerChange = 5

    def setUp(self):
        playerManagerMock = pmock.Mock()
        playerManagerMock.stubs().getNumberOfPlayers().will(pmock.return_value(self.playerCount))

        self.oldPlayerManager = bf2.playerManager
        bf2.playerManager = playerManagerMock

    def tearDown(self):
        bf2.playerManager = self.oldPlayerManager

    def test_playerJoined_belowMax(self):
        # Test assertions
        self.assertEqual(realitystats.g_maxPlayers, 15)
```

## 2. Mocking Engine Objects with `pmock`

When testing modules that interact with `bf2` or `realityserver`, mock out underlying dependencies in `setUp()` and restore them in `tearDown()` to maintain test isolation.
