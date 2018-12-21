
```
# Requires,
yum install -y rh-python36-python rh-python36-python-pip
/opt/rh/rh-python36/root/bin/pip3 install hug
# Run with,
/opt/rh/rh-python36/root/bin/hug -f straceinject.py -ho 127.0.0.1 -p 1337
```

Example result

```
[root@f92fd5ba8b81 /]# awk '{ print NR,$0 }' /tmp/straceinject_1545368268_node_2791_edit.k | awk '{ print $NF,$1}' | sort -r | head
<0.008817> 10431
<0.005517> 10519
<0.005116> 10486
<0.004879> 10068
<0.004374> 1528
<0.002758> 10432
<0.002146> 10487
<0.002039> 1409
<0.001931> 1538
<0.001627> 1543
[root@f92fd5ba8b81 /]# vim +10431 /tmp/straceinject_1545368268_node_2791_edit.k
```
