from app.controllers.message_controller import MessageController

def main():
    menssagem = "Olá {name}, tudo bem com você?"
    MessageController.send_message_to_all_users(menssagem)

if __name__ == "__main__":
    main()
