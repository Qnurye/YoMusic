
---

### 歌手相关MV


`https://music.163.com/weapi/artist/mvs`

POST :
```javascript
{
    artistId: query.id,
    limit: query.limit,
    offset: query.offset,
    total: true
  }
```

---

### 分类歌单


`https://music.163.com/weapi/playlist/list`

POST :
```javascript
{
    cat: query.cat || '全部', // 全部,华语,欧美,日语,韩语,粤语,小语种,流行,摇滚,民谣,电子,舞曲,说唱,轻音乐,爵士,乡村,R&B/Soul,古典,民族,英伦,金属,朋克,蓝调,雷鬼,世界音乐,拉丁,另类/独立,New Age,古风,后摇,Bossa Nova,清晨,夜晚,学习,工作,午休,下午茶,地铁,驾车,运动,旅行,散步,酒吧,怀旧,清新,浪漫,性感,伤感,治愈,放松,孤独,感动,兴奋,快乐,安静,思念,影视原声,ACG,儿童,校园,游戏,70后,80后,90后,网络歌曲,KTV,经典,翻唱,吉他,钢琴,器乐,榜单,00后
    order: query.order || 'hot', // hot,new
    limit: query.limit || 50,
    offset: query.offset || 0,
    total: true
  }
```

---

### 视频链接


`https://music.163.com/weapi/cloudvideo/playurl`

POST :
```javascript
{
    ids: '["' + query.id + '"]',
    resolution: query.res || 1080
  }
```

---

### 电台推荐类型


`http://music.163.com/weapi/djradio/home/category/recommend`

POST :
```javascript
{}
```

---

### 热门搜索


`https://music.163.com/weapi/search/hot`

POST :
```javascript
{
    type: 1111
  }
```

---

### 歌曲链接


`https://music.163.com/api/song/enhance/player/url`

POST :
```javascript
{
    ids: '[' + query.id + ']',
    br: parseInt(query.br || 999000)
  }
```

---

### 编辑歌单


`https://music.163.com/weapi/batch`

POST :
```javascript
{
    '/api/playlist/desc/update': `{"id":${query.id},"desc":"${query.desc}"}`,
    '/api/playlist/tags/update': `{"id":${query.id},"tags":"${query.tags}"}`,
    '/api/playlist/update/name': `{"id":${query.id},"name":"${query.name}"}`
  }
```

---

### 点赞与取消点赞评论


`https://music.163.com/weapi/v1/comment/${query.t}`

POST :
```javascript
{
    threadId: query.type + query.id,
    commentId: query.cid
  }
  if(query.type == 'A_EV_2_'){
    data.threadId = query.threadId
  }
```

---

### 点赞与取消点赞资源


`https://music.163.com/weapi/resource/${query.t}`

POST :
```javascript
{
    threadId: query.type + query.id
  }
  if(query.type=='A_EV_2_'){
    data.threadId=query.threadId
  }
```

---

### 精选电台


`https://music.163.com/weapi/djradio/recommend/v1`

POST :
```javascript
{}
```

---

### 首页-发现 block page


`https://music.163.com/api/homepage/block/page`

POST :
```javascript
{ 'refresh': query.refresh || true }
```

---

### 推荐电台


`https://music.163.com/weapi/personalized/djprogram`

POST :
```javascript
{}
```

---

### 全部MV


`https://interface.music.163.com/api/mv/all`

POST :
```javascript
{
    tags: JSON.stringify({
      地区: query.area || '全部',
      类型: query.type || '全部',
      排序: query.order || '上升最快'
    }),
    offset: query.offset || 0,
    total: 'true',
    limit: query.limit || 30
  };
```

---

### 收藏单曲到歌单 从歌单删除歌曲


`https://music.163.com/weapi/playlist/manipulate/tracks`

POST :
```javascript
{
    op: query.op, // del,add
    pid: query.pid, // 歌单id
    trackIds: '[' + query.tracks + ']' // 歌曲id
  }
```

---

### 设置


`https://music.163.com/api/user/setting`

POST :
```javascript
{
       
  }
```

---

### 热门歌单分类


`https://music.163.com/weapi/playlist/hottags`

POST :
```javascript
{}
```

---

### 动态


`https://music.163.com/weapi/v1/event/get`

POST :
```javascript
{
    'pagesize': query.pagesize || 20,
    'lasttime': query.lasttime || -1
  }
```

---

### 用户动态


`https://music.163.com/weapi/event/get/${query.uid}`

POST :
```javascript
{
    getcounts: true,
    time: query.lasttime || -1,
    limit: query.limit || 30,
    total: false
  };
```

