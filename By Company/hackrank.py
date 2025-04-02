#
# Complete the 'getAuthorHistory' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING author as parameter.
#
# Base urls:
#   https://jsonmock.hackerrank.com/api/article_users?username=
#   https://jsonmock.hackerrank.com/api/articles?author=
#
"""
Initialize the history array to store a list of string elements. 
Query https://jsonmock.hackerrank.com/api/article_users?username=<authorName>(replace <authorName>) to retrieve author information in the  data field.
Store the value of the about field from the query response.  If the about field is empty or null, do not store a value for this item.
Query https://jsonmock.hackerrank.com/api/articles?author=<authorName>(replace <authorName>), to retrieve the list of author's articles in the data field.
Add the title from each record returned in the data field to the history array. 
If the title field is null or empty then use the story_title to add in the history array.
If the title and story_title fields are null or empty then ignore the record to add in the history array.
Based on the total_pagescount, fetch all the data (pagination), and repeat steps 4 and 5.
Return the history array.
"""
import requests

def getAuthorHistory(author):
    history = []
    
    try:
        # query author info
        author_url = f"https://jsonmock.hackerrank.com/api/article_users?username={author}"
        author_response = requests.get(author_url)
        author_data = author_response.json()
        #print(author_data)
        
        # check if about is in the author_data
        author_about = None
        if author_data.get('data') and len(author_data['data']) > 0:
            about = author_data['data'][0].get('about')
            if about: #and about.strip():
                author_about = about
                history.append(about)
        
        seen_titles = set()
        current_page = 1
        total_page = 1
        while current_page <= total_page:
            # query list of author articles 
            articles_url = f"https://jsonmock.hackerrank.com/api/articles?author={author}&page={current_page}"
            articles_response = requests.get(articles_url)
            articles_data = articles_response.json()
            #print("test in articles")
            #print(articles_data)
            total_page = articles_data.get('total_pages')
            if articles_data.get('data'):
                for article in articles_data['data']:
                    title = article['title']
                    story_title = article['story_title']
                    if title and title not in seen_titles:
                        history.append(title)
                        seen_titles.add(title)
                    elif story_title and story_title not in seen_titles:
                        history.append(story_title)
                        seen_titles.add(story_title)
                    else:
                        continue
            current_page += 1  
        
        return history
    except Exception as e:
        print("Error fetching author data.")
        raise