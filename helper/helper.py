from utils.logger import logger
import random

class Helper:
    """Utility helper class to provide reusable methods across the framework."""

    @staticmethod
    def get_random_book(books):
        """Select a random book from a list of books and return its ID."""
        try:
            # Pick a random book
            random_book = random.choice(books)
            book_id = random_book.get("bookId")
            logger.debug(f"Random Book ID generated: {book_id}")
            return book_id
        except Exception as e:
            logger.error(f"Error in Helper - Pick a random book: {e}")