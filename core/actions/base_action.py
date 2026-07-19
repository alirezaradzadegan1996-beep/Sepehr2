from abc import ABC, abstractmethod


class BaseAction(ABC):
    """
    کلاس پایه برای تمام Actionهای سپهر
    """

    name = "base"

    @abstractmethod
    def execute(self, context):
        """اجرای اکشن"""
        raise NotImplementedError
