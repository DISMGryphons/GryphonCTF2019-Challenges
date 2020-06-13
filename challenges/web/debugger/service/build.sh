docker build -t web-debugger .
docker run --restart always -d -p 12001:80 --name web-debugger web-debugger
docker start web-debugger