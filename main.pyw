import tkinter as tk
import json

file_address = "data.json"


def donothing():
    pass


def add():
    global file_address

    def confirm():
        file = open(file_address, 'r')
        contents = json.loads(file.read())
        file.close()

        contents.append({
            "name": ent_album.get(),
            "artist": ent_artist.get(),
            "year": ent_year.get(),
            "genre": ent_genre.get()
        })

        contents_json = json.dumps(contents)
        file = open(file_address, 'w')
        file.write(contents_json)
        file.close()

        update()

    popup = tk.Toplevel(root)

    lbl_album = tk.Label(popup, text="Album:\t")
    lbl_artist = tk.Label(popup, text="Atrist:\t")
    lbl_genre = tk.Label(popup, text="Genre:\t")
    lbl_year = tk.Label(popup, text="Year:\t")

    ent_album = tk.Entry(popup)
    ent_artist = tk.Entry(popup)
    ent_genre = tk.Entry(popup)
    ent_year = tk.Entry(popup)

    btn_confirm = tk.Button(popup, text="Add", command=confirm)

    blank1 = tk.Label(popup, text="           ")
    blank2 = tk.Label(popup, text="           ")

    lbl_album.grid(row=1, column=1)
    lbl_artist.grid(row=2, column=1)
    lbl_genre.grid(row=3, column=1)
    lbl_year.grid(row=4, column=1)
    ent_album.grid(row=1, column=2)
    ent_artist.grid(row=2, column=2)
    ent_genre.grid(row=3, column=2)
    ent_year.grid(row=4, column=2)
    btn_confirm.grid(row=5, column=2)

    blank1.grid(row=0, column=0)
    blank2.grid(row=6, column=3)


root = tk.Tk()
root.geometry("500x500")

# making elements
lbl_genre = tk.Label(root, text="Genre")
lbl_album = tk.Label(root, text="Album")
lbl_artist = tk.Label(root, text="Artist")
lbl_year = tk.Label(root, text="Year")
lbl_blank = tk.Label(root, text="           ")

# making menubar
menu = tk.Menu(root)

filemenu = tk.Menu(menu, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menu, tearoff=0)
editmenu.add_command(label="Add", command=add)
editmenu.add_command(label="remove", command=donothing)
menu.add_cascade(label="Edit", menu=editmenu)

findmenu = tk.Menu(menu, tearoff=0)

root.config(menu=menu)

# reading the json file and dsiplaying albums #
# obtaining file contents
file = open(file_address, 'r')
contents = file.read()
file.close()

# converting json to python
album_list = json.loads(contents)


# displaying elements
lbl_blank.grid(row=0, column=0)
lbl_album.grid(row=1, column=1)
lbl_artist.grid(row=1, column=2)
lbl_year.grid(row=1, column=3)
lbl_genre.grid(row=1, column=4)


# entering every album data
def update():
    for i in range(len(album_list)):
        lbl_album = tk.Label(root, text=album_list[i]["name"])
        lbl_artist = tk.Label(root, text=album_list[i]["artist"])
        lbl_year = tk.Label(root, text=album_list[i]["year"])
        lbl_genre = tk.Label(root, text=album_list[i]["genre"])

        row_num = i + 2
        lbl_album.grid(row=row_num, column=1)
        lbl_artist.grid(row=row_num, column=2)
        lbl_year.grid(row=row_num, column=3)
        lbl_genre.grid(row=row_num, column=4)


update()

root.mainloop()
