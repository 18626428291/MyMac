
"""
Created on Thu Jun  6 14:51:13 2019

@author: xujiajun
"""

from flask import Flask,url_for
app = Flask(__name__)


@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index',username='shixiaolou'))
    print(url_for('show_post',post_id=1,_external=True))
    print(url_for('show_post',post_id=2,q='python03'))
    print(url_for('show_post',post_id=2,q='python is ok'))
    print(url_for('show_post',post_id=2,))
    