import tkinter as tk
import random

# توليد رقم عشوائي
secret_number = random.randint(1, 10)
attempts = 0

def check_guess():
    global attempts
    guess = entry.get()

    if not guess.isdigit():
        result_label.config(text="❌ أدخل رقم فقط", fg="red")
        return

    guess = int(guess)
    attempts += 1

    if guess == secret_number:
        result_label.config(text=f"✅ صحيح! الرقم هو {secret_number} 🎉\nعدد المحاولات: {attempts}", fg="green")
        submit_button.config(state="disabled")
    elif guess < secret_number:
        result_label.config(text="📈 الرقم أكبر", fg="blue")
    else:
        result_label.config(text="📉 الرقم أصغر", fg="blue")

# واجهة البرنامج
window = tk.Tk()
window.title("لعبة التخمين")
window.geometry("300x200")

label = tk.Label(window, text="🔢 أدخل رقم بين 1 و 10:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

submit_button = tk.Button(window, text="تحقق", command=check_guess)
submit_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
