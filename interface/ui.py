from typing import Any, List, Union

class Page:
    def __init__(self):
        """
        Create group
        """
        
        self.__attr_group: dict = {}
    
    def add(self, element: Any, draw_function: callable, id: str,
            type: str = "auto", event_functions: Union[List[callable], None] = None):
        """
        Add element to draw onto screen
        """
        
        if type not in ("event", "auto"):
            raise ValueError(f"'type' paramter must be 'event' or 'auto'. Instead received {type}")
        
        self.__attr_group[id] = {
            "element" : element,
            "draw": draw_function,
            "type": type,
            "efs" : event_functions # efs -> event functions
        }

    def update_event(self, event):
        """
        Call update event functions of all elements on page with type "event"
        """
        
        for _ in self.__attr_group.values():
            if _["type"] == "event":
                for func in _["efs"]:
                    func(event)
    
    def update_auto(self):
        """
        Call update default functions of all elements on page
        """
        
        for _ in self.__attr_group.values():
            _["draw"]()
    
    def remove_element(self, id: str):
        """
        Remove element from page
        """
        
        del self.__attr_group[id]
    
    def clear_page(self):
        """
        Clear all elements belonging to the page
        """
        self.__attr_group = {}
        
class PageGroup:
    def __init__(self):
        """
        Create page group
        """
        self.__pages: dict = {}
        self.__selected_page: Union[Page, None] = None
    
    def add(self, page: Page, id: str):
        """
        Add a page to the page group
        """
        
        self.__pages[id] = page
    
    def remove(self, id: str):
        """
        Remove a page (identified by page ID)
        """
        del self.__pages[id]
    
    def clear_group(self):
        """
        Clear all pages from page group
        """
        
        self.__pages = {}
    
    def select_page(self, id: str):
        """
        Select page to be displayed onto screen
        """
        self.__selected_page = self.__pages[id]
    
    def update_event(self, event):
        """
        Update the selected page based on event that happens
        """
        if not self.__selected_page:
            raise ValueError("No page selected")
        self.__selected_page.update_event(event=event)
    
    def update_auto(self):
        """
        Update selected page based on default function
        """
        if not self.__selected_page:
            raise ValueError("No page selected")
        self.__selected_page.update_auto()