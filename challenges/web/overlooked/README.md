# Overlooked

## Question Text

After the shenanigans with the debugger, it is now inaccessible. However, we made a login page that only works with our inhouse browser. Now u can't get the flag!

*Creator - @bitxer*

## Setup Guide
1. Enter `service` directory
2. `bash build.sh`

## Solution
1. Download `accounts.db` from the url
2. Reverse the md5 hash of the password for the user admin. You should get `permissions`
3. Login using a `POST` request, relevant `User-Agent` and login credentials
```
curl -X POST -A 'Mozilla/5.0 (SMART-TV; Ubuntu 12.04 LTS; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 TV Safari/538.1' -F 'user=admin' -F 'pass=permissions' http://13.67.65.32:12005/
```

### Flag
`GCTF{D0n7_Und3r3s71m4t3_7h3_p0w3r_0f_d1rec70r1e5}`
