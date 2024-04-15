
# $1 - USERNAME
# $2 - HOST_IP

echo "create .env file"
set -e

> .env
echo "VERSION=$CI_PIPELINE_ID" >> .env
echo "CI_PROJECT_NAMESPACE=$CI_PROJECT_NAMESPACE" >> .env
echo "CI_PROJECT_NAME=$CI_PROJECT_NAME" >> .env
echo "CI_REGISTRY=$CI_REGISTRY" >> .env
echo "CORS_ALLOWED_ORIGINS=$PROD_CORS_ALLOWED_ORIGINS" >> .env
echo "CSRF_TRUSTED_ORIGINS=$PROD_CSRF_TRUSTED_ORIGINS" >> .env
echo "SECRET_KEY=$PROD_SECRET_KEY" >> .env
echo "POSTGRES_DB=$PROD_POSTGRES_DB" >> .env
echo "POSTGRES_USER=$PROD_POSTGRES_USER" >> .env
echo "POSTGRES_PASSWORD=$PROD_POSTGRES_PASSWORD" >> .env
echo "MAIL_USERNAME=$PROD_MAIL_USERNAME" >> .env
echo "MAIL_PASSWORD=$PROD_MAIL_PASSWORD" >> .env
echo "MAIL_FROM=$PROD_MAIL_FROM" >> .env
echo "MAIL_PORT=$PROD_MAIL_PORT" >> .env
echo "MAIL_SERVER=$PROD_MAIL_SERVER" >> .env
echo "MAIL_STARTTLS=$PROD_MAIL_STARTTLS" >> .env
echo "MAIL_SSL_TLS=$PROD_MAIL_SSL_TLS" >> .env
echo "MAIL_FROM_NAME=$PROD_MAIL_FROM_NAME" >> .env

echo "create project dir"
ssh $1@$2 mkdir -p /data/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME

echo "login docker registry"
ssh $1@$2 "docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY"

echo "copy docker-compose file"
scp $SSH_OPT ./docker-compose.stage.yml $1@$2:/data/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME/docker-compose.yml;

echo "copy .env file"
scp ./.env $1@$2:/data/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME/.env

echo "pull images"
ssh $1@$2 "cd /data/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME/ && docker compose pull"

echo "migrate..."
ssh $1@$2 "cd /data/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME/ && docker compose run --rm server bash -c "alembic upgrade head"

echo "start services"
ssh $1@$2 "cd /data/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME/ && docker compose up -d"

echo "remove none docker images"
ssh $1@$2 'docker image prune -a -f'
