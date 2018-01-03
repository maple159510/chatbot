from transitions.extensions import GraphMachine
import telegram
API_TOKEN = '519466420:AAEqkUKvoHwqHCAcmSVN6zQmRk-TY4YPid0'
bot = telegram.Bot(token=API_TOKEN)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'go to state3'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'go to state4'

    def on_enter_state1(self, update):
        update.message.reply_text("Basic Problem--SET\n")
        bot.send_photo(chat_id = update.message.chat.id, photo = open('BotResource/set1.jpg','rb'))
        update.message.reply_text("Black first. Choose the best answer.\nRespond with 'A' or 'B'.\nIf you want to go back, please type 'back'.\n")
        while 1:
            text = update.message.text
            if text == 'A':
                update.message.reply_text("Correct! The answer is A.\n")
                bot.send_photo(chat_id = update.message.chat, photo = open('BotResource/set1ans.jpg','rb'))
            
            elif text == 'B':
                update.message.reply_text("Wrong.\nIf you want to see the correct answer, please type 'answer'.")
            
            elif text == 'answer':
                bot.send_photo(chat_id = update.message.chat, photo = open('BotResource/set1ans.jpg','rb'))
                update.message.reply_text("The correct answer is A.\n")

            elif text =='back':
                self.go_back(update)
            
            elif text:
                text = text
            else :
                update.message.reply_text("Please respond with 'A', 'B', or 'C'.\n")

    def on_enter_state2(self, update):
        update.message.reply_text("Technical Problem--EAT\n")
        bot.send_photo(chat_id = update.message.chat.id, photo = open('BotResource/eat1.jpg','rb'))
        update.message.reply_text("Black first. Choose the best answer.\n Respond with 'A', 'B', or 'C'.\n")
        if update.message.text == 'A':
            update.message.reply_text("\n")
        elif update.message.text == 'B':
            update.message.reply_text("\n")
        elif update.message.text == 'C':
            update.message.reply_text("\n")
        else :
            update.message.reply_text("Please respond with 'A', 'B', or 'C'.\n")
        self.go_back(update)

    def on_enter_state3(self, update):
        update.message.reply_text("Technical Problem--BROKE EYE\n")
        bot.send_photo(chat_id = update.message.chat.id, photo = open('BotResource/broke1.jpg','rb'))
        update.message.reply_text("Black first. Choose the best answer.\n Respond with 'A', 'B', or 'C'.\n")
        if update.message.text == 'A':
            update.message.reply_text("\n")
        
        elif update.message.text =='B':
            update.message.reply_text("\n")

        elif update.message.text =='C':
            update.message.reply_text("\n")
        else :
            update.message.reply_text("Please respond with 'A', 'B', or 'C'.\n")
        
        self.go_back(update)

    def on_enter_state4(self, update):
        update.message.reply_text("Advanced Problem--DEATH LIVE\n")
        bot.send_photo(chat_id = update.message.chat.id, photo = open('BotResource/death1.jpg','rb'))
        update.message.reply_text("Black first. Choose the best answer.\n Respond with 'A', 'B', or 'C'.\n")
        if update.message.text == 'A':
            update.message.reply_text("\n")
            
        elif update.message.text =='B':
            update.message.reply_text("\n")

        elif update.message.text =='C':
            update.message.reply_text("\n")

        else :
            update.message.reply_text("Please respond with 'A', 'B', or 'C'.\n")
        
        self.go_back(update)


    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_exit_state3(self, update):
        print('Leaving state3')
    
    def on_exit_state4(self, update):
        print('Leaving state4')
