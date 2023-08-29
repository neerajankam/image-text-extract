import logging
from PIL import Image
import pytesseract
from pytesseract import TesseractNotFoundError
from sqlalchemy.exc import SQLAlchemyError, MultipleResultsFound
from db.connection import Database
from db.models import Extracts as ExtractsDB

# Path to the Tesseract executable (Update this with your installation path)
pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"


class Extract:
    def extract_text(self, uploaded_image: str) -> None:
        """
        Extract text from an uploaded image and add it to the database.

        :param uploaded_image: Path to the uploaded image file.
        :type uploaded_image: str
        """
        image = Image.open(uploaded_image)
        try:
            text = pytesseract.image_to_string(image, lang="eng")
        except TesseractNotFoundError:
            logging.critical(
                "Make sure tesseract is installed on the server and the path is set correctly."
            )
            return
        self.add_result_to_database(text)

    def get_text(self) -> str:
        """
        Get the extracted text from the database.

        :return: Extracted text.
        :rtype: str
        """
        return self.get_result_from_database()

    def add_result_to_database(self, text: str) -> None:
        """
        Add the extracted text to the database.

        :param text: Extracted text.
        :type text: str
        """
        try:
            with Database.get_session() as db_session:
                self.delete_result_from_database()
                row = ExtractsDB(content=text)
                db_session.add(row)
                db_session.commit()
        except SQLAlchemyError:
            logging.exception("Error while interacting with the database.")

    def delete_result_from_database(self) -> None:
        """Delete the existing result from the database."""
        try:
            with Database.get_session() as db_session:
                db_session.query(ExtractsDB).delete()
                db_session.commit()
        except SQLAlchemyError:
            logging.exception("Error while interacting with the database.")

    def get_result_from_database(self) -> str:
        """
        Get the extracted text from the database.

        :return: Extracted text.
        :rtype: str
        """
        try:
            with Database.get_session() as db_session:
                record = db_session.query(ExtractsDB).one()
            return record.content
        except SQLAlchemyError:
            logging.exception("Error while interacting with the database.")
        except MultipleResultsFound:
            logging.exception("Multiple results were found in the database.")
