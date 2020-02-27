docker stop storage || true \
&& docker rm storage || true \
&& docker build -f Dockerfile -t storage_img . \
&& docker run --name storage -p 3306:3306  -v $(pwd)/db_storage:/var/lib/mysql -d storage_img