---

### 编辑歌单顺序


`https://music.163.com/api/playlist/order/update`

POST :
```javascript
{
    ids: query.ids
  }
```

---

### 收藏/取消收藏专辑


`https://music.163.com/api/album/${query.t}`

POST :
```javascript
{
    id: query.id
  };
```

---

### 全部视频列表


`https://music.163.com/api/videotimeline/otherclient/get`

POST :
```javascript
{
    groupId: 0,
    offset: query.offset || 0,
    need_preview_url: 'true',
    total: true
  }
  console.log({data})
  //   /api/videotimeline/otherclient/get
```

---

### 收藏与取消收藏歌单


`https://music.163.com/weapi/playlist/${query.t}`

POST :
```javascript
{
    id: query.id
  }
```

---

### 删除歌单


`https://music.163.com/weapi/playlist/remove`

POST :
```javascript
{
    ids: '[' + query.id + ']' 
  };
```

---

### 更新歌单描述


`http://interface3.music.163.com/eapi/playlist/desc/update`

POST :
```javascript
{
    id: query.id,
    desc: query.desc
  }
```

---

### MV详情


`https://music.163.com/api/v1/mv/detail`

POST :
```javascript
{
    id: query.mvid
  }
```

---

### 视频点赞转发评论数数据


`https://music.163.com/api/comment/commentthread/info`

POST :
```javascript
{
    'threadid': `R_VI_62_${query.vid}`,
    'composeliked': true
  }
```

---

### 私信内容


`https://music.163.com/api/msg/private/history`

POST :
```javascript
{
    userId: query.uid,
    limit: query.limit || 30,
    time: query.before || 0,
    total: 'true'
  };
```

---

### 获取动态评论


`https://music.163.com/weapi/v1/resource/comments/${query.threadId}`

POST :
```javascript
{
    limit: query.limit || 20,
    offset: query.offset || 0,
    beforeTime: query.before || 0
  };
```

---

### 首页-发现 dragon ball


`https://music.163.com/eapi/homepage/dragon/ball/static`

POST :
```javascript
{}
```

---

### 更新歌单名


`http://interface3.music.163.com/eapi/playlist/update/name`

POST :
```javascript
{
    id: query.id,
    name: query.name
  }
```

---

### 用户歌单


`https://music.163.com/weapi/user/playlist`

POST :
```javascript
{
    uid: query.uid,
    limit: query.limit || 30,
    offset: query.offset || 0
  }
```

---

### 购买数字专辑


`https://music.163.com/api/ordering/web/digital`

POST :
```javascript
{
    business: 'Album',
    paymentMethod: query.payment,
    digitalResources: JSON.stringify([{
      business: 'Album',
      resourceID: query.id,
      quantity: query.quantity,
    }]),
    from: 'web'
  }
```

---

### 关注与取消关注用户


`https://music.163.com/weapi/user/${query.t}/${query.id}`

POST :
```javascript
{}
```

---

### 电台节目详情


`https://music.163.com/weapi/dj/program/detail`

POST :
```javascript
{
    id: query.id
  }
```

---

### 通知


`https://music.163.com/api/msg/notices`

POST :
```javascript
{
    limit: query.limit || 30,
    time: query.lasttime || -1
  };
```

---

### 分享歌曲到动态


`http://music.163.com/weapi/share/friends/resource`

POST :
```javascript
{
    type: query.type || 'song', // song,playlist,mv,djprogram，djradio
    msg: query.msg || '',
    id: query.id || ''
  };
```

---

### 歌手单曲


`https://music.163.com/weapi/v1/artist/${query.id}`

POST :
```javascript
{}
```

---

### 相似用户


`https://music.163.com/weapi/discovery/simiUser`

POST :
```javascript
{
    songid: query.id,
    limit: query.limit || 50,
    offset: query.offset || 0
  }
```

---

### 电台节目榜


`https://music.163.com/api/program/toplist/v1`

POST :
```javascript
{
    limit: query.limit || 100,
    offset: query.offset || 0
  }
```

---

### 评论


`https://music.163.com/api/v1/user/comments/${query.uid}`

POST :
```javascript
{
    beforeTime: query.before || '-1',
    limit: query.limit || 30,
    total: 'true',
    uid: query.uid
  };
  
```

---

### 订阅电台列表


`https://music.163.com/weapi/djradio/get/subed`

POST :
```javascript
{
    limit: query.limit || 30,
    offset: query.offset || 0,
    total: true
  }
```

---

### 首页轮播图


`https://music.163.com/api/v2/banner/get`

