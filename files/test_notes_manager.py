import unittest
import os
from notes_manager import (
    init_notes_dir,
    add_note,
    list_notes,
    read_note,
    edit_note,
    delete_note,
    search_notes,
)


class TestNotesManager(unittest.TestCase):

    def setUp(self):
        """
        Виконується перед кожним тестом.
        Тут можна створювати тимчасову папку для тестів.
        """
        pass

    def tearDown(self):
        """
        Виконується після кожного тесту.
        Тут можна чистити тимчасову папку.
        """
        pass

    def test_init_notes_dir(self):
            init_notes_dir(),


    def test_add_note(self):
            add_note('note 1', 'This is content')
        

    def test_list_notes(self):
            list_notes()

    def test_read_note(self):
            read_note('./notes/read_example.txt')

    def test_edit_note_append(self):
            edit_note('./notes/read_example.txt', "fifth string", True)

    def test_edit_note_overwrite(self):
        pass

    def test_delete_note(self):
        pass

    def test_search_notes(self):
        pass


if __name__ == "__main__":
    unittest.main()
