from tkinter import *
from PIL import Image
from PIL import ImageTk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


ds = pd.read_csv(r'C:\Users\NIKHIL\Desktop\AI project\sample-data.csv')

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(ds['description'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

results = {}

for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

    results[row['id']] = similar_items[1:]


def item(id):
    return ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0]


def recommend(item_id, num):
    print("Recommending " + str(num) + " products similar to " + item(item_id) + "...")
    print("-------")
    recs = results[item_id][:num]
    for rec in recs:
        print("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")


def onclick1(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[1][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()


def onclick2(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[2][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()


def onclick3(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[3][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()


def onclick4(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[4][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()


'''def onclick5(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[4][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()
'''

def onclick5(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[5][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()


def onclick6(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[6][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()


def onclick7(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[4][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()


def onclick8(event):
    root2 = Toplevel()
    label1 = Label(root2, text='Recommended Items')
    label1.pack()
    label1.config(font=("Courier", 44))
    recs = results[4][:5]
    for rec in recs:
        a = ("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
        label = Label(root2, text=a)
        label.pack()
        label.config(font=("Courier", 18))
    root2.mainloop()


def product_list():
    root1 = Toplevel()
    f1 = Frame(root1, width=300, height=100)
    f1.grid(row=100, column=200)
    photo1_1 = Image.open(r'C:\Users\NIKHIL\Desktop\AI project\ActiveClassicBoxer.png')
    photo1_2 = photo1_1.resize((100, 100), Image.ANTIALIAS)
    photo1_3 = ImageTk.PhotoImage(photo1_2)
    l1 = Label(f1, image=photo1_3)
    l1.grid(row=3, column=2)
    B1 = Button(f1, text="Active Classic Boxer")
    B1.grid(row=3, column=200)
    B1.bind('<Button-1>', onclick1)
    photo2_1 = Image.open(r'C:\Users\NIKHIL\Desktop\AI project\ActiveSportsBoxer.png')
    photo2_2 = photo2_1.resize((100, 100), Image.ANTIALIAS)
    photo2_3 = ImageTk.PhotoImage(photo2_2)
    l2 = Label(f1, image=photo2_3)
    l2.grid(row=8, column=2)
    B2 = Button(f1, text="Active Sports Boxer")
    B2.grid(row=8, column=200)
    B2.bind("<Button-1>", onclick2)
    photo3_1 = Image.open(r'C:\Users\NIKHIL\Desktop\AI project\ActiveSportsBriefs.png')
    photo3_2 = photo3_1.resize((100, 100), Image.ANTIALIAS)
    photo3_3 = ImageTk.PhotoImage(photo3_2)
    l3 = Label(f1, image=photo3_3)
    l3.grid(row=20, column=2)
    B3 = Button(f1, text="Active Sports Briefs")
    B3.grid(row=20, column=200)
    B3.bind('<Button-1>', onclick3)
    photo4_1 = Image.open(r'C:\Users\NIKHIL\Desktop\AI project\Alpine guide pants.png')
    photo4_2 = photo4_1.resize((100, 100), Image.ANTIALIAS)
    photo4_3 = ImageTk.PhotoImage(photo4_2)
    l4 = Label(f1, image=photo4_3)
    l4.grid(row=18, column=2)
    B4 = Button(f1, text="Alpine guide pants")
    B4.grid(row=18, column=200)
    B4.bind("<Button-1>", onclick4)
    photo5_1 = Image.open(r'C:\Users\NIKHIL\Desktop\AI project\Alpine wind jkt.png')
    photo5_2 = photo5_1.resize((100, 100), Image.ANTIALIAS)
    photo5_3 = ImageTk.PhotoImage(photo5_2)
    l5 = Label(f1, image=photo5_3)
    l5.grid(row=23, column=2)
    B5 = Button(f1, text="Alpine wind jacket")
    B5.grid(row=23, column=200)
    B5.bind("<Button-1>", onclick5)
    photo6_1 = Image.open(r'C:\Users\NIKHIL\Desktop\AI project\Ascensionist jkt.png')
    photo6_2 = photo6_1.resize((100, 100), Image.ANTIALIAS)
    photo6_3 = ImageTk.PhotoImage(photo6_2)
    l6 = Label(f1, image=photo6_3)
    l6.grid(row=28, column=2)
    B6 = Button(f1, text="Ascensionist jacket")
    B6.grid(row=28, column=200)
    B6.bind("<Button-1>", onclick6)
    photo7_1 = Image.open(r'C:\Users\NIKHIL\Desktop\AI project\Baby sun bucket hat.png')
    photo7_2 = photo7_1.resize((100, 100), Image.ANTIALIAS)
    photo7_3 = ImageTk.PhotoImage(photo7_2)
    l7 = Label(f1, image=photo7_3)
    l7.grid(row=33, column=2)
    B7 = Button(f1, text="Baby sun bucket hat")
    B7.grid(row=33, column=200)
    B7.bind("<Button-1>", onclick7)
    photo8_1 = Image.open(r'C:\Users\NIKHIL\Desktop\AI project\Baby sunshade top.png')
    photo8_2 = photo8_1.resize((100, 100), Image.ANTIALIAS)
    photo8_3 = ImageTk.PhotoImage(photo8_2)
    l8 = Label(f1, image=photo8_3)
    l8.grid(row=40, column=2)
    B8 = Button(f1, text="Baby sun bucket hat")
    B8.grid(row=40, column=200)
    B8.bind("<Button-1>", onclick8)
    root1.mainloop()


product_list()
