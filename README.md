1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Membuat sebuah proyek Django baru.

* Membuat repositori GitHub baru dengan nama GMart
* Membuat direktori lokal bernama GMart dan inisiasikan dengan `git init` dan hubungkan dengan repositori github tersebut dengan perintah `git remote add origin <URL_GMart>`
* buat file `requirements.txt` dengan beberapa _dependencies_
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
* buat _virtual environment_ dengan perintah `python -m venv env` dan aktifkan dengan perintah `env\Scripts\activate.bat`
* install _dependencies_ tadi dengan perintah `pip install -r requirements.txt`
* buat proyek Django dengan nama GMart dengan perintah `django-admin startproject GMart .`
* Tambahkan `*` pada ALLOWED_HOSTS di `settings.py` untuk keperluan deployment.
* Buat berkas `.gitignore` di repositori lokal yang berisi:
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

- [x] Membuat aplikasi dengan nama main pada proyek tersebut.

* aktifkan _virtual environment_ dan buat aplikasi baru `main` dalam proyek GMart dengan perintah `python manage.py startapp main`
* Mendaftarkan `main` dalam proyek dengan menambahkan `'main'` pada variabel `INSTALLED_APPS` di dalam berkas `settings.py` pada direktori `GMart`

```
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```

-  Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.

* buat berkas `urls.py` di dalam direktori `main` yang berisi:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
* Buka berkas `urls.py` di dalam direktori proyek GMart, impor fungsi `include` dari `django.urls`
```
...
from django.urls import path, include
...
```
* tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`
```
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```

- [x] membuat model pada aplikasi `main`

* isi berkas models.py pada direktori aplikasi `main` dengan kode:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    type = models.TextField()
```

* migrasi model dengan perintah:
```
python manage.py makemigrations
```
* migrasi ke dalam basis data lokal dengan perintah:
```
python manage.py migrate
```

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas

* membuat direktori `templates` pada direktori aplikasi `main`
* buat berkas `main.html` pada direktori `templates` yang berisi:
```
<h1>GMart Page</h1>

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```
* buka berkas `views.py` yang terletak di dalam berkas aplikasi `main` dan isi dengan
```
def show_main(request):
    context = {
        'name': 'Rafi Ghani Harditama',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
```

- [x] Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`

* buat berkas `urls.py` di dalam direktori `main`
* isi urls.py dengan kode berikut.
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

- [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat

* Lakukan `add`, `commit`, dan `push` dari direktori repositori lokal ke repositori GMart di GitHub dengan menggunakan perintah
```
git add .
```
```
git commit -m "<KOMENTAR>"
```
```
git push -u origin main
```

* Masuk ke _website_ Adaptable.io dan tombol `New App`. Pilih `Connect an Existing Repository`
* Pilihlah repositori proyek `GMart` sebagai basis aplikasi yang akan di-_deploy_. Pilih _branch_ yang ingin dijadikan sebagai _deployment branch_
* Pilihlah `Python App Template` sebagai _template deployment_
* Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan
* Pilih Phyton versi 3.11
* Pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn shopping_list.wsgi`
* Masukkan nama aplikasi yang akan menjadi _domain_ web
* Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![image](https://github.com/RafGhan/GMart/assets/124992862/a331d954-37ce-4a1e-af81-fb217799221b)


* User: merupakan pengguna(user) yang menjalankan/mengakses web aplikasi
* URLConf(`urls.py`): file yang berfungsi untuk mengatur pola URL yang akan diatur oleh views dalam aplikasi
* Model (`models.py`): file yang berfungsi untuk mendefinisikan struktur data aplikasi dan logika bisnis yang akan disimpan dalam database.
* View (`views.py`): file yang berfungsi sebagai tempat menyimpan model data kita dan hubungan antara data-data tersebut di dalam database
* Template: file HTML yang berfungsi untuk mengatur tampilan dalam aplikasi web. 
* Database: Tempat dimana aplikasi web disimpan secara permanen. 

Dalam pengembangan aplikasi web dengan Django, `urls.py` mengatur pola URL yang mengarahkan permintaan pengguna ke fungsi-fungsi views di `views.py`. Views berperan sebagai perantara antara model di `models.py` dan file template. Saat user melakukan permintaan, `urls.py` menentukan views yang akan menangani permintaan tersebut. Kemudian, views menggunakan model dari `models.py` untuk mengakses data dalam database sesuai dengan permintaan. Selanjutnya, views merender file Template yang sesuai dengan data dan mengirim respons ke pengguna sebagai halaman web. 

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

_Virtual environment_ adalah alat yang digunakan untuk menciptakan suatu ruang lingkup virtual yang terisolasi secara independen dari _dependencies_ utama. Dengan _virtual environment_, dapat memungkinkan kita untuk menghindari konflik dari _dependencies-dependecies_ yang dapat saling bertabrakan.

Walaupun kita dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_, sangat disarankan untuk tetap menggunakan _virtual environment_ dalam pengembangan Django. Hal tersebut karena menggunakan _virtual environment_ merupakan _best practice_ karena dapat membantu proyek tetap terorganisir, mencegah terjadinya konflik, dan memudahkan manajemen dependensi. Dengan demikian, membuat aplikasi web berbasis Django dengan menggunakan _virtual environment_ merupakan _best practice_ dan lebih efektif dibandingkan dengan tidak menggunakannya.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

* MVC (Model-View-Controller) adalah konsep arsitektur yang memisahkan aplikasi menjadi 3 komponen yaitu Model, View dan Controller
  + Model: Komponen yang bertanggung jawab untuk mengatur dan mengelola data dari aplikasi
  + View: komponen yang menangani logika presentasi. View mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna
  + Controller: komponen yang menghubungkan model dan view dalam setiap proses request dari user
    
* MVT (Model-View-Template) adalah konsep arsitektur yang memisahkan aplikasi menjadi 3 komponen yaitu Model, View dan Template
  + Model: Komponen yang bertanggung jawab untuk mengatur dan mengelola data dari aplikasi
  + View: komponen yang menangani logika presentasi. View mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna
  + Template: komponen yang berfungsi untuk mengatur tampilan atau antarmuka pengguna
    
* MVVM (Model-View-ViewModel)adalah konsep arsitektur yang memisahkan aplikasi menjadi 3 komponen yaitu Model, View dan ViewModel
  + Model: Komponen yang bertanggung jawab untuk mengatur dan mengelola data dari aplikasi
  + View: komponen yang menangani logika presentasi. View mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna
  + ViewModel: komponen yang berfungsi untuk berinteraksi dengan model di mana data yang ada akan diteruskan ke layer view

Perbedaan ketiganya terletak pada bagaimana komponen-komponen tersebut saling berinteraksi dan memisahkan tanggung jawab mereka dalam pengembangan aplikasi. MVC lebih terfokus pada pengendalian aliran aplikasi, MVT memisahkan tampilan dengan markup HTML
    