POST :
```javascript
{}
```

---

### 云盘数据详情


`https://music.163.com/weapi/v1/cloud/get/byids`

POST :
```javascript
{
    songIds: id
  };
```

---

### 搜索


`https://music.163.com/weapi/search/get`

POST :
```javascript
{
    s: query.keywords,
    type: query.type || 1, // 1: 单曲, 10: 专辑, 100: 歌手, 1000: 歌单, 1002: 用户, 1004: MV, 1006: 歌词, 1009: 电台, 1014: 视频
    limit: query.limit || 30,
    offset: query.offset || 0
  }
```

---

### 删除动态


`https://music.163.com/eapi/event/delete`

POST :
```javascript
{
    id: query.evId,
  }
```

---

### 歌手介绍


`https://music.163.com/weapi/artist/introduction`

POST :
```javascript
{
    id: query.id
  }
```

---

### 云盘数据


`https://music.163.com/weapi/v1/cloud/get`

POST :
```javascript
{
    limit: query.limit || 30,
    offset: query.offset || 0
  }
```

---

### 校验验证码


`https://music.163.com/weapi/sms/captcha/verify`

POST :
```javascript
{
    ctcode: query.ctcode || '86',
    cellphone: query.phone,
    captcha: query.captcha
  }
```

---

### 新晋电台榜/热门电台榜


`https://music.163.com/api/djradio/toplist`

POST :
```javascript
{
    limit: query.limit || 100,
    offset: query.offset || 0,
    type: typeMap[query.type || 'new'] || '0'  //0为新晋,1为热门
  }
```

---

### 退出登录


`https://music.163.com/weapi/logout`

POST :
```javascript
{}
```

---

### 热搜列表


`https://music.163.com/weapi/hotsearchlist/get`

POST :
```javascript
{
  };
```

---

### 电台最热主播榜


`https://music.163.com/api/dj/toplist/popular`

POST :
```javascript
{
    limit: query.limit || 100
    // 不支持 offset
  }
```

---

### 收藏与取消收藏视频


`https://music.163.com/weapi/cloudvideo/video/${query.t}`

POST :
```javascript
{
    id: query.id
  }
```

---

### 相似MV


`https://music.163.com/weapi/discovery/simiMV`

POST :
```javascript
{
    mvid: query.mvid
  }
```

---

### 推荐视频


`https://music.163.com/api/videotimeline/get`

POST :
```javascript
{
    offset: query.offset || 0,
    filterLives: '[]',
    withProgramInfo: 'true',
    needUrl: '1',
    resolution: '480'
  };
```

---

### 视频评论


`https://music.163.com/weapi/v1/resource/comments/R_VI_62_${query.id}`

POST :
```javascript
{
    rid: query.id,
    limit: query.limit || 20,
    offset: query.offset || 0,
    beforeTime: query.before || 0
  }
```

---

### 热门电台


`https://music.163.com/weapi/djradio/hot/v1`

POST :
```javascript
{
    limit: query.limit || 30,
    offset: query.offset || 0
  }
```

---

### 电台新人榜


`https://music.163.com/api/dj/toplist/newcomer`

POST :
```javascript
{
    limit: query.limit || 100,
    offset: query.offset || 0
  }
```

---

### 新碟上架


`https://music.163.com/weapi/album/new`

POST :
```javascript
{
    area: query.type || 'ALL', // ALL,ZH,EA,KR,JP
    limit: query.limit || 50,
    offset: query.offset || 0,
    total: true
  }
```

---

### 歌单评论


`https://music.163.com/weapi/v1/resource/comments/A_PL_0_${query.id}`

POST :
```javascript
{
    rid: query.id,
    limit: query.limit || 20,
    offset: query.offset || 0,
    beforeTime: query.before || 0
  }
```

---

### 垃圾桶


`https://music.163.com/weapi/radio/trash/add?alg=RT&songId=${query.id}&time=${query.time || 25}`

POST :
```javascript
{
    songId: query.id
  }
```

---

### 精品歌单


`https://music.163.com/weapi/playlist/highquality/list`

POST :
```javascript
{
    cat: query.cat || '全部', // 全部,华语,欧美,韩语,日语,粤语,小语种,运动,ACG,影视原声,流行,摇滚,后摇,古风,民谣,轻音乐,电子,器乐,说唱,古典,爵士
    limit: query.limit || 50,
    lasttime: query.before || 0, // 歌单updateTime
    total: true
  }
```

---

### 独家放送


`https://music.163.com/weapi/personalized/privatecontent`

POST :
```javascript
{}
```

