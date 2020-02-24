docker stop storage || true \
&& docker rm storage || true \
&& docker build -f Dockerfile -t storage_img . \
&& docker run --name storage -p 3306:3306  -v $(pwd)/db_zakupki:/var/lib/mysql -d storage_img
