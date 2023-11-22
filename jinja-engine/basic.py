from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def hello_world():

 orang = {'nama': 'Toni Bin Suep', 'umur':'17tahun'}

 komentar = [

  {

   'penulis': {'nama': 'Upin'},

   'ucapan': 'hai Toni, artikel yang bagus'

  },

  {

   'penulis': {'nama': 'Ipin'},

   'ucapan': 'artikel ini cukup membantu saya'

  }

 ]

 return render_template('index.html', title='Beranda', orang=orang, komentar=komentar)