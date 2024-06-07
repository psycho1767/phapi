from pornhub_api import *

# api = PornhubApi()









import random
api = PornhubApi()

tags = random.sample(api.video.tags("f").tags, 5)
category = random.choice(api.video.categories().categories)
result = api.search.search_videos(ordering="mostviewed", tags=tags, category=category)

print(result.size())
for vid in result:
    print(vid.title, vid.url)