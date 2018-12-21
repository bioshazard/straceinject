import hug, threading, subprocess, uuid

uuidPidMap = { }

def doStrace(uniqId, pid, filename):
    cmd = "/usr/bin/strace -T -t -f -v -s4096 -p%d -o /tmp/straceinject_%s.k" % (pid, filename)
    proc = subprocess.Popen(cmd.split(" "), stderr=subprocess.PIPE)
    # Keep track of the PID to kill it later when we are done tracing
    uuidPidMap[uniqId] = proc

@hug.get('/strace/inject/{pid}/{filename}')
def inject(pid: int, filename: str):

    # Generate unique identifier
    uniqId = str(uuid.uuid4())

    # Start a thread to run strace
    t = threading.Thread(target=doStrace, args=(uniqId, pid, filename,))
    t.start()

    return { "uuid": uniqId }

@hug.get('/strace/kill/{targetId}')
def kill(targetId: str):

    print(uuidPidMap)

    procToKill = uuidPidMap.pop(targetId, None)
    if procToKill:
        procToKill.kill()
        # Clean up zombie process
        procToKill.communicate()

    return { "msg": "Killed trace %s" % targetId }

hug.API(__name__).http.serve(host="127.0.0.1",port=1337)
