Ref: https://cloudnative-pg.io/documentation

```
kubectl config get-contexts
```

```
kubectl config use-context <k8s-cluster-context-name>
```

```
kubectl config current-context
```

```
kubectl apply --server-side -f \
  https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/main/releases/cnpg-1.24.0.yaml
```

```
kubectl get deployment -n cnpg-system cnpg-controller-manager
```

```
kubectl create namespace postgresql-dev-staging-ns
```

```
kubectl apply -n postgresql-dev-staging-ns -f postgresql-cluster.yaml
```

```
kubectl get secrets -n postgresql-dev-staging-ns
```

```
kubectl get secret postgresql-cluster-app -n postgresql-dev-staging-ns -oyaml -o=jsonpath={.data.username}|base64 -d
kubectl get secret postgresql-cluster-app -n postgresql-dev-staging-ns -oyaml -o=jsonpath={.data.password}|base64 -d
```

```
kubectl exec -it postgresql-cluster-1 -n postgresql-dev-staging-ns -- psql -U postgres
```

```
\l
```

```
kubectl apply -f writer-service.yaml -n postgresql-dev-staging-ns
```

```
kubectl apply -f reader-service.yaml -n postgresql-dev-staging-ns
```

```
kubectl get services -n postgresql-dev-staging-ns
```

```
NAME                           TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
postgresql-cluster-r           ClusterIP   10.2.70.122    <none>        5432/TCP   64s
postgresql-cluster-remote      ClusterIP   10.2.68.39     <none>        5432/TCP   18s
postgresql-cluster-ro          ClusterIP   10.2.3.18      <none>        5432/TCP   64s
postgresql-cluster-ro-remote   ClusterIP   10.2.211.9     <none>        5432/TCP   10s
postgresql-cluster-rw          ClusterIP   10.2.165.186   <none>        5432/TCP   64s
```

Use these endpoint to connect to database
```
postgresql-cluster-ro          ClusterIP   10.2.3.18      <none>        5432/TCP   64s
postgresql-cluster-rw          ClusterIP   10.2.165.186   <none>        5432/TCP   64s
```

Get the PostgreSQL Service FQDN
Ensure you have the FQDN of the PostgreSQL service, which follows this pattern:
```
<service-name>.<namespace>.svc.cluster.local
```
example
```
postgresql.database.svc.cluster.local
```
```
PGPASSWORD=mysecretpassword psql -h postgresql-cluster-rw.postgresql-dev-staging-ns.svc.cluster.local -U postgres -d iotbedb
```
```
postgresql://username:password@postgresql-cluster-rw.postgresql-dev-staging-ns.svc.cluster.local:5432/iotbedb
```