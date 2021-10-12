# Memeit_API_V2
This is main url
https://memeit-api-v2.herokuapp.com/

For regular memes (in .png, .gif, .jpg format)

https://memeit-api-v2.herokuapp.com/dankmemes

(note you can replace the subreddit you want after "/"; "dankmemes" used as an example)


sample output:


    
    "code": 200,
    "count": 50,
    "memes": [
        {
            "subreddit": "dankmemes",
            "title": "get tf outa here",
            "url": "https://i.redd.it/8u0jcr9ovzs71.jpg"
        },
        {
            "subreddit": "dankmemes",
            "title": "Proud of you PornHub",
            "url": "https://i.redd.it/a9f07ei0qzs71.gif"
        },
        {
            "subreddit": "dankmemes",
            "title": "Gib me yo moni",
            "url": "https://i.redd.it/kb8bw54k3ys71.gif"
        },//
        
   
        
for short video memes
https://memeit-api-v2.herokuapp.com/me_irl/20

(note you can replace the subreddit you want after "/"; "me_irl" used as an example. "20"  is used to specify the number of output 100 is the max.)


sample output: 




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


