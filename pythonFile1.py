def zad9UNIT():
    def fetch_data_from_db(query, database):
        try:
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            connection.close()
            return result
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return None

    class TestDBQuery(unittest.TestCase):
        def test_db_query(self):
            database = ':memory:'  # In-memory database for testing
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE test_table (id INTEGER, name TEXT, age INTEGER)')
            cursor.execute('INSERT INTO test_table (id, name, age) VALUES (1, "John Doe", 30)')
            cursor.execute('INSERT INTO test_table (id, name, age) VALUES (2, "Jane Smith", 25)')
            connection.commit()
            connection.close()

            query = 'SELECT * FROM test_table'
            expected_result = [
                (1, 'John Doe', 30),
                (2, 'Jane Smith', 25)
            ]

            result = fetch_data_from_db(query, database)
            self.assertEqual(result, expected_result)

    unittest.main(argv=[''], verbosity=2, exit=False)

