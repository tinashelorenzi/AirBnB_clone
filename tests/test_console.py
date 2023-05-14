import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        self.cli = None

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel " + created_id)
            output = f.getvalue().strip()
        self.assertTrue(created_id in output)

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.cli.onecmd("quit")

    def test_EOF(self):
        with self.assertRaises(SystemExit):
            self.cli.onecmd("EOF")

    def test_emptyline(self):
        self.assertFalse(self.cli.onecmd(""))

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel " + created_id)
            output = f.getvalue().strip()
        self.assertTrue(created_id in output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        self.assertTrue(created_id in [obj.id for obj in self.cli.classes["BaseModel"].all().values()])
        self.cli.onecmd("destroy BaseModel " + created_id)
        self.assertFalse(created_id in [obj.id for obj in self.cli.classes["BaseModel"].all().values()])

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            created_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"update BaseModel {created_id} name 'test'")
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"show BaseModel {created_id}")
            output = f.getvalue().strip()
        self.assertTrue("test" in output)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.cli.onecmd("create User")
            self.cli.onecmd("all")
            output = f.getvalue().strip()
        self.assertTrue("BaseModel" in output)
        self.assertTrue("User" in output)
