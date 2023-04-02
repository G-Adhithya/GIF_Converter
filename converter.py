import imageio
import os
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def converter():
    text = link.get()
    inputPath = os.path.abspath(text)

    directory = "Videos"

    if not os.path.isdir(directory):
        os.mkdir(directory)

    outputPath = f"./Videos/{text}_converted.gif"

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()["fps"]

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)

    print("Done!")
    writer.close()


app = customtkinter.CTk()
app.geometry("720x405")
app.title("GIF Converter")
app.resizable(False, False)

# Icon
app.iconbitmap(
    "E:\\Adhithya\\Programming\\Tutorials\\Python\\gif_converter\\converter.ico")

# Label
title = customtkinter.CTkLabel(app, text="GIF Converter", font=("", 25))
title.pack(padx=10, pady=45, anchor=tkinter.CENTER)

instruction = customtkinter.CTkLabel(
    app, text="Paste the video in this directory and type the name of the video file")
instruction.pack()

# Text input
link = customtkinter.CTkEntry(app, 450, 50, 50)
link.pack(anchor=tkinter.CENTER, pady=45)

# Button
download_btn = customtkinter.CTkButton(
    app, 150, 50, 50, text="Convert", command=converter)
download_btn.pack(padx=20)


app.mainloop()
