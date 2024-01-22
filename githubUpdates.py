from git import Repo, exc

PATH_OF_GIT_REPO = r'.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'New Emails!'

def git_pull():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        origin = repo.remote(name='origin')
        origin.fetch()
        repo.git.merge('FETCH_HEAD')
        print('Successfully pulled from the repository')
    except exc.GitCommandError as e:
        print(f'Error occurred while pulling: {e}')

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        print('Successfully pushed to the repository')
    except exc.GitCommandError as e:
        print(f'Error occurred while pushing: {e}')
