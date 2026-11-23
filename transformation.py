import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).with_name("contacts.db")


def create_database():
	"""Create the local SQLite database and contacts table if needed."""
	with sqlite3.connect(DATABASE_PATH) as connection:
		connection.execute(
			"""
			CREATE TABLE IF NOT EXISTS contacts (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				phone_number TEXT NOT NULL
			)
			"""
		)


def add_contact(name, phone_number):
	"""Save a contact to the local database."""
	with sqlite3.connect(DATABASE_PATH) as connection:
		connection.execute(
			"INSERT INTO contacts (name, phone_number) VALUES (?, ?)",
			(name, phone_number),
		)


def get_contacts():
	"""Return contacts as (id, name, phone_number) tuples."""
	with sqlite3.connect(DATABASE_PATH) as connection:
		return connection.execute(
			"SELECT id, name, phone_number FROM contacts ORDER BY name"
		).fetchall()


if __name__ == "__main__":
	create_database()
	print(f"Local contacts database ready: {DATABASE_PATH}")
