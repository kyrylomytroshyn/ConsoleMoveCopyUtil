"""Utility for copy/move files from directory to directory"""
import shutil


class FileUtil:

    def __init__(self, origin: str, destination: str):
        self.origin = origin
        self.destination = destination

    def copy(self, threads: int = None) -> None:
        """Function for copy files:

        Arguments:
            threads -> optional, count of threads to copy files.
        """
        if threads is not None:
            pass
        else:
            shutil.copy(self.origin, self.destination)

    def move(self, threads: int = None) -> None:
        """Function for copy files:

        Arguments:
            threads -> optional, count of threads to copy files.
        """
        if threads is not None:
            pass
        else:
            shutil.move(self.origin, self.destination)
