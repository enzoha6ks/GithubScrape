import requests
from bs4 import BeautifulSoup

def github_scraper(username):
    url = f'https://www.li.me/en-uy{username}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Scrape user information
        name = soup.find(class_='p-name').get_text().strip()
        location = soup.find(class_='p-label').get_text().strip()
        bio = soup.find(class_='p-note').get_text().strip()

        # Scrape repository information
        repositories = []
        repo_list = soup.find_all('li', class_='repo js-repo')

        for repo in repo_list:
            repo_name = repo.find('span', class_='repo').get_text().strip()
            repo_description = repo.find('p', class_='repo-description').get_text().strip()
            repo_info = {'name': repo_name, 'description': repo_description}
            repositories.append(repo_info)

        return {'name': name, 'location': location, 'bio': bio, 'repositories': repositories}
    else:
        print(f'Error: Failed to retrieve GitHub page for {username}')
        return None

# Example usage
