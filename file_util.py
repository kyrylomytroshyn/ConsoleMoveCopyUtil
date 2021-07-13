"""Utility for copy/move files from directory to directory with threads of without it."""
from glob import glob
from logging import debug
from os import system, listdir, chdir
from os.path import isdir
from pathlib import Path
from shutil import move, copy
from threading import Thread, current_thread


class FileUtil:

    def __init__(self, origin: str, destination: str):
        self.origin = str(Path(origin).absolute())
        self.destination = str(Path(destination).absolute())

    def _copy_move(self, files_list: list, operation: str) -> None:
        """
        Additional function for copy/move files.Realises functional of this action.

        Arguments:
            files_list: list with file names.
        """
        thread_name = current_thread().getName()
        for file in files_list:
            full_address = str(self.origin) + '/' + file
            try:
                if isdir(full_address):
                    system(f'{operation} "{full_address}" "{self.destination}"')
                else:
                    if operation == "cp":
                        copy(full_address, self.destination)
                    else:
                        move(full_address, self.destination)

                debug(f"{thread_name} SUCCESSFUL COPIED/MOVED  {full_address} to {self.destination}")
            except Exception as ex:
                debug(f"{thread_name} ERROR OF COPY/MOVE {full_address}. {ex}")

    def _get_equal_lists(self, this_size: int, this_list: list = None) -> list:
        """Returns list of equal-sizes lists(if we can divide it without float pointer)

        Arguments:
            this_list: optional, presents the origin files in list (not in file link)
            this_size: sets the size of new lists
        """
        if this_list is None:
            this_list = listdir(self.origin)

        size_list = len(this_list) // this_size

        return [this_list[i:i + size_list] for i in range(0, len(this_list), size_list)]

    def copy_move(self, action: str, threads: int = None) -> None:
        """Function for move/copy files:

        Arguments:
            action -> "move" for move, "copy" for copy
            threads -> optional, count of threads to move/copy files.
        """
        dir_size = len(listdir(action))
        if dir_size < threads:
            threads = dir_size

        action = action.replace('e', '').replace('o', '').replace('y', '')

        if threads is not None:
            temp_lists = self._get_equal_lists(threads)
            for i, lst in enumerate(temp_lists):
                Thread(target=self._copy_move, name=f'Thread {i}', args=(lst, action)).start()
        else:
            self._copy_move(listdir(self.origin), operation=action)

    def _parse_mask(self, pos: int):
        postfix = self.origin[pos:]
        self.origin = self.origin.replace(postfix, "")
        chdir(self.origin)
        return glob(postfix)

    def copy_move_mask(self, action: str, pos: int, threads: int = None) -> None:
        """Function for move/copy files with mask:

        Arguments:
            pos -> start mask position
            action -> "move" for move, "copy" for copy
            threads -> optional, count of threads to move/copy files.
        """
        list_of_files = self._parse_mask(pos)
        action = action.replace('e', '').replace('o', '').replace('y', '')

        dir_size = len(list_of_files)
        if dir_size < threads:
            threads = dir_size

        if threads is not None:
            temp_lists = self._get_equal_lists(threads, list_of_files)
            for i, lst in enumerate(temp_lists):
                Thread(target=self._copy_move, name=f'Thread {i}', args=(lst, action)).start()
        else:
            self._copy_move(list_of_files, operation=action)
