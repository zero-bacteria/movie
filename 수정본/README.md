[toc]



# PJT 09



## 어려웠던점

```js
.catch((error) => {
        if (error.response.status === 401) {
          window.location.href = '/accounts/login/'
```

preventDefault()로 인해서 로그인 안한 사용자의 경우에도 좋아요가 눌러지고 undefind로 나오는 상황이 벌어졌다. 이를 해결하기 위해 axios 에서 실패했을때 catch를 사용하는것을 이용하여 해결하였다.







## 코드



### community/index.html

``` django
{% extends 'base.html' %}

{% block content %}
  <h1>Community</h1>
  {% if user.is_authenticated %}
    <a href="{% url 'community:create' %}">NEW</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요]</a>
  {% endif %}
  <hr>
  {% for review in articles %}
    <p><b>작성자 : <a href="{% url 'accounts:profile' review.user.username %}">{{ review.user }}</a></b></p>
    <p>글 번호: {{ review.pk }}</p>
    <p>글 제목: {{ review.title }}</p>
    <p>글 내용: {{ review.content }}</p>
    <form class="like-form d-inline" data-id="{{ review.pk }}">
      {% csrf_token %}

      {% if user in review.like_users.all %}
        <button class="btn btn-link">
          <i id="like-{{ review.pk }}" class="fas fa-heart fa-lg" style="color:crimson;"></i>
        </button>
      {% else %}
        <button class="btn btn-link">
          <i id="like-{{ review.pk }}" class="fas fa-heart fa-lg" style="color:black;"></i>
        </button>
      {% endif %}
    </form>
    <span id="count-{{ review.pk }}">{{ review.like_users.all|length }} </span>명이 이 글을 좋아합니다.<br>
    <a href="{% url 'community:detail' review.pk %}">[detail]</a>
    <hr>
  {% endfor %}
  
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
  const forms = document.querySelectorAll('.like-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  forms.forEach(function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault()
      const reviewId = event.target.dataset.id
 axios.post(`http://127.0.0.1:8000/community/${reviewId}/like/`, {}, {headers: {'X-CSRFToken' : csrftoken}})
      .then(function (response) {
        const liked = response.data.liked
        const count = response.data.count

        /* const require_login = response.request.responseURL.includes('login') ? response.request.responseURL : false
        if ( require_login ) {
      window.location.href = require_login
        } */

        const likeButton = document.querySelector(`#like-${reviewId}`)
        likeButton.style.color = liked ? 'crimson' : 'black'
        const likeCount = document.querySelector(`#count-${reviewId}`)
        likeCount.innerText = count
      })
      .catch((error) => {
        if (error.response.status === 401) {
          window.location.href = '/accounts/login/'
        }
      })
    })
  })

  </script>
{% endblock %}

```



### community.views

```python
@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True
        like_status = {
            'liked' : liked,
            'count' : review.like_users.count(),
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)
```





### accounts/_follow.html

```django
<div class="jumbotron text-center text-white bg-dark">
  <p class="lead mb-1">작성자 정보</p>
  <h1 class="display-4">{{ person.username }}</h1>
  <hr>
  {% with followings=person.followings.all followers=person.followers.all %}
    <p class="lead" >
      <span id="follow-count-{{ person.pk }}">
        팔로잉 : {{ followings|length }} / 팔로워 : {{ followers|length }}
      </span>
    </p>
    <!-- 팔로우 버튼 -->
    {% if request.user != person %}
      <form class="follow-form" data-user-id="{{ person.pk }}">
        {% csrf_token %}
        {% if request.user in followers %}
          <button class="btn-secondary btn-lg" role="button">Unfollow</button>
        {% else %}
          <button class="btn-primary btn-lg" role="button">Follow</button>
        {% endif %}
      </form>
    {% endif %}
  {% endwith %}
</div>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const forms = document.querySelectorAll('.follow-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  forms.forEach(function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault()

      const userId = event.target.dataset.userId
      
      console.log(userId)
      axios.post(`http://127.0.0.1:8000/accounts/follow/${userId}/`, {}, {headers: {'X-CSRFToken': csrftoken}
      }).then(function (response) {
        const followed = response.data.followed
        const followings = response.data.followings
        const followers = response.data.followers
        
        const followButton = document.querySelector(".follow-form > button")
        if (followed) {
          followButton.innerText = 'Unfollow'
        } else {  
          followButton.innerText = 'Follow'
        }

        const followCount = document.querySelector(`#follow-count-${ userId}`)
        followCount.innerText = `팔로잉: ${followings} / 팔로워: ${followers}`
        console.log(followers)
        console.log(followings)
      })

    })
  })
</script>
```



### accounts/views

```python
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                followed = False
            else:
                person.followers.add(user)
                followed =True
        follow_status = {
            'followed': followed,
            'followings': person.followings.count(),
            'followers': person.followers.count(),
        }
        return JsonResponse(follow_status)
    return redirect('accounts:profile', person.username)
```

