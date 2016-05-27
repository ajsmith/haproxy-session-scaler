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
  myproject/haproxy-session-scaler
```
