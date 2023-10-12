import requests

def count_words(subreddit, word_list, instances=None, after=None, count=0):
    if instances is None:
        instances = {}
        
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "YourUserAgent"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        print("Invalid subreddit or no posts found.")
        return
    elif response.status_code != 200:
        print("Error while fetching data from Reddit.")
        return

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")

    for post in data.get("children"):
        title = post.get("data").get("title").lower()
        for word in word_list:
            word_count = title.count(word.lower())
            if word_count > 0:
                if word not in instances:
                    instances[word] = 0
                instances[word] += word_count

    if after is None:
        sorted_instances = sorted(instances.items(), key=lambda x: (-x[1], x[0]))
        for word, word_count in sorted_instances:
            print(f"{word}: {word_count}")
    else:
        count_words(subreddit, word_list, instances, after, count)

# Example usage
subreddit = "programming"
word_list = ["python", "javascript", "java"]
count_words(subreddit, word_list)
