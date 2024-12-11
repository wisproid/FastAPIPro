```
helm repo add bitnami https://charts.bitnami.com/bitnami
```
```
kubectl create namespace redis-dev-staging-ns
```
```
helm install -n redis-dev-staging-ns redis-staging bitnami/redis-cluster
```
```
NAME: redis-staging
LAST DEPLOYED: Sat Oct 19 08:33:14 2024
NAMESPACE: redis-dev-staging-ns
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: redis-cluster
CHART VERSION: 11.0.6
APP VERSION: 7.4.1** Please be patient while the chart is being deployed **


To get your password run:
    export REDIS_PASSWORD=$(kubectl get secret --namespace "redis-dev-staging-ns" redis-staging-redis-cluster -o jsonpath="{.data.redis-password}" | base64 -d)

You have deployed a Redis&reg; Cluster accessible only from within you Kubernetes Cluster.INFO: The Job to create the cluster will be created.To connect to your Redis&reg; cluster:

1. Run a Redis&reg; pod that you can use as a client:
kubectl run --namespace redis-dev-staging-ns redis-staging-redis-cluster-client --rm --tty -i --restart='Never' \
 --env REDIS_PASSWORD=$REDIS_PASSWORD \
--image docker.io/bitnami/redis-cluster:7.4.1-debian-12-r0 -- bash

2. Connect using the Redis&reg; CLI:

redis-cli -c -h redis-staging-redis-cluster -a $REDIS_PASSWORD



WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
  - redis.resources
  - updateJob.resources
+info https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
```

Customize values.yaml  
Make a local copy of values.yaml from https://github.com/bitnami/charts/blob/master/bitnami/redis-cluster/values.yaml. You can modify the content in values.yaml and apply the config changes to the Redis cluster by running:

```
export REDIS_PASSWORD=$(kubectl get secret --namespace "redis-dev-staging-ns" redis-staging-redis-cluster -o jsonpath="{.data.redis-password}" | base64 -d)
```

```
helm upgrade -n redis-dev-staging-ns redis-staging bitnami/redis-cluster --set 'password=<password>' -f values.yaml
```
```
Release "redis" has been upgraded. Happy Helming!
NAME: redis
LAST DEPLOYED: Sat Oct 19 06:55:32 2024
NAMESPACE: redis-dev-staging-ns
STATUS: deployed
REVISION: 2
TEST SUITE: None
NOTES:
CHART NAME: redis-cluster
CHART VERSION: 11.0.6
APP VERSION: 7.4.1** Please be patient while the chart is being deployed **


To get your password run:
    export REDIS_PASSWORD=$(kubectl get secret --namespace "redis-dev-staging-ns" redis-staging-redis-cluster -o jsonpath="{.data.redis-password}" | base64 -d)

You have deployed a Redis&reg; Cluster accessible only from within you Kubernetes Cluster.INFO: The Job to create the cluster will be created.To connect to your Redis&reg; cluster:

1. Run a Redis&reg; pod that you can use as a client:
kubectl run --namespace redis-dev-staging-ns redis-staging-redis-cluster --rm --tty -i --restart='Never' \
 --env REDIS_PASSWORD=$REDIS_PASSWORD \
--image docker.io/bitnami/redis-cluster:7.4.1-debian-12-r0 -- bash

2. Connect using the Redis&reg; CLI:

redis-cli -c -h redis-staging-redis-cluster -a $REDIS_PASSWORD



WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
  - redis.resources
  - updateJob.resources
+info https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
```

redis webui with redis insight   
```
kubectl apply -n redis-dev-staging-ns  -f redisinsight.yaml
```

example FQDN  
```
redis-staging-redis-cluster.redis-dev-staging-ns.svc.cluster.local
```