require 1+ node

```
kubectl create namespace minio-dev-staging-ns
```
```
kubectl apply -n minio-dev-staging-ns -f distributed-headless-service.yaml
```
```
export MINIO_ACCESS_KEY=995Wpg....
export MINIO_SECRET_KEY=8YRMVj....
```
```
kubectl get -n minio-dev-staging-ns pvc
```

```
envsubst < deployment.yaml | kubectl apply -n minio-dev-staging-ns -f -
```