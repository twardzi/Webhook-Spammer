import customtkinter as ctk
import requests
from threading import Thread

def send_messages():
    webhook_url = webhook_entry.get()
    message = message_entry.get()
    count = int(count_entry.get())
    bot_name = bot_name_entry.get()
    bot_avatar = bot_avatar_entry.get()

    def send_message():
        for _ in range(count):
            payload = {"content": message}
            if bot_name:
                payload["username"] = bot_name
            if bot_avatar:
                payload["avatar_url"] = bot_avatar
            requests.post(webhook_url, json=payload)

    Thread(target=send_message).start()

app = ctk.CTk()
app.geometry("400x450")
app.title("Webhook Spammer")

ctk.CTkLabel(app, text="Webhook URL:").pack(pady=10)
webhook_entry = ctk.CTkEntry(app, width=300)
webhook_entry.pack()

ctk.CTkLabel(app, text="Message:").pack(pady=10)
message_entry = ctk.CTkEntry(app, width=300)
message_entry.pack()

ctk.CTkLabel(app, text="Number of messages:").pack(pady=10)
count_entry = ctk.CTkEntry(app, width=300)
count_entry.pack()

ctk.CTkLabel(app, text="Webhook name:").pack(pady=10)
bot_name_entry = ctk.CTkEntry(app, width=300)
bot_name_entry.pack()

ctk.CTkLabel(app, text="Webhook Icon (URL):").pack(pady=10)
bot_avatar_entry = ctk.CTkEntry(app, width=300)
bot_avatar_entry.pack()

send_button = ctk.CTkButton(app, text="Send messages", command=send_messages)
send_button.pack(pady=20)

ctk.CTkLabel(app, text="by twardzi_sigma").pack(pady=20)

app.mainloop()
