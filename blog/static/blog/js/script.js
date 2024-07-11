let switchMode = document.getElementById("switchMode");

switchMode.onclick = function () {
    let theme = document.getElementById("theme");

    if (theme.getAttribute("href") == "{% static 'blog/css/dark-mode.css' %}") {
        theme.href = "{% static 'blog/css/light-mode.css' %}";
    } else {
        theme.href = "{% static 'blog/css/dark-mode.css' %}";
    }

}

