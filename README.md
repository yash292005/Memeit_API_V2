# Memeit_API_V2

JSON API for a random meme scraped from reddit.
https://memeit-api-v2.herokuapp.com/{subreddit_name}

API Link : [https://memeit-api-v2.herokuapp.com/dankmemes](https://memeit-api-v2.herokuapp.com/dankmemes)

**Example Response:**

```jsonc
{
  "subreddit": "dankmemes",
  "title": "get tf outa here",
  "url": "https://i.redd.it/8u0jcr9ovzs71.jpg"
}
```

## Custom Endpoints

### Specify count (MAX 50)

This is the sample search for shot videos/video memes

Endpoint: [/{subreddit_name}/{count}](https://memeit-api-v2.herokuapp.com/me_irl/20)

Example: [https://memeit-api-v2.herokuapp.com/me_irl/20](https://memeit-api-v2.herokuapp.com/me_irl/20)

Response:

```jsonc
{

    "code": 200,
    "count": 20,
    "memes": [
        {
            "audio_url": "https://v.redd.it/p9utrjtnavs71/DASH_audio.mp4",
            "subreddit": "me_irl",
            "title": "me🐵irl",
            "url": "https://v.redd.it/p9utrjtnavs71/DASH_360.mp4"
        },
        {
            "audio_url": "https://v.redd.it/i1hgx853pts71/DASH_audio.mp4",
            "subreddit": "me_irl",
            "title": "me_irl",
            "url": "https://v.redd.it/i1hgx853pts71/DASH_360.mp4"
        }
    ]

}
```
