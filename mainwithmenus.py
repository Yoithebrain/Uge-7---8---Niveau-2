from src_code.ui.StartMenu import StartMenu
from src_code.db.Database import Database
def main():
    db = Database()
    session = db.Session()
    start_menu = StartMenu(session)
    start_menu.start()
    session.close()
if __name__ == "__main__":
    main()