========
Examples
========

To query HAProxy session data using curl, we'd do run a command like::

    $ curl -u admin:adminpw "infranode1-e871.oslab.opentlc.com:1936/haproxy-stats;csv"

Below is some sample HAProxxy Session Data from such a command::

    >>> session_data = """\
    ... # pxname,svname,qcur,qmax,scur,smax,slim,stot,bin,bout,dreq,dresp,ereq,econ,eresp,wretr,wredis,status,weight,act,bck,chkfail,chkdown,lastchg,downtime,qlimit,pid,iid,sid,throttle,lbtot,tracked,type,rate,rate_lim,rate_max,check_status,check_code,check_duration,hrsp_1xx,hrsp_2xx,hrsp_3xx,hrsp_4xx,hrsp_5xx,hrsp_other,hanafail,req_rate,req_rate_max,req_tot,cli_abrt,srv_abrt,comp_in,comp_out,comp_byp,comp_rsp,lastsess,last_chk,last_agt,qtime,ctime,rtime,ttime,
    ... stats,FRONTEND,,,1,1,2000,2022,170735,626967,0,0,2,,,,,OPEN,,,,,,,,,1,2,0,,,,0,1,0,493,,,,0,13,0,2008,0,0,,1,493,2022,,,0,0,0,0,,,,,,,,
    ... stats,BACKEND,0,0,0,0,200,0,170735,626967,0,0,,0,0,0,0,UP,0,0,0,,0,5353,0,,1,2,0,,0,,1,0,,0,,,,0,0,0,0,0,0,,,,,0,0,0,0,0,0,0,,,0,0,0,0,
    ... public,FRONTEND,,,0,1,2000,536,109,100148,0,0,535,,,,,OPEN,,,,,,,,,1,3,0,,,,0,0,0,1,,,,0,0,0,535,1,0,,0,1,536,,,0,0,0,0,,,,,,,,
    ... public_ssl,FRONTEND,,,0,1,2000,1,64,0,0,0,0,,,,,OPEN,,,,,,,,,1,4,0,,,,0,0,0,1,,,,,,,,,,,0,0,0,,,0,0,0,0,,,,,,,,
    ... be_sni,fe_sni,0,0,0,0,,0,0,0,,0,,0,0,0,0,no check,1,1,0,,,,,,1,5,1,,0,,2,0,,0,,,,,,,,,,0,,,,0,0,,,,,-1,,,0,0,0,0,
    ... be_sni,BACKEND,0,0,0,0,200,0,0,0,0,0,,0,0,0,0,UP,1,1,0,,0,5353,0,,1,5,0,,0,,1,0,,0,,,,,,,,,,,,,,0,0,0,0,0,0,-1,,,0,0,0,0,
    ... fe_sni,FRONTEND,,,0,0,2000,0,0,0,0,0,0,,,,,OPEN,,,,,,,,,1,6,0,,,,0,0,0,0,,,,0,0,0,0,0,0,,0,0,0,,,0,0,0,0,,,,,,,,
    ... be_no_sni,fe_no_sni,0,0,0,1,,1,64,0,,0,,0,0,0,0,no check,1,1,0,,,,,,1,7,1,,1,,2,0,,1,,,,,,,,,,0,,,,0,0,,,,,4517,,,0,1,0,1,
    ... be_no_sni,BACKEND,0,0,0,1,200,1,64,0,0,0,,0,0,0,0,UP,1,1,0,,0,5353,0,,1,7,0,,1,,1,0,,1,,,,,,,,,,,,,,0,0,0,0,0,0,4517,,,0,1,0,1,
    ... fe_no_sni,FRONTEND,,,0,1,2000,0,0,0,0,0,0,,,,,OPEN,,,,,,,,,1,8,0,,,,0,0,0,0,,,,0,0,0,0,0,0,,0,0,0,,,0,0,0,0,,,,,,,,
    ... openshift_default,BACKEND,0,0,0,1,600,1,109,103,0,0,,1,0,0,0,UP,0,0,0,,0,5353,0,,1,9,0,,0,,1,0,,1,,,,0,0,0,0,1,0,,,,,0,0,0,0,0,0,-1,,,0,0,0,0,
    ... """

The scaler inspects the session data for a given project, and returns a number
of replicas to scale up to.

    >>> import haproxy_session_scaler
    >>> haproxy_session_scaler.scale('openshift_default', session_data)
    1

The scaler adds additional replicas for every 10 sessions. For example, when a
project has 10 sessions, the scaler increases the number of replicas to 2.

    >>> session_data = """\
    ... # pxname,svname,qcur,qmax,scur,smax,slim,stot,bin,bout,dreq,dresp,ereq,econ,eresp,wretr,wredis,status,weight,act,bck,chkfail,chkdown,lastchg,downtime,qlimit,pid,iid,sid,throttle,lbtot,tracked,type,rate,rate_lim,rate_max,check_status,check_code,check_duration,hrsp_1xx,hrsp_2xx,hrsp_3xx,hrsp_4xx,hrsp_5xx,hrsp_other,hanafail,req_rate,req_rate_max,req_tot,cli_abrt,srv_abrt,comp_in,comp_out,comp_byp,comp_rsp,lastsess,last_chk,last_agt,qtime,ctime,rtime,ttime,
    ... openshift_default,BACKEND,0,0,{session_count},1,600,1,109,103,0,0,,1,0,0,0,UP,0,0,0,,0,5353,0,,1,9,0,,0,,1,0,,1,,,,0,0,0,0,1,0,,,,,0,0,0,0,0,0,-1,,,0,0,0,0,
    ... """.format(session_count=10)

    >>> haproxy_session_scaler.scale('openshift_default', session_data)
    2
