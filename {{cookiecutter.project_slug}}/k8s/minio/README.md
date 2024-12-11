```
kubectl create namespace minio-dev-staging-ns
```
```
kubectl apply -n minio-dev-staging-ns -f pvc.yaml
```
```
export MINIO_ROOT_USER=995Wpg....
export MINIO_ROOT_PASSWORD=8YRMVj....
```
```
kubectl get -n minio-dev-staging-ns pvc
```

```
envsubst < deployment.yaml | kubectl apply -n minio-dev-staging-ns -f -
```
```
kubectl apply -n minio-dev-staging-ns -f service.yaml
```

Testing API
using macOS, use *mc* not *mcli*
```
brew install minio/stable/mc
```
using alpine linux
```
apk --update add minio-client
```
```
mcli alias set myminio http://<service-name>.<namespace>.svc.cluster.local:9000 <accessKey> <secretKey>
```
```
mcli admin info myminio
```
```
mcli ls myminio
```
```
mcli mb myminio/mybucket
```
```
mcli ls myminio
```