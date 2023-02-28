<h1>nbamit</h1>
<p>a website for predicting nba games.</p>
<p>automticly scrapes game results from the web and uses glicko-2 rating system to asses team winning chanses. </p>
<p>the website is hosted at <a href="http://nbamit.herokuapp.com/">http://nbamit.herokuapp.com/</a>.</p>
<h2>runing the website localy</h2>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements:

```bash
pip install -r requirements.txt
```
and then run the website with:
```bash
python manage.py runserver --settings=nbamit.settings_local 
```
to run the tests use:
```bash
python manage.py test
```
<h2>Contributing</h2>

1. Fork it!
2. Create your feature branch:``` git checkout -b my-new-feature```
3. Commit your changes: ```git commit -am 'Add some feature'```
4. Push to the branch: ```git push origin my-new-feature```
5. Submit a pull request :D
<h2>License</h2>

[MIT](https://choosealicense.com/licenses/mit/)
