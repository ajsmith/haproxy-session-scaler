# haxproxy-session-scaler

This provides horizontal pod scaling in OpenShift by using session counts from
HAProxy.

# Tests

To run the tests:

```.shell
python -m doctest -v haproxy_session_scaler.rst
```

# Building with S2I

To build with S2I:

```.shell
s2i build https://github.com/ajsmith/haproxy-session-scaler.git \
  openshift3/python-33-rhel7 \
  haproxy-session-scaler
```

# Running

To run the scaler:

```.shell
python haproxy_session_scaler.py myproject http://haproxy.localdomain:1936/haproxy-stats;csv
```

# Running as a container

When run as a container, the project and HAProxy URL must be set as the
following environment variables on the container:

  * `PROJECT_PROXY_NAME`: The name of the project to monitor.
  * `HAPROXY_STATS_URL`: The URL used to gather session data from HAProxy.

To run with plain ol' Docker:

```.shell
docker run -e PROJECT_PROXY_NAME=myproject \
  -e HAPROXY_STATS_URL=http://haproxy.localdomain:1936/haproxy-stats;csv \
  haproxy-session-scaler
```
