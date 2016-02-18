$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    }
  }
});

function get_post(id) {
  $.post({
    url: "/get-post/",
    data: {
      id
    },
    success: function(data) {
      $('#model-post-title').text(data.title)
      $('#model-post-text').text(data.text)
    },
    dataType: "json"
  }).fail(function() {
    alert("Debug: error")
  })
}

function send_post() {
  title = $('#post-title').val()
  text = $('#post-text').val()
  $.post({
    url: "/new-post/",
    data: {
      title,
      text
    },
    success: function(data) {
      alert("Debug: success")
    },
    dataType: "json"
  }).fail(function() {
    alert("Debug: error")
  })
}

function login() {
  username = $('#username').val()
  password = $('#password').val()
  $.post({
    url: "/login/",
    data: {
      username,
      password
    },
    success: function(data) {
      alert("Debug: success")
    },
    dataType: "json"
  }).fail(function() {
    alert("Debug: error")
  })
}

function logout() {
  $.post({
    url: "/logout/",
    data: {},
    success: function(data) {
      alert("Debug: success")
    },
    dataType: "json"
  }).fail(function() {
    alert("Debug: error")
  })
}

function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}