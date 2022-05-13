from abc import ABC, abstractmethod


class Crawler(ABC):
    """Generic Crawler Type"""

    @abstractmethod
    def __init__(self, sources: list = []):
        self.__sources = sources

    @property
    def sources(self) -> list:
        return self.__sources

    @sources.setter
    def sources(self, sources: list):
        self.__sources = sources

    @abstractmethod
    def dig(self) -> dict:
        pass
