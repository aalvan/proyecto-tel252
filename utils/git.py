
from git import Repo

def git_push(commit_message):
    try:
        repo = Repo('/Users/alexisalva/USM-2022-2/cripto/proyecto-TEL252/.git')
        repo.git.add('--all')
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('There was a problem doing push')    

def git_pull():
    try:
        repo = Repo('.\proyecto-TEL252.git')
        origin = repo.remote(name='origin')
        origin.pull()
    except:
        print("Error")