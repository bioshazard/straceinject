
# How to inject

Add this to the top of your `index.php`

```
// TODO: Consolidate to, `include 'straceinject.php';`
// TODO: Thread-aware trace, not needed for low traffic scenario.

class __________epilogue {
  public function __construct() {
    $pid = getmypid();
    $filename = date('U').'_'.uniqid().str_replace('/', '_', $_SERVER['REQUEST_URI']);
    $result = json_decode(file_get_contents("http://localhost:1337/strace/inject/$pid/$filename"), true);
    $this->uuid = $result["uuid"];
  }
  public function __destruct() {
    $result = file_get_contents("http://localhost:1337/strace/kill/".$this->uuid);
  }
}

// This will garbage collect at the end of the PHP page excution, ensuring the __destruct is the last thing to run
$lastSay = new __________epilogue();
```

If developing,

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
