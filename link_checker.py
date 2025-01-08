import tkinter as tk
from tkinter.ttk import Progressbar
from turtledemo.penrose import start

import requests
from bs4 import BeautifulSoup
from tkinter import font



def check_website(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.MissingSchema:
        output_text.insert(tk.END, "Hatalı URL formatı. Lütfen tam bir URL girin.\n")
        return
    except requests.exceptions.ConnectionError:
        output_text.insert(tk.END, "Bağlantı hatası. Lütfen internet bağlantınızı kontrol edin.\n")
        return
    except Exception as e:
        output_text.insert(tk.END, f"Beklenmeyen bir hata oluştu: {e}\n")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    href = soup.find_all("a", href=True)

    new_links_found = False  # Yeni link bulunup bulunmadığını kontrol etmek için
    for link in href:
        href_value = link.get("href")
        if href_value not in url_list:
            if "http" in href_value:
                url_list.append(href_value)
                output_text.insert(tk.END ,href_value + "\n")  # Yeni linki metin alanına ekle
                new_links_found = True


    if not new_links_found:
        output_text.insert(tk.END, "Yeni link bulunamadı.\n")

url_list = []
print(len(url_list))


root = tk.Tk()
root.geometry('700x500')
root.title("Link Checker")

# Create a label
label = tk.Label(root, text="Enter URL", bg="#6693fa", fg="white", width=50, font=("Arial", 10, "bold"))
label.pack()



# Create an Entry widget
entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black", width=50)
entry.pack()
entry.insert(tk.END, "http://www.google.com")


# Create a button to run the function
button = tk.Button(root, text="RUN", activebackground="#b89c39", activeforeground="white",
                   width=10, command=lambda: check_website(entry.get()))
button.pack()

custom_font = font.Font(family="Arial", size=12, weight="normal")

# Quit button
quit_button = tk.Button(root, text="Quit", activebackground="#b89c39", activeforeground="white", command=root.destroy)
quit_button.pack()

# Output Label
output_label = tk.Label(root, text="Your Links", bg="#6693fa", fg="white", width=40, padx=10, font=("Arial", 14, "bold"))
output_label.pack()

#Scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Text box for output
output_text = tk.Text(root, height=20, width=70, bg="white", fg="black", yscrollcommand=scrollbar.set)
output_text.pack()

scrollbar.config(command=output_text.yview) #connect with textbox

root.mainloop()