---

### 国家编码列表


`http://interface3.music.163.com/eapi/lbs/countries/v1`

POST :
```javascript
{}
```

---

### 歌单详情


`https://music.163.com/weapi/v3/playlist/detail`

POST :
```javascript
{
    id: query.id,
    n: 100000,
    s: query.s || 8
  }
```

---

### 付费精品


`https://music.163.com/api/djradio/toplist/pay`

POST :
```javascript
{
    limit: query.limit || 100
    // 不支持 offset
  }
```

---

### 发送验证码


`https://music.163.com/weapi/sms/captcha/sent`

POST :
```javascript
{
    ctcode: query.ctcode || '86',
    cellphone: query.phone,
  }
```

---

### 登录状态


`https://music.163.com`, {},
    {cookie: query.cookie, proxy: query.proxy}
  )
    .then(response => {
      try{
        let profile = eval(`(${/GUser\s*=\s*([^;]+);/.exec(response.body)[1]})`)
        let bindings = eval(`(${/GBinds\s*=\s*([^;]+);/.exec(response.body)[1]})`

POST :
```javascript
{}
```

---

### 相似歌手


`https://music.163.com/weapi/discovery/simiArtist`

POST :
```javascript
{
    artistid: query.id
  }
```

---

### 全部歌单分类


`https://music.163.com/weapi/playlist/catalogue`

POST :
```javascript
{}
```

---

### 歌词


`https://music.163.com/api/song/lyric`

POST :
```javascript
{
    id: query.id,
    lv: -1,
    kv: -1,
    tv: -1
  }
```

---

### 登录刷新


`https://music.163.com/weapi/login/token/refresh`

POST :
```javascript
{}
```

---

### 推荐新歌


`https://music.163.com/weapi/personalized/newsong`

POST :
```javascript
{
    type: 'recommend'
  }
```

---

### 歌手分类


`https://music.163.com/api/v1/artist/list`

POST :
```javascript
{
    initial: isNaN(query.initial) ? (query.initial || '').toUpperCase().charCodeAt() || undefined : query.initial,
    offset: query.offset || 0,
    limit: query.limit || 30,
    total: true,
    type: query.type || '1',
    area: query.area
  }
```

---

### 收藏计数


`https://music.163.com/weapi/subcount`

POST :
```javascript
{}
```

---

### @我


`https://music.163.com/api/forwards/get`

POST :
```javascript
{
    offset: query.offset || 0,
    limit: query.limit || 30,
    total: 'true'
  };
```

---

### 私信歌单


`https://music.163.com/weapi/msg/private/send`

POST :
```javascript
{
    id: query.playlist,
    type: 'playlist',
    msg: query.msg,
    userIds: '[' + query.user_ids + ']'
  }
```

---

### 更换手机


`https://music.163.com/api/user/replaceCellphone`

POST :
```javascript
{
    captcha: query.captcha,
    phone: query.phone,
    oldcaptcha: query.oldcaptcha,
    ctcode: query.ctcode || '86'
  };
```

---

### 编辑用户信息


`https://music.163.com/weapi/user/profile/update`

POST :
```javascript
{
    avatarImgId: '0',
    birthday: query.birthday,
    city: query.city,
    gender: query.gender,
    nickname: query.nickname,
    province: query.province,
    signature: query.signature
  }
```

---

### 视频标签/分类下的视频


`https://music.163.com/api/videotimeline/videogroup/otherclient/get`

POST :
```javascript
{
    groupId: query.id,
    offset: query.offset || 0,
    need_preview_url: 'true',
    total: true
  }
```

---

### 每日推荐歌单


`https://music.163.com/weapi/v1/discovery/recommend/resource`

POST :
```javascript
{}
```

---

### 听歌排行


`https://music.163.com/weapi/v1/play/record`

POST :
```javascript
{
    uid: query.uid,
    type: query.type || 0 // 1: 最近一周, 0: 所有时间
  }
```

---

### 喜欢的歌曲(无序)


`https://music.163.com/weapi/song/like/get`

POST :
```javascript
{
    uid: query.uid
  }
```

---

### 最新专辑


`https://music.163.com/api/discovery/newAlbum`

POST :
```javascript
{}
```

---

###热门话题


`http://music.163.com/weapi/act/hot`

POST :
```javascript
{
    limit: query.limit || 20,
    offset: query.offset || 0
  }
```

---

### 歌曲详情


`https://music.163.com/weapi/v3/song/detail`

POST :
```javascript
{
    c: '[' + query.ids.map(id => ('{"id":' + id + '}')).join(',') + ']',
    ids: '[' + query.ids.join(',') + ']'
  }
```

---

### 网易出品


`https://interface.music.163.com/api/mv/exclusive/rcmd`

POST :
```javascript
{
    offset: query.offset || 0,
    limit: query.limit || 30
  };
```

---

### 搜索建议


`https://music.163.com/weapi/search/suggest/`

POST :
```javascript
{
    s: query.keywords || ''
  }
  let type = query.type == 'mobile' ? 'keyword' : 'web'
```

---

### 默认搜索关键词


`http://interface3.music.163.com/eapi/search/defaultkeyword/get`

POST :
```javascript
{}
```

---

### 热门评论


`https://music.163.com/weapi/v1/resource/hotcomments/${query.type}${query.id}`

POST :
```javascript
{
    rid: query.id,
    limit: query.limit || 20,
    offset: query.offset || 0,
    beforeTime: query.before || 0
  }
```

---

### 发送与删除评论


`https://music.163.com/weapi/resource/comments/${query.t}`

POST :
```javascript
{
    threadId: query.type + query.id
  }
    
  if(query.type == 'A_EV_2_'){
    data.threadId = query.threadId
  }
  if(query.t == 'add')
    data.content = query.content
  else if(query.t == 'delete')
    data.commentId = query.commentId
  else if (query.t == 'reply') {
    data.commentId = query.commentId
    data.content = query.content
  }
```

---

### 收藏与取消收藏MV


`https://music.163.com/weapi/mv/${query.t}`

POST :
```javascript
{
    mvId: query.mvid,
    mvIds: '["' + query.mvid + '"]'
  } 
```

---

### 关注TA的人(粉丝)


`https://music.163.com/eapi/user/getfolloweds/${query.uid}`

POST :
```javascript
{
    userId: query.uid,
    time: query.lasttime || -1,
    limit: query.limit || 30
  };
```

---

### 电台评论


`https://music.163.com/weapi/v1/resource/comments/A_DJ_1_${query.id}`

POST :
```javascript
{
    rid: query.id,
    limit: query.limit || 20,
    offset: query.offset || 0,
    beforeTime: query.before || 0
  }
```

---

### 专辑动态信息


`https://music.163.com/api/album/detail/dynamic`

POST :
```javascript
{
    id: query.id
  }
```

---

### 电台分类列表


`https://music.163.com/weapi/djradio/category/get`

POST :
```javascript
{}
```

---

### MV 点赞转发评论数数据


`https://music.163.com/api/comment/commentthread/info`

POST :
```javascript
{
    'threadid': `R_MV_5_${query.mvid}`,
    'composeliked': true
  }
```

---

### 关注歌手列表


`https://music.163.com/weapi/artist/sublist`

POST :
```javascript
{
    limit: query.limit || 25,
    offset: query.offset || 0,
    total: true
  }
```

---

### 电台节目列表


`https://music.163.com/weapi/dj/program/byradio`

POST :
```javascript
{
    radioId: query.rid,
    limit: query.limit || 30,
    offset: query.offset || 0,
    asc: toBoolean(query.asc)
  }
```

---

### 签到


`https://music.163.com/weapi/point/dailyTask`

POST :
```javascript
{
    type: query.type || 0
  }
```

---

### 电台今日优选


`http://music.163.com/weapi/djradio/home/today/perfered`

POST :
```javascript
{
    page: query.page || 0
  };
```

---

### MV链接


`https://music.163.com/weapi/song/enhance/play/mv/url`

POST :
```javascript
{
    id: query.id,
    r: query.res || 1080
  }
```

---

### 邮箱登录


`https://music.163.com/weapi/login`

POST :
```javascript
{
    username: query.email,
    password: query.md5_password || crypto.createHash('md5').update(query.password).digest('hex'),
    rememberLogin: 'true'
  }
  let result = await request(
    'POST', `https://music.163.com/weapi/login`, data,
    { crypto: 'weapi', ua: 'pc', cookie: query.cookie, proxy: query.proxy }
  )
  if (result.body.code === 502) { {
      status: 200,
      body: {
        'msg': '账号或密码错误',
        'code': 502,
        'message': '账号或密码错误'
      }
    }
  }
  if (result.body.code === 200) {
    result = {
      status: 200,
      body: {
        ...result.body,
        cookie: result.cookie.join(';')
      },
      cookie: result.cookie
    }
  }
```

---

### 已收藏MV列表


`https://music.163.com/weapi/cloudvideo/allvideo/sublist`

POST :
```javascript
{
    limit: query.limit || 25,
    offset: query.offset || 0,
    total: true
  }
```

---

### 用户详情


`https://music.163.com/weapi/v1/user/detail/${query.uid}`

POST :
```javascript
{}
```

---

### 历史每日推荐歌曲


`https://music.163.com/api/discovery/recommend/songs/history/recent`

POST :
```javascript
{
  }
```

---

### 专辑内容


`https://music.163.com/weapi/v1/album/${query.id}`

POST :
```javascript
{}
```

---

### 已收藏专辑列表


`https://music.163.com/weapi/album/sublist`

POST :
```javascript
{
    limit: query.limit || 25,
    offset: query.offset || 0,
    total: true
  }
```

---

### 所有榜单介绍


`https://music.163.com/api/toplist`

POST :
```javascript
{}
```

---

### 手机登录


`https://music.163.com/weapi/login/cellphone`

POST :
```javascript
{
    phone: query.phone,
    countrycode: query.countrycode,
    password: query.md5_password || crypto.createHash('md5').update(query.password).digest('hex'),
    rememberLogin: 'true'
  }
  let result = await request(
    'POST', `https://music.163.com/weapi/login/cellphone`, data,
    {crypto: 'weapi', ua: 'pc', cookie: query.cookie, proxy: query.proxy}
  )
 
  if (result.body.code === 200) {
    result = {
      status: 200,
      body: {
        ...result.body,
        cookie: result.cookie.join(';')
      },
      cookie: result.cookie
    }
  }
```

---

### 听歌打卡


`https://music.163.com/weapi/feedback/weblog`

POST :
```javascript
{
    logs: JSON.stringify([{
      action: 'play',
      json: {
        download: 0,
        end: 'playend',
        id: query.id,
        sourceId: query.sourceid,
        time: query.time,
        type: 'song',
        wifi: 0,
      }
    }])
  }
    
```

---

### 多类型搜索


`https://music.163.com/weapi/search/suggest/multimatch`

POST :
```javascript
{
    type: query.type || 1,
    s: query.keywords || ''
  }
```

---

### 歌曲可用性


`https://music.163.com/weapi/song/enhance/player/url`

POST :
```javascript
{
    ids: '[' + parseInt(query.id) + ']',
    br: parseInt(query.br || 999000)
  } request(
    'POST', `https://music.163.com/weapi/song/enhance/player/url`, data,
    {crypto: 'weapi', cookie: query.cookie, proxy: query.proxy}
  )
    .then(response => {
      let playable = false
      if(response.body.code == 200){
        if(response.body.data[0].code == 200){
          playable = true
        }
      }
      if(playable){
        response.body = {success: true, message: 'ok'} response
      }
      else{
        response.status = 404
        response.body = {success: false, message: '亲爱的,暂无版权'}
```

---

### 精选电台分类


`https://music.163.com/weapi/djradio/recommend`

POST :
```javascript
{
    cateId: query.type
  }
```

---

### 操作记录


`https://music.163.com/weapi/feedback/weblog`

POST :
```javascript
{}
```

---

### 电台24小时主播榜


`https://music.163.com/api/dj/toplist/hours`

POST :
```javascript
{
    limit: query.limit || 100
    // 不支持 offset
  }
```

---

### 云村热评


`https://music.163.com/api/comment/hotwall/list/get`

POST :
```javascript
{}
```

---

### 红心与取消红心歌曲


`https://music.163.com/weapi/radio/like?alg=${query.alg ||
      'itembased'}&trackId=${query.id}&time=${query.time ||
      25}`

POST :
```javascript
{
    trackId: query.id,
    like: query.like
  }
```

---

### 视频分类列表


`https://music.163.com/api/cloudvideo/category/list`

POST :
```javascript
{
    offset: query.offset || 0,
    total: 'true',
    limit: query.limit || 99,
  };
```

---

### 歌曲评论


`https://music.163.com/api/v1/resource/comments/R_SO_4_${query.id}`

POST :
```javascript
{
    rid: query.id,
    limit: query.limit || 20,
    offset: query.offset || 0,
    beforeTime: query.before || 0
  };
```

---

### 初始化名字


`http://music.163.com/eapi/activate/initProfile`

POST :
```javascript
{
    nickname: query.nickname
  };
```

---

### 电台非热门类型


`http://music.163.com/weapi/djradio/category/excludehot`

POST :
```javascript
{}
```

---

### 推荐歌单


`https://music.163.com/weapi/personalized/playlist`

POST :
```javascript
{
    limit: query.limit || 30,
    // offset: query.offset || 0,
    total: true,
    n: 1000
  }
```

---

### 视频详情


`https://music.163.com/weapi/cloudvideo/v1/video/detail`

POST :
```javascript
{
    id: query.id
  }
```

---

### 歌手专辑列表


`https://music.163.com/weapi/artist/albums/${query.id}`

POST :
```javascript
{
    limit: query.limit || 30,
    offset: query.offset || 0,
    total: true
  }
```

---

### 付费电台


`https://music.163.com/weapi/djradio/home/paygift/list?_nmclfl=1`

POST :
```javascript
{
    limit: query.limit || 30,
    offset: query.offset || 0
  }
```

---

### 热门歌手


`https://music.163.com/weapi/artist/top`

POST :
```javascript
{
    limit: query.limit || 50,
    offset: query.offset || 0,
    total: true
  }
```

---

### 独家放送列表


`https://music.163.com/api/v2/privatecontent/list`

POST :
```javascript
{
    offset: query.offset || 0,
    total: 'true',
    limit: query.limit || 60,
  }
```

---

### 电台banner


`http://music.163.com/weapi/djradio/banner/get`

POST :
```javascript
{};
  query.cookie.os = 'pc';
```

---

### 相似歌单


`https://music.163.com/weapi/discovery/simiPlaylist`

POST :
```javascript
{
    songid: query.id,
    limit: query.limit || 50,
    offset: query.offset || 0
  }
```

---

### 推荐MV


`https://music.163.com/weapi/personalized/mv`

POST :
```javascript
{}
```

---

### 我的数字专辑


`https://music.163.com/api/digitalAlbum/purchased`

POST :
```javascript
{
    limit: query.limit || 30,
    offset: query.offset || 0,
    total: true
  }
```

---

### 更新歌曲顺序


`http://interface.music.163.com/api/playlist/manipulate/tracks`

POST :
```javascript
{
    pid: query.pid,
    trackIds: query.ids,
    op: 'update',
  }

```

---

﻿### 转发动态


`https://music.163.com/weapi/event/forward`

POST :
```javascript
{
    forwards: query.forwards,
    id: query.evId,
    eventUserId: query.uid
  };
```

---

### 订阅与取消电台


`https://music.163.com/weapi/djradio/${query.t}`

POST :
```javascript
{
    id: query.rid
  }
```

---

### 收藏与取消收藏歌手


`https://music.163.com/weapi/artist/${query.t}`

POST :
```javascript
{
    artistId: query.id,
    artistIds: '[' + query.id + ']'
  }
```

---

### 创建歌单


`https://music.163.com/weapi/playlist/create`

POST :
```javascript
{
    name: query.name,
    privacy: query.privacy    //0 为普通歌单，10 为隐私歌单
  };
```

---

### 私人FM


`https://music.163.com/weapi/v1/radio/get`

POST :
```javascript
{}
```

---

### 歌手热门 50 首歌曲


`https://music.163.com/api/artist/top/song`

POST :
```javascript
{
    id: query.id
  }
```

---

### 歌单收藏者


`https://music.163.com/weapi/playlist/subscribers`

POST :
```javascript
{
    id: query.id,
    limit: query.limit || 20,
    offset: query.offset || 0
  };
```

---

### 类别热门电台


`https://music.163.com/api/djradio/hot`

POST :
```javascript
{
    cateId: query.cateId,
    limit: query.limit || 30,
    offset: query.offset || 0
  }
```

---

### 新歌速递


`https://music.163.com/weapi/v1/discovery/new/songs`

POST :
```javascript
{
    areaId: query.type || 0, // 全部:0 华语:7 欧美:96 日本:8 韩国:16
    // limit: query.limit || 100,
    // offset: query.offset || 0,
    total: true
  }
```

---

### 批量请求接口


`http://music.163.com/eapi/batch`

POST :
```javascript
{
    'e_r': true
  };
  Object.keys(query).forEach(i => {
    if (/^\/api\//.test(i)) {
      data[i] = query[i]
    }
  })
```

---

### 歌手榜


`https://music.163.com/weapi/toplist/artist`

POST :
```javascript
{
    type: query.type || 1,
    limit: 100,
    offset: 0,
    total: true
  }
```

---

### 云盘歌曲删除


`http://music.163.com/weapi/cloud/del`

POST :
```javascript
{
    songIds: [query.id]
  };
```

---

### MV评论


`https://music.163.com/weapi/v1/resource/comments/R_MV_5_${query.id}`

POST :
```javascript
{
    rid: query.id,
    limit: query.limit || 20,
    offset: query.offset || 0,
    beforeTime: query.before || 0
  }
```

---

### 注册账号


`https://music.163.com/weapi/register/cellphone`

POST :
```javascript
{
    captcha: query.captcha,
    phone: query.phone,
    password: crypto.createHash('md5').update(query.password).digest('hex'),
    nickname: query.nickname
  }
```

---

### 用户创建的电台


`https://music.163.com/weapi/djradio/get/byuser`

POST :
```javascript
{
    userId: query.uid
  }
```

---

### TA关注的人(关注)


`https://music.163.com/weapi/user/getfollows/${query.uid}`

POST :
```javascript
{
    offset: query.offset || 0,
    limit: query.limit || 30,
    order: true
  }
```

---

### 相似歌曲


`https://music.163.com/weapi/v1/discovery/simiSong`

POST :
```javascript
{
    songid: query.id,
    limit: query.limit || 50,
    offset: query.offset || 0
  }
```

---

### 历史每日推荐歌曲详情


`https://music.163.com/api/discovery/recommend/songs/history/detail`

POST :
```javascript
{
    date: query.date || '',
  }
```

---

### 排行榜


`https://interface3.music.163.com/api/playlist/v4/detail`

POST :
```javascript
{
    id: query.id,
    n: '500',
    s: '0',
  }
```

---

### 视频标签列表


`https://music.163.com/api/cloudvideo/group/list`

POST :
```javascript
{
  };
```

---

### 用户电台节目


`https://music.163.com/weapi/dj/program/${query.uid}`

POST :
```javascript
{
    limit: query.limit || 30,
    offset: query.offset || 0
  }
```

---

### 每日推荐歌曲


`https://music.163.com/api/v3/discovery/recommend/songs`

POST :
```javascript
{
  }
```

---

### 最新MV


`https://interface.music.163.com/weapi/mv/first`

POST :
```javascript
{
    // 'offset': query.offset || 0,
    area: query.area || '',
    limit: query.limit || 30,
    total: true
  };
```

---

### 推荐节目


`https://music.163.com/weapi/program/recommend/v1`

POST :
```javascript
{
    cateId: query.type,
    limit: query.limit || 10,
    offset: query.offset || 0
  }
```

---

### 智能播放


`http://music.163.com/weapi/playmode/intelligence/list`

POST :
```javascript
{
    songId: query.id,
    type: 'fromPlayOne',
    playlistId: query.pid,
    startMusicId: query.sid || query.id,
    count: query.count || 1
  };
```

---

### 私信


`https://music.163.com/weapi/msg/private/send`

POST :
```javascript
{
    id: query.playlist,
    type: 'text',
    msg: query.msg,
    userIds: '[' + query.user_ids + ']'
  }
```

---

### 相关歌单


`https://music.163.com/playlist?id=${query.id}`

POST :
```javascript
{}
```

---

### 所有榜单内容摘要


`https://music.163.com/weapi/toplist/detail`

POST :
```javascript
{}
```

---

### 私信


`https://music.163.com/api/msg/private/users`

POST :
```javascript
{
    offset: query.offset || 0,
    limit: query.limit || 30,
    total: 'true',
  };
```

---

### 电台详情


`https://music.163.com/weapi/djradio/get`

POST :
```javascript
{
    id: query.rid
  }
```

---

### 专辑评论


`https://music.163.com/weapi/v1/resource/comments/R_AL_3_${query.id}`

POST :
```javascript
{
    rid: query.id,
    limit: query.limit || 20,
    offset: query.offset || 0,
    beforeTime: query.before || 0
  }
```

---

### 检测手机号码是否已注册


`http://music.163.com/eapi/cellphone/existence/check`

POST :
```javascript
{
    cellphone: query.phone,
    countrycode: query.countrycode
  };
```

---

### 更新歌单标签


`http://interface3.music.163.com/eapi/playlist/tags/update`

POST :
```javascript
{
    id: query.id,
    tags: query.tags
  }
```

---

### 电台24小时节目榜


`https://music.163.com/api/djprogram/toplist/hours`

POST :
```javascript
{
    limit: query.limit || 100
    // 不支持 offset
  }
```

---

### MV排行榜


`https://music.163.com/weapi/mv/toplist`

POST :
```javascript
{
    area: query.area || '',
    limit: query.limit || 30,
    offset: query.offset || 0,
    total: true
  };
```

---

### 相关视频


`https://music.163.com/weapi/cloudvideo/v1/allvideo/rcmd`

POST :
```javascript
{
    id: query.id,
    type: (/^\d+$/.test(query.id)) ? 0 : 1
  }
```
